import re, pytest
from playwright.sync_api import Page, expect
from pages.home_page import HomePage

@pytest.fixture(autouse=True)
def open_litres(page: Page):
    page.goto("https://litres.com/")

@pytest.fixture
def home(page: Page) -> HomePage:
    return HomePage(page) 