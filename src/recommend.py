import sqlite3
import pandas as pd
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np

def get_movie_features(conn):
    query = "SELECT * FROM movie_features"
    movie_features_df = pd.read_sql(query, conn)
    return movie_features_df

def recommend_movies(conn, movie_id, num_recommendations=5):
    movie_features_df = get_movie_features(conn)
    movie_ids = movie_features_df['movie_id'].tolist()
    
    # Get features for the given movie_id
    movie_features = movie_features_df[movie_features_df['movie_id'] == movie_id].iloc[:, 1:].values.reshape(1, -1)
    
    # Compute cosine similarity between this movie and all others
    cosine_similarities = cosine_similarity(movie_features, movie_features_df.iloc[:, 1:].values).flatten()
    
    # Get the indices of the most similar movies
    similar_indices = cosine_similarities.argsort()[::-1][1:num_recommendations+1]
    
    # Get the corresponding movie IDs
    similar_movie_ids = [movie_ids[i] for i in similar_indices]
    
    return similar_movie_ids
