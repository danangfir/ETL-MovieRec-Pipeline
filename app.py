from flask import Flask
from src.api import api_blueprint
from config import DevelopmentConfig

app = Flask(__name__)
app.config.from_object(DevelopmentConfig)
app.register_blueprint(api_blueprint)

if __name__ == "__main__":
    app.run(debug=True)
    