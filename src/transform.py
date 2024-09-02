import pandas as pd 
from src.utils import clean_genre_name

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


def clean_movie_titles(movies_df):
    """
    Clean the movie titles by removing the year from the genres column
    
    Parameters
    ----------
    movies_df : pd.DataFrame
        DataFrame containing movie information
    
    Returns
    -------
    movies_df : pd.DataFrame
        DataFrame containing clean movie titles
    """
    
    movies_df['title'] = movies_df['genres'].str.replace(r'\(\d{4}\)', '').str.strip()
    return movies_df

def split_genres(movies_df):    
    """
    Convert genres from pipe-separated string to list
    
    Parameters
    ----------
    movies_df : pd.DataFrame
        DataFrame containing movie information
    
    Returns
    -------
    movies_df : pd.DataFrame
        DataFrame containing genres as a list
    """

    movies_df['genres'] = movies_df['genres'].apply(lambda x: x.split('|'))
    return movies_df

def calculate_average_ratings(ratings_df):
    """
    Calculate average ratings for each movie

    Parameters
    ----------
    ratings_df : pd.DataFrame
        DataFrame containing user ratings

    Returns
    -------
    avg_ratings : pd.DataFrame
        DataFrame containing average ratings for each movie
    """

    avg_ratings = ratings_df.groupby('movie_id')['rating'].mean().reset_index()
    avg_ratings.rename(columns={'rating': 'avg_rating'}, inplace=True)
    return avg_ratings

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
    # Extract genres from the first row (assuming a single movie)
    genres = cleaned_movie['genres'][0]  # This is a list of genres, e.g., ['Action', 'Adventure', 'Sci-Fi']
    
    # Define the genres you want to include (or you can dynamically determine this)
    all_genres = ['Action', 'Adventure', 'Sci-Fi']  # Add more genres as needed
    
    # Create a dictionary with genre columns
    genre_dict = {f'genre_{genre.replace(" ", "_")}': (1 if genre in genres else 0) for genre in all_genres}
    
    # Convert dictionary to DataFrame
    features = pd.DataFrame([genre_dict])
    
    return features
  

def clean_movie_titles(movies_df):
    """
    Clean the movie titles by removing the year from the title column.
    
    Parameters
    ----------
    movies_df : pd.DataFrame
        DataFrame containing movie information
    
    Returns
    -------
    movies_df : pd.DataFrame
        DataFrame containing clean movie titles
    """
    movies_df['title'] = movies_df['title'].str.replace(r'\(\d{4}\)', '').str.strip()
    return movies_df

