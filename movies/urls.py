from typing import Any
from django.urls import path

from movies.views import MovieDetail, MovieList

urlpatterns: list[Any] = [
    path("api/movies/", MovieList.as_view(), name="movies"),
    path("api/movies/<int:pk>/", MovieDetail.as_view(), name="movie-detail")
]
