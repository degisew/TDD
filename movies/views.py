from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.request import Request
from movies.serializers import MovieSerializer
from rest_framework.status import (
    HTTP_201_CREATED,
    HTTP_400_BAD_REQUEST
)


class MovieList(APIView):
    """A Rest framework view for CRUD operation on the movies

    Returns:
        Response object
    """
    def post(self, request: Request, format=None):
        serializer = MovieSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=HTTP_201_CREATED)
        return Response(serializer.errors, status=HTTP_400_BAD_REQUEST)
