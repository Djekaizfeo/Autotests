import re, pytest
from playwright.sync_api import Page, expect

#We can unmark this fixture and it will be used in every file in this folder
# @pytest.fixture(autouse=True)
# def open_litres(page: Page):
#     page.goto("https://litres.com/")