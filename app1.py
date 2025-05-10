import tkinter as tk
from tkinter import messagebox, simpledialog
from tkinter import ttk
import psycopg2

# --- Database Connection ---
conn = psycopg2.connect(
    dbname="project",
    user="postgres",
    password="pgadmin4",
    host="localhost",
    port="5432"
)
cursor = conn.cursor()
CURRENT_USER_ID = 1  # For example, Alice

# --- GUI Setup ---
root = tk.Tk()
root.title("Movie Recommendation System")
root.configure(bg="#FFC0CB")  # Light pink background

# --- Helper Functions ---
def get_genres():
    cursor.execute("SELECT DISTINCT genre FROM movies ORDER BY genre;")
    return [row[0] for row in cursor.fetchall()]

def show_movies_by_genre(genre):
    for i in tree.get_children():
        tree.delete(i)

    cursor.execute("""
    SELECT movie_id, title ,genre ,description,length,rating,release_year FROM movies
    WHERE genre = %s
    AND movie_id NOT IN (
        SELECT movie_id FROM watched WHERE user_id = %s
    );""", (genre, CURRENT_USER_ID))

    for movie in cursor.fetchall():
        tree.insert('', 'end', values=movie)

def add_to_my_list():
    selected_items = tree.selection()
    if not selected_items:  # If no item is selected
        return
    try:
        for item in selected_items:
            movie_id = int(tree.item(item, 'values')[0])
            # Check if already in my_list
            cursor.execute("""SELECT 1 FROM my_list WHERE user_id = %s AND movie_id = %s;""", (CURRENT_USER_ID, movie_id))
            if cursor.fetchone():
                messagebox.showinfo("Info", f"Movie ID {movie_id} is already in My List.")
            else:
                cursor.execute("""
                INSERT INTO my_list (user_id, movie_id)
                VALUES (%s, %s) ON CONFLICT DO NOTHING;""", (CURRENT_USER_ID, movie_id))
        conn.commit()
        messagebox.showinfo("Success", "Movies added to My List.")
    except Exception as e:
        conn.rollback()
        messagebox.showerror("Error", str(e))

def remove_from_my_list():
    selected_items = tree.selection()
    if not selected_items: 
        return
    try:
        for item in selected_items:
            movie_id = int(tree.item(item, 'values')[0])
            cursor.execute("""
            DELETE FROM my_list
            WHERE user_id = %s AND movie_id = %s;""", (CURRENT_USER_ID, movie_id))
        conn.commit()
        messagebox.showinfo("Removed", "Movies removed from My List.")
    except Exception as e:
        conn.rollback()
        messagebox.showerror("Error", str(e))

def view_my_list():
    for i in tree.get_children():
        tree.delete(i)
    cursor.execute("""
    SELECT m.movie_id, m.title, m.description, m.length, m.rating, m.release_year
    FROM my_list ml
    JOIN movies m ON ml.movie_id = m.movie_id
    WHERE ml.user_id = %s;""", (CURRENT_USER_ID,))
    for movie in cursor.fetchall():
        tree.insert('', 'end', values=movie)

def mark_as_watched():
    selected_items = tree.selection()
    if not selected_items:
        return
    try:
        for item in selected_items:
            movie_id = int(tree.item(item, 'values')[0])
            # Check if already in watched
            cursor.execute("""SELECT 1 FROM watched WHERE user_id = %s AND movie_id = %s;""", (CURRENT_USER_ID, movie_id))
            if cursor.fetchone():
                messagebox.showinfo("Info", f"Movie ID {movie_id} is already marked as watched.")
            else:
                cursor.execute("""
                INSERT INTO watched (user_id, movie_id)
                VALUES (%s, %s) ON CONFLICT DO NOTHING;""", (CURRENT_USER_ID, movie_id))
        conn.commit()
        messagebox.showinfo("Watched", "Movies marked as watched.")
    except Exception as e:
        conn.rollback()
        messagebox.showerror("Error", str(e))

def view_watched():
    for i in tree.get_children():
        tree.delete(i)
    cursor.execute("""
    SELECT m.movie_id, m.title, m.description, m.length, m.rating, m.release_year
    FROM watched w
    JOIN movies m ON w.movie_id = m.movie_id
    WHERE w.user_id = %s;""", (CURRENT_USER_ID,))
    for movie in cursor.fetchall():
        tree.insert('', 'end', values=movie)

def remove_from_watched():
    selected_items = tree.selection()
    if not selected_items:
        return
    try:
        for item in selected_items:
            movie_id = int(tree.item(item, 'values')[0])
            cursor.execute("""
            DELETE FROM watched
            WHERE user_id = %s AND movie_id = %s;""", (CURRENT_USER_ID, movie_id))
        conn.commit()
        messagebox.showinfo("Removed", "Movies removed from Watched.")
    except Exception as e:
        conn.rollback()
        messagebox.showerror("Error", str(e))

def undo_last_removal():
    try:
        cursor.execute("""
        SELECT user_id, movie_id, rating
        FROM undo_watched
        WHERE user_id = %s
        ORDER BY movie_id DESC
        LIMIT 1;""", (CURRENT_USER_ID,))
        row = cursor.fetchone()
        if row:
            user_id, movie_id, rating = row
            cursor.execute("""
            INSERT INTO watched (user_id, movie_id, rating)
            VALUES (%s, %s, %s)
            ON CONFLICT DO NOTHING;""", (user_id, movie_id, rating))
            cursor.execute("""
            DELETE FROM undo_watched
            WHERE user_id = %s AND movie_id = %s;""", (user_id, movie_id))
            conn.commit()
            messagebox.showinfo("Undo", f"Restored movie ID {movie_id} to Watched.")
        else:
            messagebox.showinfo("Undo", "No recently removed movie to undo.")
    except Exception as e:
        conn.rollback()
        messagebox.showerror("Error", str(e))

def search_movies():
    movie_name = simpledialog.askstring("Movie Search", "Enter movie name:")
    if not movie_name:
        return
    for i in tree.get_children():
        tree.delete(i)
    cursor.execute("""
    SELECT movie_id, title, description, length, rating, release_year FROM movies
    WHERE title ILIKE %s;""", (f'%{movie_name}%',))
    results = cursor.fetchall()
    if results:
        for movie in results:
            tree.insert('', 'end', values=movie)
    else:
        messagebox.showinfo("Search Result", "No movie found with that name.")

def get_recommendations():
    cursor.execute("""
    SELECT genre, COUNT(*) as count
    FROM watched w
    JOIN movies m ON w.movie_id = m.movie_id
    WHERE w.user_id = %s
    GROUP BY genre
    ORDER BY count DESC
    LIMIT 1;""", (CURRENT_USER_ID,))

    most_watched_genre = cursor.fetchone()
    if not most_watched_genre:
        messagebox.showinfo("Recommendations", "No watched movies to base recommendations on.")
        return

    genre = most_watched_genre[0]
    for i in tree.get_children():
        tree.delete(i)
    cursor.execute("""
    SELECT movie_id, title, description, length, rating, release_year FROM movies
    WHERE genre = %s
    AND movie_id NOT IN (
        SELECT movie_id FROM watched WHERE user_id = %s
    );""", (genre, CURRENT_USER_ID))
    recommendations = cursor.fetchall()
    if recommendations:
        for movie in recommendations:
            tree.insert('', 'end', values=movie)
    else:
        messagebox.showinfo("Recommendations", "No new recommendations available for the most watched genre.")

# --- Updated UI Layout ---
genre_label = tk.Label(root, text="Select Genre:", bg="#FFC0CB")
genre_label.pack()

genre_var = tk.StringVar(root)
genres = get_genres()
genre_menu = tk.OptionMenu(root, genre_var, *genres)
genre_menu.pack()

def on_genre_select(*args):
    selected_genre = genre_var.get()
    if selected_genre:
        show_movies_by_genre(selected_genre)

genre_var.trace("w", on_genre_select)

# Create Treeview for movie display
tree = ttk.Treeview(root, columns=('ID', 'Title', 'Description', 'Length', 'Rating', 'Release Year'), show='headings')
tree.heading('ID', text='Movie ID')
tree.heading('Title', text='Title')
tree.heading('Description', text='Description')
tree.heading('Length', text='Length (min)')
tree.heading('Rating', text='Rating')
tree.heading('Release Year', text='Release Year')
tree.pack()

btn_frame = tk.Frame(root, bg="#FFC0CB")  # Frame background match
btn_frame.pack()

tk.Button(btn_frame, text="Search Movies", command=search_movies).grid(row=0, column=0, padx=5)
tk.Button(btn_frame, text="Add to My List", command=add_to_my_list).grid(row=0, column=1, padx=5)
tk.Button(btn_frame, text="Remove from My List", command=remove_from_my_list).grid(row=0, column=2, padx=5)
tk.Button(btn_frame, text="View My List", command=view_my_list).grid(row=0, column=3, padx=5)
tk.Button(btn_frame, text="Mark as Watched", command=mark_as_watched).grid(row=1, column=0, padx=5)
tk.Button(btn_frame, text="View Watched", command=view_watched).grid(row=1, column=1, padx=5)
tk.Button(btn_frame, text="Remove from Watched", command=remove_from_watched).grid(row=1, column=2, padx=5)
tk.Button(btn_frame, text="Undo Watched Removal", command=undo_last_removal).grid(row=2, column=0, padx=5)
tk.Button(btn_frame, text="Get Recommendations", command=get_recommendations).grid(row=2, column=1, padx=5)

# --- Run App ---
root.mainloop()