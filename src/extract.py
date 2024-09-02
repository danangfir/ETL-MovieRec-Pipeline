import pandas as pd

def load_movies_data(file_path):
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

def load_ratings_data(file_path):
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

def extract_all_genres(movies_df):
    """
    Extract a list of all unique genres from the movies DataFrame.

    Parameters
    ----------
    movies_df : pd.DataFrame
        DataFrame containing movie information, including genres.

    Returns
    -------
    list
        A list of all unique genres.
    """
    all_genres = set()
    for genres in movies_df['genres']:
        all_genres.update(genres)
    return list(all_genres)