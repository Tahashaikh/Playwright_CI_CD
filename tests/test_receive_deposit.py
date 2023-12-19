import os
import pytest
from playwright.sync_api import Page

from pages.NewLoginPage import NewLoginPage
from pages.login_page import LoginPage
from pages.receive_deposit_page import ReceiveDepositPage
from pages.teller_page import TellerPage
from pages.transaction_security_page import TransactionSecurity
from testdata.data_set2 import TestData as access_data
from pages.logout_page import LogoutPage


# os.environ["SELENIUM_REMOTE_URL"] = "http://10.90.25.64:4444"

# @pytest.mark.parametrize("login_R2BCBS", [{
#     "branch_code": data.Branch_Code,
#     "username": data.Poster,
#     "password": data.Password}], indirect=True)
# def test_ReceiveDeposit_CreditVoucher_CustomerAccount(login_R2BCBS):
#     logout_page = LogoutPage(login_R2BCBS, ReceiveDepositPage)
#     teller_page = TellerPage(login_R2BCBS)
#     #transaction_security = TransactionSecurity(login_R2BCBS)
#     receive_deposit = ReceiveDepositPage(login_R2BCBS)
#
#     teller_page.goto_teller_and_open_batch(data.Password)
#     receive_deposit.receive_deposit_credit_voucher_customer_account(data.Customer_Number,
#                                                                     data.Account_Number,
#                                                                     data.Narration1,
#                                                                     data.Narration2,
#                                                                     data.Narration3)
#     logout_page.logout_R2BCBS()

# @pytest.mark.parametrize("login_R2BCBS", [{
#     "branch_code": data.Branch_Code,
#     "username": data.Authorizer,
#     "password": data.Password}], indirect=True)
# def test_Authorize(login_R2BCBS):
#     logout_page = LogoutPage(login_R2BCBS)
#     transaction_security = TransactionSecurity(login_R2BCBS)
#     transaction_security.transaction_security()
#     #logout_page.logout_R2BCBS()

@pytest.mark.skip("Only Run in R2 Environment")
def test_ReceiveDeposit_CreditVoucher_CustomerAccount(page: Page):
    # reference objects
    login_page = LoginPage(page)
    logout_page = LogoutPage(page)
    teller_page = TellerPage(page)
    receive_deposit = ReceiveDepositPage(page)

    # Steps
    login_page.login_R2BCBS(access_data.Branch_Code, access_data.Poster, access_data.Password)
    teller_page.goto_teller_and_open_batch(access_data.Password)
    receive_deposit.receive_deposit_credit_voucher_customer_account(access_data.Customer_Number,
                                                                    access_data.Account_Number,
                                                                    access_data.Narration1,
                                                                    access_data.Narration2,
                                                                    access_data.Narration3)
    logout_page.logout_R2BCBS()


@pytest.mark.skip("Only Run in R2 Environment")
def test_ReceiveDeposit_CreditVoucher_CustomerAccount_Authorizer(page: Page):
    # reference objects
    login_page = LoginPage(page)
    logout_page = LogoutPage(page)
    transaction_security = TransactionSecurity(page)

    # Steps
    login_page.login_R2BCBS(access_data.Branch_Code, access_data.Authorizer, access_data.Password)
    transaction_security.transaction_security()
    logout_page.logout_R2BCBS()


def test_DemoTest(page: Page):
    newloginpage = NewLoginPage(page)
    newloginpage.goto()
    newloginpage.login_sauce()
    newloginpage.logout_sauce()
