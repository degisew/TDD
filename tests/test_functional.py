from selenium import webdriver


browser = webdriver.Chrome()


def test_find_app_title():
    browser.get('http://127.0.0.1:8000')
    assert 'install' in browser.title
