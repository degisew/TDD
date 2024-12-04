import pytest
from model_bakery import baker
from movies.models import Movie


@pytest.mark.django_db
def test_post_method_create_object(client) -> None:

    # Given
    url = "/api/movies/"
    # payload = baker.prepare(Movie)
    payload = {
            "title": "The Big Lebowski",
            "genre": "comedy",
            "year": "1998",
        }
    print(payload)

    instance_count = Movie.objects.count()

    assert instance_count == 0

    # When
    response = client.post(url, payload, content_type="application/json")

    # Then
    assert response.status_code == 201

    assert Movie.objects.count() == 1
