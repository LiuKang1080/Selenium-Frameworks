from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import *
from Utilities.custom_logger import custom_logger
import logging
import time
import os

"""
Use various methods to find, check, and interact with elements. Also provides methods to take screen shots of web pages.
"""


class CustomSeleniumDriver:

    automation_logger = custom_logger(logging.DEBUG)
    # error_logger = custom_logger(logging.DEBUG, 'Error_Logger')

    def __init__(self, driver):
        self.driver = driver

    def get_title(self):
        return self.driver.title

    def get_by_type(self, locator_type):
        """
        Filters elements by attribute type.
        :param locator_type: Type of attribute that element that we want to interact with.
        :return: BY.VALUE attribute or False.
        """
        self.automation_logger.debug('Running Method: get_by_type :')
        locator_type = locator_type.lower()

        if locator_type == 'id':
            return By.ID
        elif locator_type == 'xpath':
            return By.XPATH
        elif locator_type == 'css_selector':
            return By.CSS_SELECTOR
        elif locator_type == 'name':
            return By.NAME
        elif locator_type == 'link_text':
            return By.LINK_TEXT
        elif locator_type == 'classname':
            return By.CLASS_NAME
        else:
            self.automation_logger.error('Locator type not supported! Method get_by_type was called, but could not'
                                         ' initialize BY.TYPE return' + '\n' + '\t' + str(Exception))
            return False

    def get_element(self, locator, locator_type='id'):
        """
        Identify a specific element on a web page.
        :param locator: The value of the attribute.
        :param locator_type: The type of attribute (default = id).
        :return: element: with unique attribute and its value.
        """
        self.automation_logger.debug('Running method: get_element: ')
        element = None

        try:
            locator_type = locator_type.lower()
            by_type = self.get_by_type(locator_type)
            element = self.driver.find_element(by_type, locator)
            self.automation_logger.info("Element was found. ")

        except Exception as err:
            self.automation_logger.error('Element was not found.' + str(err))
        return element

    def get_element_list(self, locator, locator_type="id"):
        """
        Gets a list of elements with the specified BY type.
        :param locator: Locator for the elements on a page.
        :param locator_type: BY type of the locators we want to interact with.
        :return: element - List of elements.
        """
        element = None

        try:
            locator_type = locator_type.lower()
            by_type = self.get_by_type(locator_type)
            element = self.driver.find_elements(by_type, locator)
            self.automation_logger.info("Element list found with locator: " + locator + "and locator_type: " +
                                        locator_type)
        except Exception as err:
            self.automation_logger.error("Element list not found with the provided locator: " + locator +
                                         "and locator_type: " + locator_type)
            self.automation_logger.error(str(err))

        return element

    def element_click(self, locator="", locator_type='id', element=None):
        """
        Click on a specific element.
        -- --
        Either provide the complete element, or the combination of locator and locator_type.
        -- --
        :param locator: Specific locator of an element.
        :param locator_type: BY Type of the element.
        :param element: Complete element object.
        :return: N/A
        """
        try:
            if locator:
                element = self.get_element(locator, locator_type)

            element.click()
            self.automation_logger.info("element_click method was executed, and element was clicked: ")
            self.automation_logger.info("locator: " + locator + "Locator_type: " + locator_type)

        except Exception as err:
            self.automation_logger.error("An Error has occurred: Element could not be clicked. " + locator)
            self.automation_logger.error(str(err))

    def element_send_keys(self, data, locator="", locator_type='id', element=None):
        """
        Send Keys to a specified element.
        -- --
        Either provide the complete element, or the combination of locator and locator_type.
        -- --
        :param data: String of characters that will be sent to element.
        :param locator: Specific locator of an element.
        :param locator_type: BY Type of an element.
        :param element: Complete element object.
        :return: N/A
        """
        try:
            if locator:
                element = self.get_element(locator, locator_type)

            element.send_keys(data)
            self.automation_logger.info("element_send_keys method was called, and successfully sent keys to element")
            self.automation_logger.info("Sent keys to Locator: " + locator + "With Locator_Type: " + locator_type)

        except Exception as err:
            self.automation_logger.error("An Error has occurred: could not send keys to element" + locator)
            self.automation_logger.error(str(err))

    def get_element_text(self, locator="", locator_type="id", element=None):
        """
        Get 'Text' or the "innerText' of an element.
        -- --
        Either provide the complete element, or the combination of locator and locator_type.
        -- --
        :param locator: Specific locator of an element.
        :param locator_type: BY Type of an element.
        :param element: Complete element object.
        :return: text
        """
        try:
            if locator:
                element = self.get_element(locator, locator_type)

            self.automation_logger.info("get_element_text method was called.")
            text = element.text
            self.automation_logger.info("After finding element, the size is: " + str(len(text)))

            if len(text) == 0:
                text = element.get_attribute("innerText")
            if len(text) != 0:
                self.automation_logger.info("The Text on the element is: " + text)
                text = text.strip()

        except Exception as err:
            if element:
                self.automation_logger.error("Failed to get text on element: " + element)
            else:
                self.automation_logger.error("Failed to get text on element with locator: " + locator +
                                             "and locator_type: " + locator_type)

            self.automation_logger.error(str(err))
            text = None

        return text

    def highlight_element(self, element):
        """
        Highlights the specified element on current web page.
        :param element: HTML element on current web page.
        """
        self.driver = element._parent
        # self.driver.execute_script("arguments[0].scrollIntoView(true);", element)

        def apply_style(style):
            self.driver.execute_script("arguments[0].setAttribute('style', arguments[1]);", element, style)

        for i in range(0, 3):
            original_style = element.get_attribute('style')
            apply_style("background: yellow; border: 2px solid red;")
            time.sleep(.5)
            apply_style(original_style)

    def element_check(self, locator="", locator_type='id', element=None):
        """
        Check to see if an element is present on current web page.
        -- --
        Either provide the complete element, or the combination of locator and locator_type.
        -- --
        :param locator: Specific value of element attribute.
        :param locator_type: Attribute BY Type of the element.
        :param element: Complete element object.
        :return: True / False
        """
        self.automation_logger.info("element_check method was called: ")
        try:
            if locator:
                element = self.get_element(locator, locator_type)

            if element:
                self.automation_logger.info("element_check method was successful, element is present: " + str(element))
                return True
            else:
                self.automation_logger.info("Element is not present on current page: " + str(element))
                return False

        except Exception as err:
            self.automation_logger.error('Could not find provided element on current page. ' + str(err))
            return False

    def element_displayed_check(self, locator="", locator_type="id", element=None):
        """
        Check if specific element is currently displayed on page.
        -- --
        Either provide the complete element, or the combination of locator and locator_type.
        -- --
        :param locator: Specific value of element attribute.
        :param locator_type: Attribute BY Type of element
        :param element: Complete element object
        :return: bool(displayed) / False
        """
        displayed = False
        try:
            if locator:
                element = self.get_element(locator, locator_type)

            if element is not None:
                displayed = element.is_displayed()
                self.automation_logger.info("Element is currently displayed with locator: " + locator +
                                            "and locator_type: " + locator_type)
            else:
                self.automation_logger.info("Element is currently NOT displayed: Locator: " + locator + "Locator_Type: "
                                            + locator_type)
            return displayed

        except Exception as err:
            self.automation_logger.error("Specified element was not found: \n \t" + str(err))
            return False

    def take_screen_shot(self, result_message):
        """
        Takes screen shot of current page.
        :param result_message:
        :return:
        """

        file_name = result_message + "." + str(round(time.time() * 1000)) + ".png"
        screenshot_directory = "../Screenshots/"
        current_directory = os.path.dirname(__file__)
        relative_file_path = screenshot_directory + file_name
        destination_file = os.path.join(current_directory, relative_file_path)

        # The files have been generated; Check if screen shot directory exists, if not create it:
        destination_directory = os.path.join(current_directory, screenshot_directory)

        self.automation_logger.info("take_screen_shot method was called: ")
        try:
            if not os.path.exists(destination_directory):
                os.makedirs(destination_directory)

            self.driver.save_screenshot(destination_file)
            self.automation_logger.info("Screen shot file saved to: " + destination_file)
        except Exception as err:
            self.automation_logger.error("An Error has occurred: Could not save screen shot. " + str(err))

    def element_explicit_wait(self, locator, locator_type='id', timeout=10, poll_frequency=0.5):
        element = None

        try:
            by_type = self.get_by_type(locator_type)
            print("Waiting for maximum ::" + str(timeout) +
                  " :: seconds for element to be clickable")

            wait = WebDriverWait(self.driver, timeout=timeout, poll_frequency=poll_frequency,
                                 ignored_exceptions=[NoSuchElementException, ElementNotSelectableException,
                                                     ElementNotVisibleException])

            element = wait.until(EC.element_to_be_clickable((by_type, locator)))
            print("Element appeared on page")

        except Exception as err:
            print("Element not found." + str(err))

        return element

    def scroll_window(self, direction="up"):
        """
        Scroll current window up or down.
        :param direction: Direction of scroll.
        :return: N/A
        """
        if direction == "up":
            self.driver.execute_script("window.scrollBy(0, -1000);")

        if direction == "down":
            self.driver.execute_script("window.scrollBy(0, 1000);")

    def switch_iframes(self, frame_index):
        self.driver.switch_to.frame(frame_index)
