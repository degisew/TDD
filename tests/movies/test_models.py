import pytest
from model_bakery import baker
from movies.models import Movie  # Replace `myapp` with the actual app name


@pytest.mark.django_db
def test_movie_model():
    movie = baker.make(Movie)

    assert movie.id is not None 

    assert movie.created_date
    assert movie.updated_date
    # Test the __str__ method
    assert str(movie) == movie.title
