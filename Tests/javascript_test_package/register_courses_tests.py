from Pages.javascript_test_package.register_courses_page import RegisterCourses
from Utilities.status_of_tests import StatusOfTest
import unittest
import pytest


@pytest.mark.usefixture('one_time_setup', 'set_up')
class RegisterCoursesTests(unittest.TestCase):

    @pytest.fixture(autouse=True)
    def class_setup(self, set_up):
        self.register_courses_page = RegisterCourses(self.driver)
        self.test_status = StatusOfTest(self.driver)

    @pytest.mark.run(order=1)
    def test_register_course_invalid(self):
        self.register_courses_page.enroll_in_course('JavaScript', "JavaScript for beginners",
                                                    '1111111111111111', '1111', '111', '11111')
        result = self.register_courses_page.verify_enroll_fail()
        self.test_status.mark_final("test_register_course_invalid", result,
                                    "Verification of invalid registration of course")
