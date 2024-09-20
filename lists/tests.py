from django.http import HttpRequest
from django.urls import resolve
from django.test import TestCase
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