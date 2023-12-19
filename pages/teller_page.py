import re

from pages.base_page import BasePage


class TellerPage(BasePage):
    def __init__(self, page):
        super().__init__(page)
        # Locators
        self._teller_menu_button = "#teller"
        self._batch_menu_button = 'button#batch-btn'
        self._open_batch_button = "a#batch-open"
        self._batch_password = "#PasswordTextBox"
        self._batch_ok_button = "#OkButton"
        self._batch_message = ".el-form-item__content"

    def goto_teller_and_open_batch(self, password: str):
        self.click_on_element(self._teller_menu_button)
        self.click_on_element(self._batch_menu_button)
        self.click_on_element(self._open_batch_button)
        self.type_on_element(self._batch_password, password)
        self.click_on_element(self._batch_ok_button)

        message_element = self.page.wait_for_selector(self._batch_message)
        actual_message = message_element.inner_text()
        expected_pattern = re.compile(r'Batch No\. \d+')
        assert expected_pattern.match(actual_message), \
            f"Expected pattern not found in actual message: {actual_message}"

        self.click_on_element(self._batch_ok_button)

