from src.utils import get_movie_by_id, load_movies_data

def test_get_movie_by_id():
    movies_df = load_movies_data()
    movie = get_movie_by_id(1, movies_df)
    assert movie['movieId'] == 1
    assert 'title' in movie
    