from django.http import HttpRequest, HttpResponse
from django.urls import resolve
from django.template.loader import render_to_string
from lists.views import home_page


def test_root_url_resolves_to_home_page_view():
    found = resolve('/')
    assert found.func == home_page

# def test_home_page_returns_correct_html():
#     request = HttpRequest()
#     response = home_page(request)
#     self.assertTrue(response.content.startswith(b'<html>'))
#     self.assertIn(b'<title>To-Do lists</title>', response.content)
#     self.assertTrue(response.content.endswith(b'</html>'))


def test_home_page_returns_correct_html():
    request = HttpRequest()
    response = home_page(request)

    assert response.content.startswith(b'<html>')
    assert b'<title>To-Do lists</title>' in response.content
    assert response.content.endswith(b'</html>')
    expected_html = render_to_string(
        'home.html',
        {'new_item_text': 'A new list item'}
        )
    assert response.content.decode() == expected_html


def test_home_page_can_save_a_POST_request():
    request = HttpRequest()
    request.method = 'POST'
    request.POST['item_text'] = 'A new list item'
    response: HttpResponse = home_page(request)
    assert 'A new list item' in response.content.decode()
