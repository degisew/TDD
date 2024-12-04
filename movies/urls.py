from typing import Any
from django.urls import path

from movies.views import MovieList

urlpatterns: list[Any] = [
    path("api/movies/", MovieList.as_view(), name="movies")
]
