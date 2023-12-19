import re
from pages.base_page import BasePage
from pages.receive_deposit_page import ReceiveDepositPage


class TransactionSecurity(BasePage):
    def __init__(self, page):
        super().__init__(page)
        # Locators
        self._transaction_security_menu_button = "#transaction-security"
        self._authorize_button = 'button[class="el-button moduleBtn"]>span'
        self._by_voucher_list_button = "//a[normalize-space()='By Voucher List']"
        self._normal_button = "//a[normalize-space()='Normal']"
        self._user_id_dropdown = "#UserIdDropDown"
        self._user_voucher_type_dropdown = "#VoucherTypeDropDown-GenericDropDown"
        self._transaction_security_ok_button = "#OkButton"
        self._transaction_security_exceptions_button = "#ExceptionsButton"
        self._transaction_security_authorize_button = "#AuthorizeButton"
        self._transaction_security_back_button = "#BackButton"
        self._main_menu_button = "#main-menu"

    def transaction_security(self):
        self.click_on_element(self._transaction_security_menu_button)
        self.page.locator(self._authorize_button).get_by_text("Authorize").click()
        container_locator = self.page.locator("#container")
        container_locator.get_by_text("By Voucher List").hover()
        container_locator.get_by_text("Normal").click()

        element = self.page.locator(self._user_id_dropdown)
        element.click()
        element.type("VDQATST1")
        element.press("Enter")

        element = self.page.locator(self._user_voucher_type_dropdown)
        element.click()
        element.type("All")
        element.press("Enter")
        self.click_on_element(self._transaction_security_ok_button)
########################################################################################################

        voucher_number = self.use_global_variable('voucher_1')
        print(f"This voucher number is being used: {voucher_number}")

        element = self.page.locator("//td[text()='" + voucher_number + "']/preceding-sibling::td/div")
        element.click()

########################################################################################################
        self.click_on_element(self._transaction_security_ok_button)
        self.click_on_element(self._transaction_security_exceptions_button)
        self.click_on_element(self._transaction_security_authorize_button)
        self.click_on_element(self._transaction_security_ok_button)
        self.click_on_element(self._transaction_security_back_button)
        self.click_on_element(self._transaction_security_back_button)
        self.click_on_element(self._main_menu_button)




