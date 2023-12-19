import pytest
from playwright.sync_api import Page


@pytest.fixture(scope="function")
def login_R2BCBS(page: Page, request):
    print("\n\033[1;32;40mLogin Successful\033[0m")
    # Selectors
    element_branch_code = "//input[@id='brncd']"
    element_username = "#usernamebox"
    element_password = "#passwordbox"
    element_login_button = "#login"
    element_modal_message = '.el-message-box__message'
    element_ok_popup_button = "//span[normalize-space()='OK']"

    branch_code = request.param.get("branch_code")
    username = request.param.get("username")
    password = request.param.get("password")

    page.goto("/")
    page.click(element_branch_code)
    page.fill(element_branch_code, branch_code)

    page.click(element_username)
    page.fill(element_username, username)

    page.click(element_password)
    page.fill(element_password, password)

    page.click(element_login_button)

    modal_message = page.locator(element_modal_message).text_content()
    print("\033[1;33m{}\033[0m".format("Message: " + modal_message))
    if "Sign-on is Successful" in modal_message:
        page.click(element_ok_popup_button)

    return page
