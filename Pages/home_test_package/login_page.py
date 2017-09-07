from selenium.webdriver.common.keys import Keys
from Utilities.custom_logger import custom_logger
from Base.base_page import BasePage
import logging
import time


class LoginPage(BasePage):

    automation_logger = custom_logger(logging.DEBUG)

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # Locators
    _login_field = "Login"
    _email_field = "user_email"
    _password_field = "user_password"
    _login_button_field = "commit"

    # Method Actions on specific elements on current page.
    def click_web_link(self):
        self.element_click(self._login_field, 'link_text')
        self.automation_logger.info("click_web_link method was executed: Using the locator: " +
                                    self._login_field + " and " + "locator_type = link_text")

    def enter_email(self, email):
        self.automation_logger.info("enter_email method from Page Class was called: Locator: " + self._email_field)
        self.element_send_keys(Keys.CLEAR, self._email_field)
        time.sleep(2)
        self.element_send_keys(email, self._email_field)

    def enter_password(self, password):
        self.automation_logger.info("enter_password method was called: Locator: " + self._password_field)
        self.element_send_keys(Keys.CLEAR, self._password_field)
        time.sleep(2)
        self.element_send_keys(password, self._password_field)

    def click_web_button(self):
        self.automation_logger.info("click_web_button method was executed: Locator: " + self._login_button_field +
                                    "locator_type = name")
        self.element_click(self._login_button_field, locator_type='name')

    def verify_login(self):
        result = self.element_check(".//*[@id='navbar']//span[text()='User Settings']", locator_type='xpath')
        return result

    def verify_invalid_login(self):
        result = self.element_check("//div[contains(text(), 'Invalid email or password')]", locator_type='xpath')
        return result

    def verify_title(self):
        return self.verify_page_title("Let's Kode It")

    # Initialize Login Test
    def login(self, username='', password=''):

        self.automation_logger.info("LoginPage class was called, and page 'login' was executed.")

        self.click_web_link()
        self.enter_email(username)
        self.enter_password(password)
        self.click_web_button()
        time.sleep(3)

        self.automation_logger.info("LoginPage class has finished executing.")
        self.automation_logger.debug('\n')
