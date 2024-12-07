from rest_framework.generics import get_object_or_404
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.status import HTTP_201_CREATED, HTTP_400_BAD_REQUEST
from rest_framework.views import APIView

from movies.models import Movie
from movies.serializers import MovieSerializer


class MovieList(APIView):
    """A DRF view for listing and creating movies.

    This view handles the retrieval of all movies and the creation of new movie records.

    Methods:
        GET: Retrieve a list of all movies.
        POST: Create a new movie record.

    Returns:
        Response: A Response object containing the serialized movie data or validation errors.
    """

    def get(self, request: Request) -> Response:
        """Retrieve a list of all movies.

        Args:
            request (Request): The HTTP request object.

        Returns:
            Response: A Response object containing the list of serialized movie data.
        """
        movies = Movie.objects.all()
        serializer = MovieSerializer(movies, many=True)

        return Response(serializer.data)

    def post(self, request: Request, format=None):
        """Create a new movie record.

        Args:
            request (Request): The HTTP request object containing the movie data.

        Returns:
            Response: A Response object containing the serialized movie data on success,
            or validation errors on failure.
        """
        serializer = MovieSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=HTTP_201_CREATED)
        return Response(serializer.errors, status=HTTP_400_BAD_REQUEST)
