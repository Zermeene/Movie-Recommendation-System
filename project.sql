-- ========================================
-- Table: movies
-- ========================================
CREATE TABLE movies (
    movie_id SERIAL PRIMARY KEY,
    title VARCHAR(255),
    genre VARCHAR(100),
    description TEXT,
    length INT,
    rating FLOAT,
    release_year INT
);

-- Sample Movies
INSERT INTO movies (title, genre, description, length, rating, release_year) VALUES
('Inception', 'Sci-Fi', 'A mind-bending thriller about dream infiltration.', 148, 8.8, 2010),
('The Shawshank Redemption', 'Drama', 'Two imprisoned men bond over a number of years.', 142, 9.3, 1994),
('The Dark Knight', 'Action', 'Batman faces off against the Joker.', 152, 9.0, 2008),
('Interstellar', 'Sci-Fi', 'A team travels through a wormhole in space.', 169, 8.6, 2014),
('Parasite', 'Thriller', 'A poor family schemes to become employed by a wealthy one.', 132, 8.6, 2019),
('Forrest Gump', 'Drama', 'The story of a man who witnessed and influenced historical events.', 142, 8.8, 1994),
('The Matrix', 'Sci-Fi', 'A hacker learns the world is a simulated reality.', 136, 8.7, 1999),
('Gladiator', 'Action', 'A betrayed general seeks revenge.', 155, 8.5, 2000),
('Titanic', 'Romance', 'A love story aboard the ill-fated RMS Titanic.', 195, 7.8, 1997),
('The Godfather', 'Crime', 'The aging patriarch of an organized crime dynasty transfers control.', 175, 9.2, 1972),
('The Avengers', 'Action', 'Earth''s mightiest heroes must unite.', 143, 8.0, 2012),
('Joker', 'Drama', 'A mentally troubled man turns to crime.', 122, 8.4, 2019),
('Coco', 'Animation', 'A boy journeys into the Land of the Dead.', 105, 8.4, 2017),
('Finding Nemo', 'Animation', 'A clownfish searches for his missing son.', 100, 8.1, 2003),
('The Lion King', 'Animation', 'A young lion prince flees his kingdom.', 88, 8.5, 1994),
('Avengers: Endgame', 'Action', 'The Avengers assemble once more.', 181, 8.4, 2019),
('Up', 'Animation', 'A man ties balloons to his house and flies to South America.', 96, 8.2, 2009),
('Toy Story', 'Animation', 'Toys come to life when humans are not around.', 81, 8.3, 1995),
('Black Panther', 'Action', 'The king of Wakanda fights to secure his nation.', 134, 7.3, 2018),
('Frozen', 'Animation', 'A princess sets off to find her sister.', 102, 7.4, 2013),
('La La Land', 'Romance', 'A musician and an actress fall in love.', 128, 8.0, 2016),
('Whiplash', 'Drama', 'A student drummer under a ruthless instructor.', 107, 8.5, 2014),
('The Notebook', 'Romance', 'A poor man falls in love with a rich woman.', 123, 7.8, 2004),
('1917', 'War', 'Two soldiers race to save 1600 men.', 119, 8.3, 2019),
('Tenet', 'Sci-Fi', 'An operative manipulates the flow of time.', 150, 7.4, 2020),
('The Prestige', 'Mystery', 'Two rival magicians engage in a deadly competition.', 130, 8.5, 2006),
('Shutter Island', 'Mystery', 'A U.S. Marshal investigates a psychiatric facility.', 138, 8.2, 2010),
('Django Unchained', 'Western', 'A freed slave sets out to rescue his wife.', 165, 8.4, 2012),
('The Revenant', 'Adventure', 'A frontiersman fights for survival.', 156, 8.0, 2015),
('The Irishman', 'Crime', 'A hitman recalls his past.', 209, 7.8, 2019),
('Inglourious Basterds', 'War', 'A group plots to assassinate Nazi leaders.', 153, 8.3, 2009),
('Doctor Strange', 'Fantasy', 'A surgeon becomes a master of mystic arts.', 115, 7.5, 2016),
('Ant-Man', 'Action', 'A thief gains the power to shrink.', 117, 7.3, 2015),
('Logan', 'Action', 'An aging Wolverine cares for Professor X.', 137, 8.1, 2017),
('Deadpool', 'Action', 'A mercenary becomes a superhero.', 108, 8.0, 2016),
('The Social Network', 'Drama', 'The founding of Facebook.', 120, 7.7, 2010),
('The Wolf of Wall Street', 'Biography', 'A stockbroker rises and falls.', 180, 8.2, 2013),
('The Grand Budapest Hotel', 'Comedy', 'A hotel concierge is framed for murder.', 99, 8.1, 2014),
('Get Out', 'Horror', 'A black man uncovers a disturbing secret.', 104, 7.7, 2017),
('A Quiet Place', 'Horror', 'A family lives in silence to avoid monsters.', 90, 7.5, 2018),
('It', 'Horror', 'A group of kids fight a shape-shifting evil.', 135, 7.3, 2017),
('The Conjuring', 'Horror', 'Paranormal investigators help a family.', 112, 7.5, 2013),
('Skyfall', 'Action', 'James Bond investigates a cyber attack.', 143, 7.8, 2012),
('Mission Impossible: Fallout', 'Action', 'Ethan Hunt tries to prevent a nuclear disaster.', 147, 7.7, 2018),
('Blade Runner 2049', 'Sci-Fi', 'A blade runner uncovers a long-buried secret.', 164, 8.0, 2017),
('Her', 'Romance', 'A man falls in love with an AI assistant.', 126, 8.0, 2013),
('Ex Machina', 'Sci-Fi', 'A programmer evaluates a humanoid AI.', 108, 7.7, 2014),
('The Truman Show', 'Drama', 'A man discovers his whole life is a TV show.', 103, 8.1, 1998),
('Arrival', 'Sci-Fi', 'A linguist communicates with aliens.', 116, 7.9, 2016);

INSERT INTO movies (title, genre, description, length, rating, release_year) VALUES
('Superbad', 'Comedy', 'Teen friends plan a wild night before graduation.', 113, 7.6, 2007),
('The Hangover', 'Comedy', 'A bachelor party goes terribly wrong in Las Vegas.', 100, 7.7, 2009),
('Step Brothers', 'Comedy', 'Two middle-aged men become stepbrothers and rivals.', 98, 6.9, 2008),
('Bridesmaids', 'Comedy', 'A woman faces chaos as her best friend gets married.', 125, 6.8, 2011),
('Anchorman', 'Comedy', 'A 1970s news anchor battles new trends.', 94, 7.1, 2004),
('Dumb and Dumber', 'Comedy', 'Two dim-witted friends go on a road trip.', 107, 7.3, 1994),
('Zoolander', 'Comedy', 'A clueless male model is brainwashed for assassination.', 89, 6.5, 2001),
('Napoleon Dynamite', 'Comedy', 'A quirky teen navigates high school life.', 96, 6.9, 2004),
('Borat', 'Comedy', 'A Kazakh journalist explores America in absurd ways.', 84, 7.3, 2006),
('Tropic Thunder', 'Comedy', 'Actors making a war movie get caught in real conflict.', 107, 7.0, 2008),
('Pitch Perfect', 'Comedy', 'A college a cappella group aims for redemption.', 112, 7.1, 2012),
('The 40-Year-Old Virgin', 'Comedy', 'A middle-aged man seeks love and confidence.', 116, 7.1, 2005),
('Crazy Rich Asians', 'Comedy', 'A woman meets her wealthy boyfriend’s family.', 121, 6.9, 2018),
('Game Night', 'Comedy', 'A game night turns into a real mystery.', 100, 6.9, 2018),
('The Nice Guys', 'Comedy', 'A PI and a tough guy team up for a strange case.', 116, 7.4, 2016),
('Palm Springs', 'Comedy', 'Two wedding guests get stuck in a time loop.', 90, 7.4, 2020),
('The Other Guys', 'Comedy', 'Two mismatched cops stumble into a big case.', 107, 6.7, 2010),
('Yes Man', 'Comedy', 'A man challenges himself to say yes to everything.', 104, 6.8, 2008),
('Role Models', 'Comedy', 'Two men are forced into a youth mentorship program.', 99, 6.8, 2008),
('Horrible Bosses', 'Comedy', 'Three friends plot to take down their terrible employers.', 98, 6.9, 2011),
('Knives Out', 'Comedy', 'A detective investigates a wealthy family’s murder mystery.', 130, 7.9, 2019),
('Juno', 'Comedy', 'A teen navigates an unexpected pregnancy.', 96, 7.5, 2007),
('Scott Pilgrim vs. the World', 'Comedy', 'A slacker fights his new girlfriend’s evil exes.', 112, 7.5, 2010),
('Mean Girls', 'Comedy', 'A teen enters the ruthless world of high school cliques.', 97, 7.1, 2004),
('The Grand Seduction', 'Comedy', 'A small town tries to charm a doctor.', 112, 7.0, 2013),
('Lady Bird', 'Comedy', 'A teenager rebels against her mother while growing up.', 94, 7.4, 2017),
('Easy A', 'Comedy', 'A girl’s reputation spirals after a false rumor.', 92, 7.0, 2010),
('Little Miss Sunshine', 'Comedy', 'A family travels cross-country for a beauty pageant.', 101, 7.8, 2006),
('Shaun of the Dead', 'Comedy', 'A man tries to win back his ex during a zombie apocalypse.', 99, 7.9, 2004),
('Hot Fuzz', 'Comedy', 'A top cop is reassigned to a quiet village hiding secrets.', 121, 7.8, 2007),
('The World’s End', 'Comedy', 'Friends reunite for a pub crawl that turns alien.', 109, 7.0, 2013),
('The Intern', 'Comedy', 'A retired man becomes an intern at a fashion startup.', 121, 7.1, 2015),
('School of Rock', 'Comedy', 'A musician fakes being a teacher and starts a band.', 108, 7.2, 2003),
('Liar Liar', 'Comedy', 'A lawyer is cursed to tell the truth for 24 hours.', 86, 6.9, 1997),
('Legally Blonde', 'Comedy', 'A fashion major enrolls in Harvard Law School.', 96, 6.4, 2001),
('EuroTrip', 'Comedy', 'Teens travel across Europe in search of love.', 92, 6.6, 2004),
('The Proposal', 'Comedy', 'A boss fakes an engagement with her assistant.', 108, 6.7, 2009),
('Date Night', 'Comedy', 'A couple’s night out spirals into crime.', 88, 6.3, 2010),
('Death at a Funeral', 'Comedy', 'A family funeral is disrupted by secrets and chaos.', 90, 7.4, 2007),
('The Heat', 'Comedy', 'An FBI agent teams with a Boston cop.', 117, 6.6, 2013),
('Spy', 'Comedy', 'A desk-bound analyst goes undercover.', 120, 7.0, 2015),
('Dinner for Schmucks', 'Comedy', 'A man must bring an eccentric guest to a dinner.', 114, 5.9, 2010),
('The Pink Panther', 'Comedy', 'An inspector investigates a stolen diamond.', 93, 5.6, 2006),
('Johnny English', 'Comedy', 'A bumbling spy tries to foil an evil plan.', 88, 6.2, 2003),
('Johnny English Reborn', 'Comedy', 'The clumsy agent returns for a new mission.', 101, 6.3, 2011),
('Johnny English Strikes Again', 'Comedy', 'The secret agent must stop a cyber-attack.', 89, 6.2, 2018),
('My Big Fat Greek Wedding', 'Comedy', 'A Greek woman falls for a non-Greek man.', 95, 6.6, 2002),
('What We Do in the Shadows', 'Comedy', 'Vampires share a house in modern New Zealand.', 86, 7.6, 2014),
('The Dictator', 'Comedy', 'A dictator tries to keep his power while visiting the U.S.', 83, 6.4, 2012),
('The Death of Stalin', 'Comedy', 'Chaos erupts after Stalin’s death.', 107, 7.2, 2017);

-- ========================================
-- Table: users
-- ========================================
CREATE TABLE users (
    user_id SERIAL PRIMARY KEY,
    username VARCHAR(100) UNIQUE NOT NULL,
    password VARCHAR(100) NOT NULL
);

-- Sample Users
INSERT INTO users (username, password) VALUES
('alice', 'pass123'),
('bob', 'secure456');

-- ========================================
-- Table: my_list
-- ========================================
CREATE TABLE my_list (
    list_id SERIAL PRIMARY KEY,
    user_id INT REFERENCES users(user_id) ON DELETE CASCADE,
    movie_id INT REFERENCES movies(movie_id) ON DELETE CASCADE,
    watched BOOLEAN DEFAULT FALSE
);

-- Sample "My List" Entries
INSERT INTO my_list (user_id, movie_id, watched) VALUES
(1, 1, FALSE),  -- Alice added "The Matrix"
(1, 3, FALSE),  -- Alice added "The Godfather"
(2, 2, FALSE),  -- Bob added "Inception"
(2, 4, TRUE);   -- Bob watched "The Dark Knight" (will move via trigger)

-- ========================================
-- Table: watched
-- ========================================
CREATE TABLE watched (
    watch_id SERIAL PRIMARY KEY,
    user_id INT REFERENCES users(user_id) ON DELETE CASCADE,
    movie_id INT REFERENCES movies(movie_id) ON DELETE CASCADE,
    rating FLOAT,
    watched_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- ========================================
-- Trigger Function: move_to_watched_on_flag
-- ========================================
CREATE OR REPLACE FUNCTION move_to_watched_on_flag()
RETURNS TRIGGER AS $$
BEGIN
    IF NEW.watched = TRUE THEN
        INSERT INTO watched(user_id, movie_id, rating)
        VALUES (NEW.user_id, NEW.movie_id, NULL);

        DELETE FROM my_list
        WHERE user_id = NEW.user_id AND movie_id = NEW.movie_id;
    END IF;
    RETURN NEW;
END;
$$ LANGUAGE plpgsql;

-- ========================================
-- Trigger: on UPDATE of my_list.watched = TRUE
-- ========================================
CREATE TRIGGER trg_watch_flag
AFTER UPDATE ON my_list
FOR EACH ROW
WHEN (NEW.watched = TRUE)
EXECUTE FUNCTION move_to_watched_on_flag();

-- ========================================
-- Optional: Genre stats (future use)
-- ========================================
CREATE TABLE genre_stats (
    genre VARCHAR(100) PRIMARY KEY,
    watch_count INT DEFAULT 0
);
CREATE TABLE undo_watched (
    user_id INT,
    movie_id INT,
    rating INT,
    PRIMARY KEY (user_id, movie_id),
    FOREIGN KEY (user_id) REFERENCES users(user_id),
    FOREIGN KEY (movie_id) REFERENCES movies(movie_id)
);

-- Create a function to move movies from "watched" to "undo_watched"
CREATE OR REPLACE FUNCTION move_to_undo_watched()
RETURNS TRIGGER AS $$
BEGIN
    -- Insert the movie into the undo_watched table when it's deleted from watched
    INSERT INTO undo_watched (user_id, movie_id, rating)
    VALUES (OLD.user_id, OLD.movie_id, OLD.rating);
    RETURN OLD;
END;
$$ LANGUAGE plpgsql;

-- Create a trigger to call this function after a delete on watched table
CREATE TRIGGER after_delete_from_watched
AFTER DELETE ON watched
FOR EACH ROW
EXECUTE FUNCTION move_to_undo_watched();
select* from undo_watched;
