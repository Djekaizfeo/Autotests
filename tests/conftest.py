import re, pytest
from playwright.sync_api import Page, expect

@pytest.fixture(autouse=True)
def open_litres(page: Page):
    page.goto("https://litres.com/")