from datetime import datetime
import pandas
import allure
from playwright.sync_api import Page


def get_data_from_file(file_path, sheet_name='Sheet1'):

    if file_path.endswith('.csv'):
        df = pandas.read_csv(file_path)
    elif file_path.endswith(('.xls', '.xlsx')):
        df = pandas.read_excel(file_path, sheet_name)
    else:
        raise ValueError("Unsupported file format. Please provide a CSV or Excel file.")
    return df


class BasePage:
    global_variables = {}

    def __init__(self, page: Page):
        self.page = page

    def visit(self, url, time=0):
        self.page.goto(url)
        self.page.wait_for_timeout(time)

    def click_on_element(self, selector, time=0):
        try:
            element = self.page.wait_for_selector(selector)
            element.click()
            self.page.wait_for_timeout(time)
        except Exception as exp:
            selectors_list = [selector]
            self.print_error_message(selectors_list, exp,
                                     custom_message=f"Error clicking element {selectors_list}: {exp}")

    def type_on_element(self, selector: str, text, time=0):
        try:
            element = self.page.wait_for_selector(selector)
            element.click()
            element.type(text)
            self.page.wait_for_timeout(time)
        except Exception as exp:
            selectors_list = [selector]
            self.print_error_message(selectors_list, exp,
                                     custom_message=f"Error typing on element {selectors_list}: {exp}")

    def get_text_and_click(self, selector1: str, selector2: str, expected_text: str, time=0):
        try:
            modal_message = self.page.locator(selector1).text_content()
            self.print_message(f"Message: {modal_message}", color="yellow")
            if expected_text in modal_message:
                self.click_on_element(selector2)
            self.page.wait_for_timeout(time)
        except Exception as exp:
            selectors_list = [selector1, selector2]
            self.print_error_message(selectors_list, exp,
                                     custom_message=f"Error clicking on element {selectors_list} : {exp}")

    def set_global_variable(self, **values):
        try:
            self.global_variables.update(values)
        except Exception as exp:
            selectors_list = None
            self.print_error_message(selectors_list, exp,
                                     custom_message=f"Error setting up global variable in dictionary: {exp}")

    def use_global_variable(self, key):
        if key in self.global_variables:
            return self.global_variables[key]
        else:
            selectors_list = None
            self.print_error_message(selectors_list, key,
                                     custom_message=f"Key {key} not found in global variables in dictionary")

    def show_all_global_variables(self):
        self.print_message("Global Variables: ")
        for key, value in self.global_variables.items():
            self.print_message("green", key, value)

    def show_dictionary(self):
        print("\n")
        keys = self.global_variables.keys()
        self.print_message(keys,"red")

        values = self.global_variables.values()
        self.print_message(values, "red")

        items = self.global_variables.items()
        self.print_message(items, "red")

    def print_error_message(self, selectors, e, custom_message=None):
        self.page.wait_for_timeout(1)
        if custom_message is not None:
            error_message = custom_message
        else:
            selector_string = ', '.join(map(str, selectors))
            error_message = "Error Message {}: {}".format(selector_string, e)

        formatted_error = "\033[1;31m{}\033[0m".format(error_message)
        print(formatted_error)

    def print_message(self, *texts, color="green"):
        self.page.wait_for_timeout(1)
        color_code = {"red": "31", "yellow": "33", "green": "32"}

        if color not in color_code:
            raise ValueError("Invalid color. Supported colors: red, yellow, green")

        formatted_texts = [f"\033[1;{color_code[color]}m{text}\033[0m" for text in texts]
        formatted_message = ' '.join(formatted_texts)
        print(formatted_message)

    def clear_all_values(self):
        self.global_variables.clear()

    def closePage(self):
        self.page.close()

    def attach_screenshot_to_allure(self, step_name: str = "Screenshot"):
        with allure.step(step_name):
            timestamp = datetime.now().strftime("%Y%m%d%H%M%S")
            screenshot_path = f"reports/screenshots/{step_name.replace(' ', '_').lower()}_{timestamp}.png"
            self.page.screenshot(path=screenshot_path)
            allure.attach.file(screenshot_path, attachment_type=allure.attachment_type.PNG)

    def attach_video_to_allure(self, step_name: str = "Complete Test Case Video"):
        with allure.step(step_name):
            allure.attach.file(self.page.video.path(), attachment_type=allure.attachment_type.WEBM)

