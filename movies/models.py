from django.contrib.auth.models import AbstractUser
from django.db import models


class CustomUser(AbstractUser):
    """Custom user model to extend the default Django user model

    Args:
        AbstractUser (_type_): Base class for User model
    """

    pass


class Movie(models.Model):
    """A model representing a movie.

    Args:
        models (type): The base class for all Django models.
    """

    title = models.CharField(max_length=255)
    genre = models.CharField(max_length=255)
    year = models.CharField(max_length=4)
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return f"{self.title}"
