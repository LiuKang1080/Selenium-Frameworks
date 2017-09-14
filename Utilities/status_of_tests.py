"""
Package: Utilities

Check point class implementation.
Provides functionality to assert single or multiple assert statements.

Example: self.check_point.mark_final("test_name", result, "message")
"""

from Utilities. custom_logger import custom_logger
import logging
from Base.custom_selenium_driver import CustomSeleniumDriver


class StatusOfTest(CustomSeleniumDriver):

    test_status_logger = custom_logger(logging.DEBUG, log_name='TestStatus')

    def __init__(self, driver):
        """
        Initializes Check point class.
        :param driver: Pass current instance of driver.
        """
        super(StatusOfTest, self).__init__(driver)
        self.result_list = []

    def set_result(self, result, result_message):
        """
        Add result to result_list for each verification point in Test Case.
        :param result: Result of verification.
        :param result_message: Specific optional message: Preferred: Name of Test Case.
        :return: N/A Each result is logged into specified log.
        """
        try:
            if result is not None:
                if result:
                    self.result_list.append("PASS")
                    self.test_status_logger.info("### VERIFICATION SUCCESSFUL :: + " + result_message)
                else:
                    self.result_list.append("FAIL")
                    self.test_status_logger.error("### VERIFICATION FAILED :: + " + result_message)
                    self.take_screen_shot(result_message)
            else:
                self.result_list.append("FAIL")
                self.test_status_logger.error("### VERIFICATION FAILED :: + " + result_message)
                self.take_screen_shot(result_message)
        except Exception as err:
            self.result_list.append("FAIL")
            self.test_status_logger.error("### An Exception has occurred! " + str(err))
            self.take_screen_shot(result_message)

    def mark(self, result, result_message):
        """
        Mark the result of the verification point in a Test Case.
        :param result: Result of verification.
        :param result_message: Specific optional message: Preferred: Name of Test Case.
        :return: N/A
        """

        self.set_result(result, result_message)

    def mark_final(self, test_name, result, result_message):
        """
        Mark the final result of the verification point in a Test Case.
        mark_final needs to be called at least once in a Test Case. Preferably
        mark_final method should be the final test status of the Test Case
        """
        self.set_result(result, result_message)

        if "FAIL" in self.result_list:
            self.test_status_logger.error(test_name + " ### TEST FAILED")
            self.result_list.clear()
            assert True == False
            self.test_status_logger.debug("\n")
        else:
            self.test_status_logger.info(test_name + " ### TEST SUCCESSFUL")
            self.result_list.clear()
            assert True == True
            self.test_status_logger.debug("\n")
