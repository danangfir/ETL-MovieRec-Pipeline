import pandas as pd 

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

def spilt_genres(movies_df):
    """
    Split the genres column into a list of genres
    
    Parameters
    ----------
    movies_df : pd.DataFrame
        DataFrame containing movie information
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

def create_movie_features(movies_df):
    """
    Create feature columns in movies_df for each genre

    Parameters
    ----------
    movies_df : pd.DataFrame
        DataFrame containing movie information

    Returns
    -------
    movies_df : pd.DataFrame
        DataFrame containing feature columns for each genre
    """
    genres_list = list(set([genre for sublist in movies_df['genres'].tolist() for genre in sublist]))
    for genre in genres_list:
        movies_df[f'genre_{genre}'] = movies_df['genres'].apply(lambda x: 1 if genre in x else 0)
        return movies_df
    
    