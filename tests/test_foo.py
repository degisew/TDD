from django.urls import reverse, resolve
import json


def test_ping(client) -> None:
    # Given
    # client fixture is given

    # when
    url = reverse("ping")
    response = client.get(url)
    content = json.loads(response.content)

    # then
    assert response.status_code == 200
    assert content["ping"] == "pong!"
