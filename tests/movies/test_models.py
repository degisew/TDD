import pytest
from model_bakery import baker
from movies.models import Movie  # Replace `myapp` with the actual app name


@pytest.mark.django_db
def test_movie_model():
    instance = baker.make(Movie)

    assert instance.id is not None 

    # Test the __str__ method
    assert str(instance) == instance.title
