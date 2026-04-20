import re
from playwright.sync_api import Page, expect
 

def test_main_page_title(page: Page):
    page.goto("https://litres.com/")
    assert page.title() == "Litres is eBooks and audiobooks service, download in FB2 and MP3, read and listen online on Litres"

def test_audiobook_page_title(page: Page):
    page.goto("https://litres.com/")
    page.get_by_role("link", name="Audiobooks").click()
    expect(page).to_have_title("Litres is eBooks and audiobooks service, download in FB2 and MP3, read and listen online on Litres")