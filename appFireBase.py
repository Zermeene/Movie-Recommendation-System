import tkinter as tk
from tkinter import messagebox, ttk
import pyttsx3
import firebase_admin
from firebase_admin import credentials, firestore
from collections import Counter

#Initialize Firebase
def initialize_firebase():
    if not firebase_admin._apps:
        cred = credentials.Certificate(r"D:\movies\movie-recommendation-sys-bb651-firebase-adminsdk-fbsvc-da82ecd839.json")
        firebase_admin.initialize_app(cred)
    return firestore.client()

#CRUD Operations
def delete_document(collection, document_id):
    db = firestore.client()
    doc_ref = db.collection(collection).document(document_id)
    doc_ref.delete()
    print('Document deleted successfully!')

def read_document(collection, document_id):
    db = firestore.client()
    doc_ref = db.collection(collection).document(document_id)
    document = doc_ref.get()
    if document.exists:
        return document.to_dict()
    else:
        print('No such document!')
        return None

def add_document(collection, data):
    db = firestore.client()
    db.collection(collection).add(data)
    print('Document added successfully!')

def update_document(collection, document_id, update_data):
    db = firestore.client()
    doc_ref = db.collection(collection).document(document_id)
    doc_ref.update(update_data)
    print('Document updated successfully!')

#Search all movies
def search_all_movies(title):
    db = firestore.client()
    movies_ref = db.collection("movies").stream()
    results = []
    for doc in movies_ref:
        data = doc.to_dict()
        if title.lower() in data.get('title', '').lower(): 
            data['id'] = doc.id  
            results.append(data)
    return results

#Voice Feedback Function
def speak(text):
    engine = pyttsx3.init()
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[1].id)
    engine.setProperty('rate', 150)
    engine.setProperty('volume', 0.9)
    engine.say(text)
    engine.runAndWait()

speak("we welcome you to our Movie recommendation system.")
#Recommendation Function
def get_recommendations():
    user_movies = fb_client.collection('my_list').where('user_id', '==', CURRENT_USER_ID).stream()
    genres = []
    user_movie_ids = set()

    for doc in user_movies:
        data = doc.to_dict()
        genres.append(data.get('genre', ''))
        user_movie_ids.add(data.get('ID')) 

    if genres:
        top_genres = Counter(genres).most_common(3)
        recommendations = set()

        for genre, _ in top_genres:
            genre_movies = fb_client.collection('movies').where('genre', '==', genre).stream()
            for movie in genre_movies:
                movie_data = movie.to_dict()
                movie_data['id'] = movie.id

               
                if movie.id not in user_movie_ids:
                    recommendation_tuple = (
                        movie.id,
                        movie_data.get('title', ''),
                        movie_data.get('genre', ''),
                        movie_data.get('description', ''),
                        movie_data.get('length', ''),
                        movie_data.get('rating', ''),
                        movie_data.get('release_year', '')
                    )
                    recommendations.add(recommendation_tuple)

        speak("Top recommended movies.")
        return list(recommendations)[:5]
    else:
        speak("No movie to recommend.")
        return []
  

#Main App
def main_app():
    global CURRENT_USER_ID, tree, last_deleted_document, fb_client

    CURRENT_USER_ID = 1 
    fb_client = initialize_firebase()
    last_deleted_document = None  

    root = tk.Tk()
    root.title("🎀 Movie Recommendation System 🎬")
    root.configure(bg="#FFD1DC")
    custom_font = ("Comic Sans MS", 10, "bold")

    #Treeview Setup
    columns = ("ID", "Title", "Genre", "Description", "Length", "Rating", "Year")
    tree = ttk.Treeview(root, columns=columns, show='headings', height=15)
    for col in columns:
        tree.heading(col, text=col)
        if col == "ID":
            tree.column(col, width=50)
        elif col == "Title":
            tree.column(col, width=150)
        elif col == "Genre":
            tree.column(col, width=75)
        elif col == "Description":
            tree.column(col, width=400)
        elif col in ["Rating", "Year"]:
            tree.column(col, width=50)
        else:
            tree.column(col, width=100)
    tree.pack(pady=10)

    #Function to Get Genres
    def get_genres():
        genres = set()
        docs = fb_client.collection('movies').stream()
        for doc in docs:
            data = doc.to_dict()
            if 'genre' in data:
                genres.add(data['genre'])
        genres.add("ALL")  
        return sorted(list(genres))

    #Show Movies by Genre
    def show_movies_by_genre(genre):
        for i in tree.get_children():
            tree.delete(i)

        if genre == "ALL":
            docs = fb_client.collection('movies').stream()
        else:
            docs = fb_client.collection('movies').where('genre', '==', genre).stream()

        for doc in docs:
            data = doc.to_dict()
            tree.insert('', 'end', values=(
                doc.id, 
                data.get('title', ''),
                data.get('genre', ''),
                data.get('description', ''),
                data.get('length', ''),
                data.get('rating', ''),
                data.get('release_year', '')
            ))

        if not tree.get_children():
            speak("No movies found for this genre.")

    #Add To My List
    def add_to_my_list():
        selected_items = tree.selection()
        if not selected_items:
            speak("Please select a movie to add.")
            return
        for item in selected_items:
            movie_data = tree.item(item, 'values')
            movie_id = movie_data[0] 
            add_document('my_list', {
                'ID': movie_data[0],
                'title': movie_data[1],
                'genre': movie_data[2],
                'description': movie_data[3],
                'length': movie_data[4],
                'rating': movie_data[5],
                'release_year': movie_data[6],
                'user_id': CURRENT_USER_ID
            })
        speak("Movie added to My List.")

    #Show My List
    def show_my_list():
        query_and_display('my_list', "No movies in your list.")

    #Helper Function to Query and Display
    def query_and_display(collection, no_records_message):
        for i in tree.get_children():
            tree.delete(i)

        docs = fb_client.collection(collection).where('user_id', '==', CURRENT_USER_ID).stream()
        if not docs:
            speak(no_records_message)
        for doc in docs:
            data = doc.to_dict()
            tree.insert('', 'end', values=(
                doc.id,  
                data.get('title', ''),
                data.get('genre', ''),
                data.get('description', ''),
                data.get('length', ''),
                data.get('rating', ''),
                data.get('release_year', '')
            ))

    #Delete From My List
    def delete_from_my_list():
        global last_deleted_document
        selected_items = tree.selection()
        if not selected_items:
            speak("Please select a movie to delete.")
            return
        for item in selected_items:
            movie_id = tree.item(item, 'values')[0]  
            last_movie_data = read_document('my_list', movie_id)  
            if last_movie_data: 
                last_deleted_document = last_movie_data
            delete_document('my_list', movie_id)  
            
        show_my_list()  
        speak("Movie deleted successfully from My List.")

    
    def undo_delete():
        global last_deleted_document
        if last_deleted_document:
            add_document('my_list', last_deleted_document)  
            speak("Undid last delete action.")
            last_deleted_document = None
            show_my_list()  
        else:
            speak("No delete action to undo.")

    #Search Movies
    def search_movies_by_title():
        search_term = search_entry.get()
        if search_term:
            results = search_all_movies(search_term)
            for i in tree.get_children():
                tree.delete(i)
            for movie in results:
                tree.insert('', 'end', values=(
                    movie.get('id'),
                    movie.get('title', ''),
                    movie.get('genre', ''),
                    movie.get('description', ''),
                    movie.get('length', ''),
                    movie.get('rating', ''),
                    movie.get('release_year', '')
                ))
            if not results:
                speak("No movies found matching the search term.")
        else:
            speak("Please enter a title to search.")

    
    def recommend_movies():
        recommendations = get_recommendations()
        for i in tree.get_children():
            tree.delete(i)
        for movie in recommendations:
            tree.insert('', 'end', values=movie)

    
    genre_var = tk.StringVar(root)
    genres = get_genres()
    if not genres:
        messagebox.showerror("Error", "No genres found.")
        root.destroy()
        return

    genre_var.set(genres[0])  
    genre_menu = ttk.OptionMenu(root, genre_var, genres[0], *genres)
    genre_menu.pack(pady=5)

    
    button_frame = tk.Frame(root, bg="#FFD1DC")
    button_frame.pack(pady=5)

    
    search_entry = tk.Entry(root)
    search_entry.pack(pady=5)

    
    ttk.Button(button_frame, text="🎬 Show Movies", command=lambda: show_movies_by_genre(genre_var.get())).pack(side=tk.LEFT, padx=5)
    ttk.Button(button_frame, text="➕ Add to My List", command=add_to_my_list).pack(side=tk.LEFT, padx=5)
    ttk.Button(button_frame, text="✅ Show My List", command=show_my_list).pack(side=tk.LEFT, padx=5)
    ttk.Button(button_frame, text="🗑️ Delete from My List", command=delete_from_my_list).pack(side=tk.LEFT, padx=5)
    ttk.Button(button_frame, text="↩️ Undo Delete", command=undo_delete).pack(side=tk.LEFT, padx=5)
    ttk.Button(button_frame, text="🔍 Search Movies", command=search_movies_by_title).pack(side=tk.LEFT, padx=5)
    ttk.Button(button_frame, text="✨ Get Recommendations", command=recommend_movies).pack(side=tk.LEFT, padx=5)

    root.mainloop()
    speak("Exiting movie recommendation systtem")

#Start
if __name__ == "__main__":
    main_app()
