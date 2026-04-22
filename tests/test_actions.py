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