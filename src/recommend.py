import pandas as pd
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np

def get_movie_features(conn):
    """
    Get movie features data from the database.

    Parameters
    ----------
    conn : sqlite3.Connection
        Connection to the SQLite database

    Returns
    -------
    pd.DataFrame
        DataFrame containing movie features
    """
    query = "SELECT * FROM movie_features"
    movie_features_df = pd.read_sql(query, conn)
    return movie_features_df

def recommend_movies(conn, movie_id, top_n=5):
    """
    Recommend movies based on a given movie ID using cosine similarity.

    Parameters
    ----------
    conn : sqlite3.Connection
        Connection to the SQLite database
    movie_id : int
        The ID of the movie to base recommendations on
    top_n : int, optional
        Number of recommendations to return (default is 5)

    Returns
    -------
    list of tuples
        List of recommended movie IDs and their similarity scores
    """
    # Load the movie features from the database
    query = "SELECT * FROM movie_features"
    movie_features_df = pd.read_sql_query(query, conn)

    # Check if the movie_id exists in the DataFrame
    if movie_id not in movie_features_df['movie_id'].values:
        print(f"Movie ID {movie_id} not found in the dataset.")
        return []

    # Get the genre feature columns (all columns except movie_id)
    genre_columns = [col for col in movie_features_df.columns if col.startswith('genre_')]
    
    # Extract the feature matrix
    feature_matrix = movie_features_df[genre_columns].values

    # Compute the cosine similarity matrix
    similarity_matrix = cosine_similarity(feature_matrix)

    # Find the index of the movie to compare against
    movie_idx = movie_features_df[movie_features_df['movie_id'] == movie_id].index[0]

    # Get similarity scores for the selected movie
    similarity_scores = list(enumerate(similarity_matrix[movie_idx]))

    # Sort by similarity score in descending order and exclude the first (itself)
    similarity_scores = sorted(similarity_scores, key=lambda x: x[1], reverse=True)[1:top_n+1]

    # Get the recommended movie IDs and their similarity scores
    recommended_movies = [(int(movie_features_df.iloc[i]['movie_id']), score) for i, score in similarity_scores]

    return recommended_movies

