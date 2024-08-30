import sqlite3


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
            "INSERT INTO movies (movie_id, title, genres, avg_rating) VALUES (?, ?, ?, ?)",
            (row['movie_id'], row['title'], ','.join(row['genres']), row['avg_rating'])
        )
    conn.commit()

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
        genre_features = ','.join([str(int(row[f'genre_{genre}'])) for genre in row.index if genre.startswith('genre_')])
        conn.execute(
            "INSERT INTO movie_features (movie_id, genre_features) VALUES (?, ?)",
            (row['movie_id'], genre_features)
        )
    conn.commit()
