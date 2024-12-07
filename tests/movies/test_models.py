import pytest
from django.forms import ValidationError
from model_bakery import baker

from movies.models import Movie


@pytest.mark.django_db
def test_movie_creation() -> None:
    """Test that a Movie instance can be created and has required fields."""
    movie = baker.make(Movie, year="2023", title="Valid Title")

    assert movie.id is not None
    assert movie.created_date is not None
    assert movie.updated_date is not None
    assert str(movie) == movie.title


@pytest.mark.django_db
def test_movie_year_max_length_validation() -> None:
    """Test that the year field enforces max_length=4."""
    movie = baker.prepare(Movie, year="12345")  # Use prepare to avoid saving

    with pytest.raises(ValidationError) as excinfo:
        movie.full_clean()

    assert "Ensure this value has at most 4 characters" in str(excinfo.value)


@pytest.mark.django_db
def test_movie_title_required() -> None:
    """Test that the title field cannot be empty if required."""
    movie = baker.prepare(Movie, title="")

    with pytest.raises(ValidationError) as excinfo:
        movie.full_clean()

    assert "This field cannot be blank" in str(excinfo.value)
