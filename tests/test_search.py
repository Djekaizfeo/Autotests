import re
from playwright.sync_api import Page, expect

def test_main_actions(page: Page):
    page.locator("button:has-text('I agree')").click()
    page.get_by_test_id("search__input").fill("python")
    page.keyboard.press("Enter")
    expect(page).to_have_url("https://litres.com/search/?q=python")
    page.locator("xpath=//*[@aria-labelledby='labelFor-only_high_rated']").click()
    page.locator("xpath=//*[@for='languages-ru']").check()
    page.pause()

def test_waiting(page: Page):
    page.get_by_placeholder("Find").fill("python")
    page.get_by_test_id("search__button").click()

    expect(page.get_by_text("Search results «python»")).to_be_visible()
    expect(page).to_have_title("Search results for books: «python»")
    
    # expect(page.get_by_text("TestError"), "Show log message for test error demo").to_be_visible()

    result_title = page.locator("text=Search results «python»")
    result_title.wait_for(timeout=7000)

    books = page.get_by_test_id("art__wrapper")
    expect(books).to_have_count(24, timeout=10000)