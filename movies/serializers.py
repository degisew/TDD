from rest_framework import serializers

from movies.models import Movie


class MovieSerializer(serializers.ModelSerializer):
    """A serializer class for the Movie model.

    This serializer is used to convert Movie model instances into
    JSON data and validate incoming data for creating or updating
    movies.

    Args:
        serializers (ModelSerializer): The base serializer class from
        Django REST Framework, which this class inherits from.
    """

    class Meta:
        model = Movie
        fields = "__all__"
        read_only_fields = (
            "id",
            "created_date",
            "updated_date",
        )
