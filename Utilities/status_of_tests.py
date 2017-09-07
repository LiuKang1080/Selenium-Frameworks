"""
@package utilities

CheckPoint class implementation
It provides functionality to assert the result

Example:
    self.check_point.markFinal("Test Name", result, "Message")
"""
from Utilities. custom_logger import custom_logger
import logging
from Base.custom_selenium_driver import CustomSeleniumDriver


class StatusOfTest(CustomSeleniumDriver):

    test_status_logger = custom_logger(logging.DEBUG, log_name='TestStatus')

    def __init__(self, driver):
        """
        Initializes CheckPoint class
        :param driver:
        """
        super(StatusOfTest, self).__init__(driver)
        self.result_list = []

    def set_result(self, result, result_message):
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
        Mark the result of the verification point in a test case
        """
        self.set_result(result, result_message)

    def mark_final(self, test_name, result, result_message):
        """
        Mark the final result of the verification point in a test case
        This needs to be called at least once in a test case
        This should be final test status of the test case
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
