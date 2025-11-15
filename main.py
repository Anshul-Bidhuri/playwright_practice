from playwright.sync_api import sync_playwright
import time

with sync_playwright() as p:
    browser = p.firefox.launch(headless=False)
    page = browser.new_page().add_init_script
    page.goto("https://playwright.dev/python/docs/intro")
    time.sleep(5)
print(2344)

print(123456456456)