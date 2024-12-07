from movies.serializers import MovieSerializer


def test_valid_data_deserialization() -> None:
    valid_payload = {"title": "Yewendoch Guday", "genre": "comedy", "year": "1999"}
    serializer = MovieSerializer(data=valid_payload)
    assert serializer.is_valid()
    assert serializer.validated_data == valid_payload
    assert serializer.data == valid_payload
    assert serializer.errors == {}


def test_invalid_data_deserialization() -> None:
    invalid_payload = {"title": "Fikir Siferd", "genre": "romantic"}

    serializer = MovieSerializer(data=invalid_payload)
    assert not serializer.is_valid()
    assert serializer.validated_data == {}
    assert serializer.data == invalid_payload
    assert serializer.errors == {"year": ["This field is required."]}
