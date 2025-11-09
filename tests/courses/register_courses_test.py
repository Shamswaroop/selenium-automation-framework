import pytest
from pages.courses.register_courses_page import course_registeration
import unittest
from utilities.test_status import TestStatus

@pytest.mark.usefixtures("oneTimeSetup", "setUp")
class Course_registeration(unittest.TestCase):

    @pytest.fixture(autouse=True)
    def classSetup(self, oneTimeSetup):
        self.cr_obj = course_registeration(self.driver)  # register object
        self.ts_obj = TestStatus(self.driver)  # testStatus object

    @pytest.mark.run(order=1)
    def test_courseRegistered(self):
        self.cr_obj.courseSelection(course="javascript")
        self.cr_obj.courseEnroll()
        self.cr_obj.enrollCourse(Num="2222", expDate="1111", cvv="234")
        result = self.cr_obj.errorMessage()
        self.ts_obj.markFinal("test_courseRegistered", result,
                              "Checking whether the error message is displayed or not")