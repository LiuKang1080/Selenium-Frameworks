from Pages.register_courses_page_package.register_courses_page import RegisterCourses
from Utilities.status_of_tests import StatusOfTest
import unittest
import pytest
from ddt import ddt, data, unpack


@ddt
@pytest.mark.usefixture('one_time_setup', 'set_up')
class RegisterCoursesTests(unittest.TestCase):

    @pytest.fixture(autouse=True)
    def class_setup(self, set_up):
        self.register_courses_page = RegisterCourses(self.driver)
        self.test_status = StatusOfTest(self.driver)

    @pytest.mark.run(order=1)
    @unpack
    @data(("Javascript", "JavaScript for beginners", '1111111111111111', '1111', '111', '11111'),
          ("Python", "Learn Python 3 from scratch", '2222222222222222', '2222', '222', '22222'))
    def test_register_course_invalid(self, course_to_search, full_course_name, credit_num, exp_date, cvc_num, zip_num):
        self.register_courses_page.enroll_in_course(course_title=course_to_search, full_course_name=full_course_name,
                                                    credit_num=credit_num, exp_date=exp_date,
                                                    cvc_num=cvc_num, zip_num=zip_num)
        result = self.register_courses_page.verify_enroll_fail()
        self.test_status.mark_final("test_register_course_invalid", result,
                                    "Verification of invalid registration of course")

        self.driver.find_element_by_xpath("//div[@class='navbar-header']//a").click()
