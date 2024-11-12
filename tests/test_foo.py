from django.urls import reverse, resolve
import json
def test_ping(client) -> None:
    url = reverse("ping")
    print(resolve(url))

    response = client.get(url)
    content = json.loads(response.content)

    assert response.status_code == 200

    assert content["ping"] == "pong!"
