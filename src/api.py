from flask import Blueprint, jsonify
from src.utils import load_movies_data, get_movie_by_id

api_blueprint = Blueprint('api', __name__)

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
    movie = get_movie_by_id(movie_id)
    if movie:
        return jsonify(movie)
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
