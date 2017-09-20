from selenium.common.exceptions import WebDriverException
from Utilities.custom_logger import custom_logger
from Base.base_page import BasePage
import logging
import time


class RegisterCourses(BasePage):

    register_course_logger = custom_logger(logging.DEBUG)

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # LOCATORS: By default locators are "id". Otherwise they are specified above the specific locator.

    _search_field = "search-courses"
    _search_button = "search-course-button"
    # XPATH:
    _course_field = "//div[contains(@class,'course-listing') and contains(text(),'{0}')]"
    _enroll_button = "enroll-button-top"

    iframe_xpath = "//input[@class='StripeField--fake']"

    # XPATH EMBEDDED WITHIN IFRAME=0
    _credit_card_field = iframe_xpath
    # XPATH EMBEDDED WITHIN IFRAME=1
    _expiration_field = iframe_xpath
    # XPATH EMBEDDED WITHIN IFRAME=2
    _cvc_field = iframe_xpath
    # XPATH EMBEDDED WITHIN IFRAME=3
    _zip_field = iframe_xpath
    _confirm_enroll_button = "confirm-purchase"

    ##
    # Method actions on specific elements for test.
    ##

    def search_for_course(self, course_name_to_search, full_course_name):
        self.register_course_logger.info("\n" + "enroll_in_course method was called from Page Class")

        self.element_send_keys(course_name_to_search, self._search_field)
        time.sleep(2)
        self.register_course_logger.info("send_keys method from was called: Locator: "
                                         + self._search_field)

        self.element_click(self._search_button)
        time.sleep(2)
        self.register_course_logger.info("element_click method from was called. Locator: "
                                         + self._search_button)

        self.element_click(self._course_field.format(full_course_name), locator_type='xpath')
        time.sleep(2)
        self.register_course_logger.info("element_click method from was called. Locator: "
                                         + self._course_field)

        self.element_click(self._enroll_button)
        time.sleep(2)
        self.register_course_logger.info("element_click method was called. Locator: "
                                         + self._enroll_button)

    def enter_credit_info(self, credit_num, exp_date, cvc_num, zip_num):
        self.register_course_logger.info("\n" + "enter_credit_info method from Page Class was called.")

        self.scroll_window("down")
        self.register_course_logger.info("enter_credit_info method was called from Page Class: " + "\n")

        try:
            self.switch_iframes(0)
            element_list = self.get_element_list(self._credit_card_field, locator_type='xpath')
            self.element_send_keys(credit_num, element=element_list[0])
            self.register_course_logger.info("Entering credit card info: Locator: " + self._credit_card_field)
            time.sleep(1)
        except Exception as err:
            self.register_course_logger.error("Could not switch to the Frame: Frame(0)" + '\n' + str(err))

        try:
            self.switch_iframes(1)
            element_list = self.get_element_list(self._expiration_field, locator_type='xpath')
            self.element_send_keys(exp_date, element=element_list[0])
            self.register_course_logger.info("Entering expiration date: Locator: " + self._expiration_field)
            time.sleep(1)
        except Exception as err:
            self.register_course_logger.error("Could not switch to the Frame: Frame(1)" + '\n' + str(err))

        try:
            self.switch_iframes(2)
            element_list = self.get_element_list(self._cvc_field, locator_type='xpath')
            self.element_send_keys(cvc_num, element=element_list[0])
            self.register_course_logger.info("Entering CVC number: Locator: " + self._cvc_field)
            time.sleep(1)
        except Exception as err:
            self.register_course_logger.error("Could not switch to the Frame: Frame(2)" + '\n' + str(err))

        try:
            self.switch_iframes(3)
            element_list = self.get_element_list(self._zip_field, locator_type='xpath')
            self.element_send_keys(zip_num, element=element_list[0])
            self.register_course_logger.info("Entering zip code: Locator: " + self._zip_field)
        except Exception as err:
            self.register_course_logger.error("Could not switch to the Frame: Frame(3)" + '\n' + str(err))

    def verify_enroll_fail(self):
        """
        Verification should be a negative test. Enroll in course button should not be intractable.
        :return: True / False
        """
        self.take_screen_shot("Verification of register course: ")

        try:
            self.element_click(self._confirm_enroll_button)
            result = False
            self.register_course_logger.error("Confirm button was clicked! ##")
        except WebDriverException:
            # We want this element to not be intractable during this test.
            self.register_course_logger.info("Confirm button was not clicked.")
            result = True

        return result

    def enroll_in_course(self, course_title, full_course_name, credit_num, exp_date, cvc_num, zip_num):
        self.register_course_logger.info("RegisterCourses class was called, and Page "
                                         "'register_courses_page' was executed.")

        self.search_for_course(course_title, full_course_name)
        self.enter_credit_info(credit_num, exp_date, cvc_num, zip_num)
        time.sleep(2)

        self.register_course_logger.info("RegisterCourses class has finished executing.")
        self.register_course_logger.debug('\n')
