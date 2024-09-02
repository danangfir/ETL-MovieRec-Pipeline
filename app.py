from flask import Flask, jsonify
from src.api import api_blueprint
from config import DevelopmentConfig

app = Flask(__name__)
app.config.from_object(DevelopmentConfig)
app.register_blueprint(api_blueprint)

if __name__ == "__main__":
    app.run(debug=True)
    
    
@api_blueprint.route('/', methods=['GET'])
def home():
    """
    Return a welcome message for the Movie API.

    Returns
    -------
    JSON response containing a welcome message
    """
    try:
        return jsonify({"message": "Welcome to the Movie API!"})
    except Exception as e:
        return jsonify({"error": str(e)}), 500


@api_blueprint.route('/favicon.ico')
def favicon():
    """Return a 204 status code with an empty body."""
    return "", 204
