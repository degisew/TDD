from selenium import webdriver
from selenium.webdriver.common import keys, by

options = webdriver.ChromeOptions()
browser = webdriver.Chrome(options=options)
options.add_argument("--start-maximized")


def test_find_app_title():
    browser.get('http://127.0.0.1:8000')
    assert 'To-Do' in browser.title
    header_text = browser.find_element(by.By.TAG_NAME, "title").get_attribute("textContent")
    assert "To-Do" in header_text

    # She is invited to enter a to-do item straight away
    input_box = browser.find_element(by.By.ID, 'id_new_item')
    assert input_box.get_attribute('placeholder') == 'Enter a to-do item'
    # She types "Buy peacock feathers" into a text box (Edith's hobby
    # is tying fly-fishing lures)
    input_box.send_keys('Buy peacock feathers')

    # When she hits enter, the page updates, and now the page lists
    # "1: Buy peacock feathers" as an item in a to-do list table
    input_box.send_keys(keys.Keys.ENTER)
    table = browser.find_element(by.By.ID, 'id_list_table')
    rows = table.find_elements(by.By.TAG_NAME, 'tr')
    assert any(row.text == '1: Buy peacock feathers' for row in rows)
