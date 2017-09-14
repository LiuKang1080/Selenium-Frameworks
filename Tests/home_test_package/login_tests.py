from Pages.home_test_package.login_page import LoginPage
from Utilities.status_of_tests import StatusOfTest
import unittest
import pytest


@pytest.mark.usefixtures('one_time_setup', 'set_up')
class LoginTests(unittest.TestCase):

    @pytest.fixture(autouse=True)
    def class_setup(self, set_up):
        self.login_page = LoginPage(self.driver)
        self.test_status = StatusOfTest(self.driver)

    @pytest.mark.run(order=1)
    def test_valid_login(self):
        # self.login_page.login('test@gmail.com', 'abcabc')
        result1 = self.login_page.verify_title()
        self.test_status.mark(result1, "Verification of page title.")
        result2 = self.login_page.verify_login()
        self.test_status.mark_final("test_valid_login", result2, "Verification of login on second page.")

    @pytest.mark.run(order=2)
    def test_invalid_login(self):
        # self.login_page.login('test@gmail.com', 'abc123abc123')
        result = self.login_page.verify_invalid_login()
        self.test_status.mark_final("test_invalid_login", result, "verification of invalid login.")
