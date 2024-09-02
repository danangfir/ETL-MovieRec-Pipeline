import sqlite3
from src.utils import clean_genre_name
import pandas as pd

def insert_movie_features_data(conn, movies_df):
    """
    Insert movie features data from a DataFrame into the movie_features table in the database.

    Parameters
    ----------
    conn : sqlite3.Connection
        Connection to the SQLite database
    movies_df : pd.DataFrame
        DataFrame containing movie features

    Returns
    -------
    None
    """
    for _, row in movies_df.iterrows():
        cleaned_genres_list = [clean_genre_name(genre) for genre in row.index if genre.startswith('genre_')]
        genre_values = [int(row[f'genre_{genre}']) for genre in cleaned_genres_list]
        placeholders = ', '.join('?' * len(genre_values))
        query = f"INSERT INTO movie_features (movie_id, {', '.join([f'genre_{genre}' for genre in cleaned_genres_list])}) VALUES (?, {placeholders})"
        conn.execute(query, (row['movie_id'], *genre_values))
    conn.commit()



def create_database(db_name):
    
    """
    Create a new SQLite database with the given name.

    Parameters
    ----------
    db_name : str
        The name of the database to create.

    Returns
    -------
    sqlite3.Connection
        A connection to the newly created database.

    """
    conn = sqlite3.connect(db_name)
    return conn

def create_table(conn):
    """
    Create tables in the database for storing movies and their features.

    Parameters
    ----------
    conn : sqlite3.Connection
        Connection to the SQLite database

    Returns
    -------
    None
    """
    # Drop the tables if they exist to avoid conflicts
    conn.execute("DROP TABLE IF EXISTS movies")
    conn.execute("DROP TABLE IF EXISTS movie_features")
    
    create_movies_table = """
    CREATE TABLE IF NOT EXISTS movies (
        movie_id INTEGER PRIMARY KEY,
        title TEXT,
        genres TEXT,
        avg_rating REAL
    );
    """
    create_movie_features_table = """
    CREATE TABLE IF NOT EXISTS movie_features (
        movie_id INTEGER PRIMARY KEY,
        genre_features TEXT
    );
    """
    conn.execute(create_movies_table)
    conn.execute(create_movie_features_table)
    conn.commit()


    
def insert_movies_data(conn, movies_df):
    """
    Insert movie data from a DataFrame into the movies table in the database.

    Parameters
    ----------
    conn : sqlite3.Connection
        Connection to the SQLite database
    movies_df : pd.DataFrame
        DataFrame containing movie information

    Returns
    -------
    None
    """
    for _, row in movies_df.iterrows():
        conn.execute(
            "INSERT OR IGNORE INTO movies (movie_id, title, genres, avg_rating) VALUES (?, ?, ?, ?)",
            (row['movie_id'], row['Title'], ','.join(row['genres']), row.get('avg_rating', None))
        )
    conn.commit()
    
def create_movie_features(cleaned_movie):
    """
    Create a DataFrame with binary columns representing each genre.

    Parameters
    ----------
    cleaned_movie : pd.DataFrame
        DataFrame containing cleaned movie data with a 'genres' column.

    Returns
    -------
    pd.DataFrame
        DataFrame containing one-hot encoded columns for each genre.
    """
    genres = cleaned_movie['genres'][0]
    genre_columns = ['genre_' + genre.replace(' ', '_').replace('-', '_') for genre in genres]
    genre_values = [1 if genre in genres else 0 for genre in ['Action', 'Adventure', 'Sci_Fi']]  # Add more genres as needed
    
    features = pd.DataFrame([genre_values], columns=genre_columns)
    return features


def create_movie_features_table(conn, all_genres):
    """
    Create the movie_features table with a column for each genre.

    Parameters
    ----------
    conn : sqlite3.Connection
        Connection to the SQLite database
    all_genres : list
        List of all genres to create columns for.

    Returns
    -------
    None
    """
    # Drop the table if it exists to avoid conflicts with existing columns
    conn.execute("DROP TABLE IF EXISTS movie_features")
    
    # Create columns for each genre, replacing hyphens and spaces with underscores
    columns = ', '.join([f'genre_{genre.replace(" ", "_").replace("-", "_")} INTEGER' for genre in all_genres])
    create_table_query = f"""
    CREATE TABLE IF NOT EXISTS movie_features (
        movie_id INTEGER PRIMARY KEY,
        {columns}
    );
    """
    conn.execute(create_table_query)
    conn.commit()





def insert_movie_features_data(conn, movie_id, features):
    """
    Insert movie features data from a DataFrame into the movie_features table in the database.

    Parameters
    ----------
    conn : sqlite3.Connection
        Connection to the SQLite database
    movie_id : int
        The ID of the movie to insert features for
    features : pd.DataFrame
        DataFrame containing movie features

    Returns
    -------
    None
    """
    genre_columns = [col.replace(" ", "_").replace("-", "_") for col in features.columns]  # Sanitize column names
    genre_values = features.iloc[0].tolist()
    
    placeholders = ', '.join('?' * len(genre_values))
    query = f"INSERT INTO movie_features (movie_id, {', '.join(genre_columns)}) VALUES (?, {placeholders})"
    
    conn.execute(query, (movie_id, *genre_values))
    conn.commit()







