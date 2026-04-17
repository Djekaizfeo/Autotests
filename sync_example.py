from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser = p.chromium.launch()
    page = browser.new_page()
    page.goto("https://bigtesty.ru")
    page.screenshot(path="screenshots/homepage.png")
    browser.close()