from src.extract import load_movies_data, load_ratings_data
from src.transform import clean_movie_titles, split_genres, calculate_average_ratings, create_movie_features
from src.load import create_database, create_tables, insert_movies_data, insert_movie_features_data
from src.recommend import recommend_movies

def main():
    # Step 1: Extract
    movies_df = load_movies_data('data/movies.csv')
    ratings_df = load_ratings_data('data/ratings.csv')

    # Step 2: Transform
    movies_df = clean_movie_titles(movies_df)
    movies_df = split_genres(movies_df)
    avg_ratings_df = calculate_average_ratings(ratings_df)
    movies_df = movies_df.merge(avg_ratings_df, on='movie_id')
    movies_df = create_movie_features(movies_df)

    # Step 3: Load
    conn = create_database('movies.db')
    create_tables(conn)
    insert_movies_data(conn, movies_df)
    insert_movie_features_data(conn, movies_df)

    # Step 4: Recommendation (CLI)
    while True:
        movie_id = int(input("Enter a movie ID to get recommendations: "))
        recommendations = recommend_movies(conn, movie_id)
        print(f"Recommended movies based on movie ID {movie_id}: {recommendations}")

if __name__ == "__main__":
    main()
