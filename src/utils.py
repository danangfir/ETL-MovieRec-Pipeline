import pandas as pd
import requests

def load_movies_data(file_path='data/movies.csv'):
    """
    Load movies data from CSV file.

    Parameters
    ----------
    file_path : str
        Path to the CSV file containing movies data

    Returns
    -------
    pd.DataFrame
        DataFrame containing movies data
    """
    return pd.read_csv(file_path)

def load_ratings_data(file_path='data/ratings.csv'):
    """
    Load ratings data from CSV file.

    Parameters
    ----------
    file_path : str
        Path to the CSV file containing ratings data

    Returns
    -------
    pd.DataFrame
        DataFrame containing ratings data
    """
    return pd.read_csv(file_path)

def get_movie_by_id(movie_id, movies_df=None):
    """
    Get a movie by its ID from the movies_df DataFrame.

    If movies_df is None, it will load the movies data from the default file path.

    Parameters
    ----------
    movie_id : int
        The ID of the movie to retrieve
    movies_df : pd.DataFrame, optional
        DataFrame containing movie information

    Returns
    -------
    dict or None
        A dictionary containing the movie information for the given movie ID, or None if not found
    """
    if movies_df is None:
        movies_df = load_movies_data()
    movie = movies_df[movies_df['movieId'] == movie_id]  # Adjusted to match common MovieLens dataset column name

    if not movie.empty:
        return movie.to_dict(orient='records')[0]
    return None

def get_movie_from_omdb(movie_title, api_key='YOUR_OMDB_API_KEY'):
    """
    Retrieve movie details from OMDb API.

    Parameters
    ----------
    movie_title : str
        Title of the movie to retrieve from OMDb
    api_key : str
        OMDb API key

    Returns
    -------
    dict
        A dictionary containing the movie details or an error message
    """
    url = f"http://www.omdbapi.com/?t={movie_title}&apikey={api_key}"
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        return {'error': 'Could not retrieve data from OMDb'}
