from flask import Blueprint, jsonify
from src.utils import load_movies_data, get_movie_by_id, get_movie_from_omdb
import os
from dotenv import load_dotenv

load_dotenv()

api_blueprint = Blueprint('api', __name__)

OMDB_API_KEY = os.getenv('OMDB_API_KEY')

@api_blueprint.route('/movies/<int:movie_id>', methods=['GET'])
def get_movie(movie_id):
    """
    Return a movie by ID.

    Parameters
    ----------
    movie_id : int
        Movie ID to retrieve

    Returns
    -------
    JSON response containing the movie information or an error message
    """
    movies_df = load_movies_data()
    movie = get_movie_by_id(movie_id, movies_df)
    if movie:
        omdb_data = get_movie_from_omdb(movie['title'], api_key=OMDB_API_KEY)
        return jsonify(omdb_data)
    else:
        return jsonify({'error': 'Movie not found'}), 404
    
@api_blueprint.route('/movies', methods=['GET'])
def get_all_movies():
    """
    Return all movies in the database.

    Returns
    -------
    JSON response containing a list of all movies
    """
    movies = load_movies_data().to_dict(orient='records')
    return jsonify(movies)
