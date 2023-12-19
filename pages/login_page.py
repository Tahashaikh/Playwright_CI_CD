from pages.base_page import BasePage
from testdata.data_set2 import TestData


class LoginPage(BasePage):
    def __init__(self, page):
        super().__init__(page)

        # Locators
        self._branch_code = "#brncd"
        self._user_name = "#usernamebox"
        self._pass_word = "#passwordbox"
        self._login_button = "#login"
        self._modal_message = '.el-message-box__message'
        self._ok_popup_button = "//span[normalize-space()='OK']"

    def goto(self, url):
        self.visit(url)

    def login_R2BCBS(self, branch_code:str, username:str, password:str):
        self.goto('/')
        self.type_on_element(self._branch_code, branch_code)
        if username == TestData.Poster:
            self.type_on_element(self._user_name, username)
        elif username == TestData.Authorizer:
            self.type_on_element(self._user_name, username)
        self.type_on_element(self._pass_word, password)
        self.click_on_element(self._login_button)
        self.get_text_and_click(self._modal_message,self._ok_popup_button,"Sign-on is Successful")
        self.print_message("Login Successfully")
        self.attach_screenshot_to_allure("Login Successfully")
