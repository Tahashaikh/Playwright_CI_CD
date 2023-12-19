from pages.base_page import BasePage


class LogoutPage(BasePage):
    def __init__(self, page):
        super().__init__(page)

        # Locators
        self._logout_button = "#sign-off"
        self._modal_message = '.el-message-box__message'
        self._ok_button = "//span[normalize-space()='OK']"

    def logout_R2BCBS(self):
        self.click_on_element(self._logout_button)
        self.get_text_and_click(self._modal_message, self._ok_button, "Are You Sure, You Want To Sign Off!")
        self.print_message("Logout Successful")
        self.attach_video_to_allure()


