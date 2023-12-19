import random
from pages.base_page import BasePage


class ReceiveDepositPage(BasePage):
    def __init__(self, page):
        super().__init__(page)

        # Locators
        self._receive_deposit_menu_button = "#receive-deposit"
        self._receive_deposit_credit_voucher_button = "//a[normalize-space()='Credit Voucher']"
        self._receive_deposit_customer_account_button = "#PYCCVS10"
        self._receive_deposit_customer_number_textbox = "#CustomerNumberTextBox"
        self._receive_deposit_customer_account_number_dropdown = "#AccountNumberDropDown"
        self._receive_deposit_ok_button = "#OkButton"
        self._receive_deposit_amount_textbox = "#AmountTextBox"
        self._receive_deposit_document_number_textbox = "#DocumentNumberTextBox"
        self._receive_deposit_narration1_textbox = "#NarrationTextBox"
        self._receive_deposit_narration2_textbox = "#NoLabelNarration2TextBox"
        self._receive_deposit_narration3_textbox = "#NoLabelNarration3TextBox"
        self._receive_deposit_narration3_textbox = "#NoLabelNarration3TextBox"
        self._receive_deposit_purpose_dropdown = "#PurposeDropDown-GenericDropDown"
        self._receive_deposit_purpose_education = "//span[normalize-space()='EDUCATION']"
        self._receive_deposit_receive_cash_print_receipt_button = "#ReceiveCashPrintReceiptButton"
        self._receive_deposit_modal_message = '.el-message-box__message'
        self._receive_deposit_modal_ok_button = "button[class='el-button el-button--primary']"
        self._receive_deposit_continue_button = "#ContButton"
        self._receive_deposit_voucher_number = '.el-form-item__content'
        self._receive_deposit_slip_print_ok_button = ("//div[@class='el-col el-col-24 el-col-md-4 el-col-lg-4']"
                                                      "//div//button[@id='OkButton']")
        self._receive_deposit_exit_button = '#ExitButton'
        self._main_menu_button = '#main-menu'

    def receive_deposit_credit_voucher_customer_account(self,
                                                        customer_number: str,
                                                        account_number: str,
                                                        narration1: str,
                                                        narration2: str,
                                                        narration3: str):
        self.click_on_element(self._receive_deposit_menu_button)
        self.click_on_element(self._receive_deposit_credit_voucher_button)
        self.click_on_element(self._receive_deposit_customer_account_button)
        self.type_on_element(self._receive_deposit_customer_number_textbox, customer_number)
        self.click_on_element(self._receive_deposit_customer_account_number_dropdown)

        element = "//span[normalize-space()='" + account_number + "']"
        self.click_on_element(element)

        self.click_on_element(self._receive_deposit_ok_button)

        expected_text = ("Unauthorized financial transaction(s) exist for the selectd "
                         "account Do you want to continue?")
        if self.page.wait_for_selector(self._receive_deposit_modal_ok_button).is_visible():
            assert self.page.wait_for_selector(self._receive_deposit_modal_message).inner_text() == expected_text, \
                f"Text does not match {expected_text}"

        self.click_on_element(self._receive_deposit_modal_ok_button)
        self.type_on_element(self._receive_deposit_amount_textbox, str(random.randint(50001, 100000)))
        self.type_on_element(self._receive_deposit_document_number_textbox, str(random.randint(10, 100)))

        self.type_on_element(self._receive_deposit_narration1_textbox, narration1)
        self.type_on_element(self._receive_deposit_narration2_textbox, narration2)
        self.type_on_element(self._receive_deposit_narration3_textbox, narration3)
        self.click_on_element(self._receive_deposit_purpose_dropdown)
        self.click_on_element(self._receive_deposit_purpose_education)
        self.click_on_element(self._receive_deposit_receive_cash_print_receipt_button)
        self.get_text_and_click(self._receive_deposit_modal_message,
                                self._receive_deposit_modal_ok_button,
                                "Please Check  whether the Deposit Slip ")
        self.click_on_element(self._receive_deposit_continue_button)
        self.click_on_element(self._receive_deposit_ok_button)
        #########################################################################################################
        partial_text = "Voucher No:"
        xpath_dynamic = f"//div[@class='el-form-item__content'][contains(normalize-space(), '{partial_text}')]"
        element = self.page.locator(xpath_dynamic)
        extracted_text = element.inner_text()
        voucher_number = extracted_text.split(":")[1].strip()
        print("\033[1;33m{}\033[0m".format("Message: " + voucher_number))
        #########################################################################################################
        self.set_global_variable(voucher_1=voucher_number)
        self.show_all_global_variables()
        #########################################################################################################
        self.click_on_element(self._receive_deposit_ok_button)
        self.click_on_element(self._receive_deposit_slip_print_ok_button)
        self.get_text_and_click(self._receive_deposit_modal_message,
                                self._receive_deposit_modal_ok_button,
                                "Receive Cash Transaction Completed!")
        self.click_on_element(self._receive_deposit_exit_button)
        self.click_on_element(self._main_menu_button)
#########################################################################################################


# expect(page.get_by_text("Voucher No: 3004999/")).to_be_visible()
# expect(page.locator("form")).to_contain_text("Voucher No: 3004999/2023")
# self.get_text_and_click(self._modal_message, self._ok_button, "Are You Sure, You Want To Sign Off!")
# print("\033[1;32;40mLogout Successful\033[0m")
