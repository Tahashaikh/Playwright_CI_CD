from playwright.sync_api import Page

from pages.base_page import BasePage


class NewLoginPage(BasePage):
    def __init__(self, page):
        super().__init__(page)

    def goto(self):
        self.visit("/")
        self.attach_screenshot_to_allure("Launch Sucessfully")

    def login_sauce(self):
        self.page.wait_for_selector("[data-test=\"username\"]").click()
        self.page.locator("[data-test=\"username\"]").fill("standard_user")
        self.page.locator("[data-test=\"username\"]").press("Tab")
        self.page.locator("[data-test=\"password\"]").fill("secret_sauce")
        self.page.locator("[data-test=\"login-button\"]").click()
        self.attach_screenshot_to_allure("Login Successfully")

    def logout_sauce(self):
        self.page.get_by_role("button", name="Open Menu").click()
        self.page.get_by_role("link", name="Logout").click()
        self.attach_screenshot_to_allure("Logout Successfully")
        self.attach_video_to_allure()
