import pandas as pd

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

def get_movie_by_id(movie_id, movies_df):
    """
    Get a movie by its ID from the movies_df DataFrame.

    If movies_df is None, it will load the movies data from the default file path.

    Parameters
    ----------
    movie_id : int
        The ID of the movie to retrieve
    movies_df : pd.DataFrame
        DataFrame containing movie information

    Returns
    -------
    pd.DataFrame
        DataFrame containing the movie information for the given movie ID
    """

    if movies_df is None:
        movies_df = load_movies_data()
    return movies_df[movies_df['movie_id'] == movie_id]

    if not movie.empty:
        return movie.to_dict(orient='records')[0]
    return None
