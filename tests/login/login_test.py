"""I have created a python package inside a package because this is the test class/cases base on the
scenarios. For eg, this is for login page and one more will be created for some other functionality
likewise the framework is built with these different packages and maintaining code redundancy"""
import time
import pytest
from pages.login.login_page import login_Page
import unittest     # Imported unittest lib, such that the execution can be done from the terminal using py.test
from utilities.test_status import TestStatus

"""Test cases using the common class for assertions, without stopping the test execution"""
@pytest.mark.usefixtures("oneTimeSetup", "setUp")
class LoginTests(unittest.TestCase):

    """class level setup for browser instantiation by using the conftest class level setup and the driver instance is
    passed to login_page page object to perform the tests"""
    @pytest.fixture(autouse=True)
    def classSetup(self, oneTimeSetup):
        self.lp_obj = login_Page(self.driver)   # login_Page object
        self.ts_obj = TestStatus(self.driver)   # testStatus object

    @pytest.mark.run(order=3)
    def test_ValidLogin(self):
        self.lp_obj.login("test@email.com", password="abcabc")
        result3 = self.lp_obj.successfulLogin()
        self.ts_obj.markFinal("test_ValidLogin", result3, "Checking valid login")
        # assert result3 == True

    @pytest.mark.run(order=1)
    def test_invalidLogin(self):
        self.lp_obj.login(username="egsbhs@email.com", password="abcabcabc")
        time.sleep(3)
        result = self.lp_obj.unsuccessfulLogin()
        self.ts_obj.markFinal("test_invalidLogin", result, "Checking invalid login")
        # assert result == True

    @pytest.mark.run(order=2)
    def test_onlyPassword(self):
        self.lp_obj.login(password="abcabc")
        time.sleep(3)
        result1 = self.lp_obj.verifyTitle()
        self.ts_obj.mark(result1, "Title verification")
        result2 = self.lp_obj.verifyLogo()
        self.ts_obj.mark(result2, "Logo verification")
        result3 = self.lp_obj.noEmailLogin()
        self.ts_obj.markFinal("test_onlyPassword", result3, "Login Verification")