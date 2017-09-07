from Base.custom_selenium_driver import CustomSeleniumDriver
from Utilities.util import Util


class BasePage(CustomSeleniumDriver):

    def __init__(self, driver):
        """
        Initializes the BasePage class.
        :param driver: Instance of the driver.
        """
        super(BasePage, self).__init__(driver)
        self.driver = driver
        self.util = Util()

    def verify_page_title(self, title_of_page):
        """
        Verify the page title.
        :param title_of_page: Title of current page that needs to be verified.
        :return: True or False
        """

        try:
            actual_title = self.get_title()
            return self.util.verify_text_contains(actual_title, title_of_page)
        except Exception as err:
            self.automation_logger.error("Failed to get page title: " + str(err))
