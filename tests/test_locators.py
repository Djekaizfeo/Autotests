import re
from playwright.sync_api import Page, expect

def test_locator_role(page: Page):
    page.goto("https://litres.com/")
    page.get_by_role("link", name="Daily discounts").click()
    expect(page).to_have_title("Best books of 2026 – read online for free or download in fb2")
    page.get_by_role("button", name="Catalog").click()
    expect(page.get_by_text("Parenting", exact=True)).to_be_visible()

def test_locator_placeholder(page: Page):
    page.goto("https://litres.com/")
    page.get_by_placeholder("Find").fill("game of thrones")
    page.keyboard.press("Enter")
    expect(page.get_by_text("Search results «game of thrones»", exact=True)).to_be_visible()

def test_locator_testid(page: Page):
    page.goto("https://litres.com/")
    page.get_by_test_id("dropDown__sorting--wrapper").click()
    expect(page.get_by_text("Русский", exact=True)).to_be_visible()

def test_locator_alttext(page: Page):
    page.goto("https://litres.com/audiobooks/")
    page.get_by_alt_text("Litres logo").click()
    expect(page).to_have_url("https://litres.com/")

def test_locator_xpath(page: Page):
    page.goto("https://litres.com/")
    expect(page.locator("xpath=//a[@href='/pages/litres_oferta/']")).to_be_visible()