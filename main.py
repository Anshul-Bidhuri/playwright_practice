from playwright.sync_api import sync_playwright
import time
from datetime import datetime

# with sync_playwright() as p:
#     browser = p.firefox.launch(headless=False)
#     page = browser.new_page()
#     page.goto("https://playwright.dev/python/docs/intro")
#     time.sleep(5)
# print(2344)

def get_current_datetime():
    return datetime.now()

print(get_current_datetime())