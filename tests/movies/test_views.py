from django.test import Client
import pytest
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
