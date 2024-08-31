# API Documentation

## Endpoint: GET /movies/<movie_id>

- **Description**: Retrieves information about a specific movie by its ID.
- **Parameters**:
  - `movie_id` (int): The ID of the movie to retrieve.
- **Response**:
  - `200 OK`: Returns a JSON object with the movie details.
  - `404 Not Found`: If the movie ID does not exist.
- **Example Request**:
  ```bash
  curl -X GET http://localhost:5000/movies/1

```json
{
  "movieId": 1,
  "title": "Toy Story",
  "genres": "Animation|Children's|Comedy",
  "avg_rating": 3.9
}
```
