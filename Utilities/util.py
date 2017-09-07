import time
import random
import string
from Utilities.custom_logger import custom_logger
import logging


class Util(object):

    automation_logger = custom_logger(logging.DEBUG)

    def sleep(self, sec, info=""):
        """
        Set the program to wait explicitly for the specified amount of time.
        :param sec: Number of Seconds to wait
        :param info: Optional text.
        :return: None
        """
        if info is not None:
            self.automation_logger.info("Wait:: " + str(sec) + "second for " + info)
        try:
            time.sleep(sec)
        except Exception as err:
            self.automation_logger.error("An error has occurred: time.sleep() was interrupted: " + str(err))

    def get_alpha_numeric(self, length, type_of_data='letters'):
        """
        Get random string of characters
        :param length: Number of characters the string should contain.
        :param type_of_data: Type of characters the string should contain, default = letters.
        :return: Returns the alpha-numeric string
        """
        alpha_num = ''
        if type_of_data == 'lower':
            case = string.ascii_lowercase
        elif type_of_data == 'upper':
            case = string.ascii_uppercase
        elif type_of_data == 'digits':
            case = string.digits
        elif type_of_data == 'mix':
            case = string.ascii_letters + string.digits
        else:
            case = string.ascii_letters
        return alpha_num.join(random.choice(case) for i in range(length))

    def get_unique_name(self, character_count=10):
        """
        Get a unique name.
        :param character_count: length of the character.
        :return: Unique name.
        """
        return self.get_alpha_numeric(character_count, 'lower')

    def get_unique_list(self, list_size=5, item_length=None):
        """
        Get a list of unique names.
        :param list_size: Number of unique names in the list.
        :param item_length: Length of each item within the list.
        :return: Returns a list with unique names.
        """
        name_list = []
        for i in range(0, list_size):
            name_list.append(self.get_unique_name(item_length[i]))
        return name_list

    def verify_text_contains(self, actual_text, expected_text):
        """
        Verify that actual_text contains expected_text string.
        :param actual_text: Captured text value from web page
        :param expected_text: given text to test against actual_text.
        :return: True / False
        """
        self.automation_logger.info("Actual Text from web application :: " + actual_text)
        self.automation_logger.info("Expected Text from web application :: " + expected_text)
        if expected_text.lower() in actual_text.lower():
            self.automation_logger.info("# Verification contains")
            return True
        else:
            self.automation_logger.info("# Verification does NOT contain.")
            return False

    def verify_text_match(self, actual_text, expected_text):
        """
        Verify if the actual_text matches (exactly) the expected_text
        :param actual_text: Captured text value from web page
        :param expected_text: given text to test against actual_text
        :return: True / False
        """
        self.automation_logger.info("Actual Text from web application :: " + actual_text)
        self.automation_logger.info("Expected Text from web application :: " + expected_text)
        if actual_text.lower() == expected_text.lower():
            self.automation_logger.info("# Verification matched.")
            return True
        else:
            self.automation_logger.info("# Verification does NOT match.")
            return False

    def verify_list_match(self, expected_list, actual_list):
        """
        Verify if two lists match.
        :param expected_list: Provided list to match against actual_list.
        :param actual_list: Captured list.
        :return: True / False
        """
        return set(expected_list) == set(actual_list)

    def verify_list_contains(self, expected_list, actual_list):
        """
        Verify that actual_list contains elements of expected_list.
        :param expected_list: Provided list to match against actual_list
        :param actual_list: Captured list
        :return: True / False
        """
        for i in range(0, len(expected_list)):
            if expected_list[i] not in actual_list:
                return False
            else:
                return True
