import re

from playwright.sync_api import Page, expect



def test_1example(page: Page) -> None:
    page.wait_for_timeout(3000)
    page.goto("https://www.saucedemo.com/")
    expect(page).to_have_title(re.compile("Swag Labs"))

def test_2example(page: Page) -> None:
    page.wait_for_timeout(3000)
    page.goto("https://www.saucedemo.com/")
    expect(page).to_have_title(re.compile("Swag Labs"))








