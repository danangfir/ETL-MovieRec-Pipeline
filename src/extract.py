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
