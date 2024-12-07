import pytest
from django.test import Client
from model_bakery import baker

from movies.models import Movie
from movies.serializers import MovieSerializer


@pytest.mark.django_db
def test_post_method_create_object(client: Client) -> None:

    # Given
    url = "/api/movies/"

    # prefer prepare over make to avoid auto saving
    movie_instance: Movie = baker.prepare(Movie)

    # Deserialize to get the JSON version
    payload = MovieSerializer(movie_instance).data

    assert Movie.objects.count() == 0

    # When
    response = client.post(url, payload, content_type="application/json")

    # Then
    assert response.status_code == 201

    assert Movie.objects.count() == 1


@pytest.mark.django_db
def test_post_method_raises_bad_request_on_invalid_payload(client) -> None:

    url = "/api/movies/"
    payload = {}
    content_type = "application/json"

    assert Movie.objects.count() == 0

    response = client.post(url, payload, content_type)

    assert response.status_code == 400

    assert Movie.objects.count() == 0


@pytest.mark.django_db
def test_post_method_for_invalid_payload_keys(client) -> None:
    url = "/api/movies/"
    payload = {"title": "The Big Lebowski", "genre": "comedy"}

    content_type = "application/json"

    assert Movie.objects.count() == 0

    response = client.post(url, payload, content_type)

    assert response.status_code == 400

    assert Movie.objects.count() == 0


@pytest.mark.django_db
def test_fetching_a_single_movie_item(client) -> None:
    # Given
    movie = baker.make(Movie, title="The Big Lebowski", genre="comedy", year="1998")

    assert Movie.objects.filter(id=movie.id).exists()  # Confirm movie exists
    url = f"/api/movies/{movie.id}/"

    # When
    response = client.get(url)

    # Then
    assert response.status_code == 200

    assert response.data["title"] == "The Big Lebowski"
    assert response.data["genre"] == "comedy"


def test_get_single_movie_incorrect_id(client) -> None:
    url = "/api/movies/foo/"
    response = client.get(url)
    assert response.status_code == 404


@pytest.mark.django_db
def test_fetching_all_movies(client) -> None:
    # Given
    baker.make(Movie, _quantity=5)

    url: str = "/api/movies/"

    # When
    response = client.get(url)

    # Then
    assert response.status_code == 200

    assert len(response.data) == 5
