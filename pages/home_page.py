import re
from playwright.sync_api import Locator, expect
from pages.base_page import BasePage

class HomePage(BasePage):

    # Locators

    @property
    def search_input(self) -> Locator:

        return self.page.get_by_placeholder("Find")
    
    @property
    def search_button(self) -> Locator:
        
        return self.page.get_by_test_id("search__button")

    # Actions

    def search(self, query: str) -> None:

        self.search_input.fill(query)
        self.search_button.click()