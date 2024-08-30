import sqlite3


def create_database(db_name):
    conn = sqlite3.connect(db_name)
    return conn

def create_table(conn):
    create_movies_table = """ CREATE TABLE IF NOT EXISTS movies (
        movie_id integer PRIMARY KEY,
        title text,
        genres text,
        avg_rating REAL
        ); """
        
    create_movie_features_table = """ CREATE TABLE IF NOT EXISTS movie_features (
        movie_id integer PRIMARY KEY,
        genre_feat TEXT
        ); """
        
        
    conn.execute(create_movies_table)
    conn.execute(create_movie_features_table)
    conn.commit()
    
def insert_movies_data(conn, movies_df):
    for _, row in movies_df.iterrows():
        conn.execute(
            "INSERT INTO movies (movie_id, title, genres, avg_rating) VALUES (?, ?, ?, ?)",
            (row['movie_id'], row['title'], ','.join(row['genres']), row['avg_rating'])
        )
    conn.commit()

def insert_movie_features_data(conn, movies_df):
    for _, row in movies_df.iterrows():
        genre_features = ','.join([str(int(row[f'genre_{genre}'])) for genre in row.index if genre.startswith('genre_')])
        conn.execute(
            "INSERT INTO movie_features (movie_id, genre_features) VALUES (?, ?)",
            (row['movie_id'], genre_features)
        )
    conn.commit()
