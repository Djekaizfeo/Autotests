import re
from playwright.sync_api import Page, expect

def test_locator_role(page: Page):
    page.goto("https://litres.com/")
    page.get_by_role("link", name="Daily discounts").click()
    expect(page).to_have_title("Best books of 2026 – read online for free or download in fb2")
    page.get_by_role("button", name="Catalog").click()
    expect(page.get_by_text("Parenting", exact=True)).to_be_visible()