from src.recommend import recommend_movies
from src.extract import load_movies_data, load_ratings_data, extract_all_genres
from src.transform import clean_movie_titles, split_genres, calculate_average_ratings, create_movie_features
from src.load import create_database, create_table, insert_movies_data, insert_movie_features_data, create_movie_features_table
from src.utils import get_movie_from_omdb, clean_movie_data

import os
from dotenv import load_dotenv

def main():
    # Load environment variables and set up database connection
    load_dotenv()
    OMDB_API_KEY = os.getenv('OMDB_API_KEY')
    conn = create_database('movies.db')
    
    # Extract all genres from your movie dataset
    movie_titles = ["Inception", "The Matrix", "Interstellar"]
    all_genres = ['Action', 'Adventure', 'Sci-Fi']  # This should be dynamically determined if possible
    
    # Create the movie_features table with all genre columns
    create_movie_features_table(conn, all_genres)
    
    movie_id = 1  # Start with movie_id = 1
    for title in movie_titles:
        movie_data = get_movie_from_omdb(title, OMDB_API_KEY)
        if 'error' not in movie_data:
            cleaned_movie = clean_movie_data(movie_data)
            cleaned_movie['movie_id'] = movie_id  # Assign the movie_id
            
            # Print the movie ID being processed
            print(f"Inserting movie ID {movie_id} for {title}")
            
            # Create features for the movie
            features = create_movie_features(cleaned_movie)
            
            # Insert data into the database
            insert_movies_data(conn, cleaned_movie)
            insert_movie_features_data(conn, movie_id, features)
            
            movie_id += 1  # Increment the movie ID for the next movie

    # Recommendation (CLI)
    while True:
        movie_id = int(input("Enter a movie ID to get recommendations: "))
        recommendations = recommend_movies(conn, movie_id)
        print(f"Recommended movies based on movie ID {movie_id}: {recommendations}")

if __name__ == "__main__":
    main()

