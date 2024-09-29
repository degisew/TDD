from django.http import HttpRequest, HttpResponse
from django.template.loader import render_to_string

import pytest

from lists.models import Item
from lists.views import home_page


@pytest.mark.django_db
def test_home_page_can_save_a_POST_request():
    request = HttpRequest()
    request.method = 'POST'
    request.POST['item_text'] = 'A new list item'
    response: HttpResponse = home_page(request)

    new_item = Item.objects.first()
    assert new_item.text == 'A new list item'

    assert 'A new list item' in response.content.decode()

    # expected_html = render_to_string(
    #     'home.html',
    #     {'new_item_text': 'A new list item'}
    # )

    # assert response.content.decode() == expected_html


@pytest.mark.django_db
def test_home_page_only_saves_items_when_necessary():
    request = HttpRequest()
    home_page(request)

    assert Item.objects.count() == 0
