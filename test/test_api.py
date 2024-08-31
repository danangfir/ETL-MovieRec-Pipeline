import pytest
from app import app

@pytest.fixture
def client():
    with app.test_client() as client:
        yield client
        
def test_get_movies(client):
    rv = client.get('/movies/1')
    assert rv.status_code == 200
    json_data = rv.get_json()
    assert 'movieId' in json_data
    
def test_movie_not_found(client):
    rv = client.get('/movies/999999')
    assert rv.status_code == 404
    