from base.base_page import BasePage
import logging
import utilities.custom_logger as cl
import time

class course_registeration(BasePage):

    log = cl.customLogger(logging.INFO)

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # Locators
    _all_Courses = "//a[text() = 'ALL COURSES']"
    _search_icon = "//input[@name= 'course']"
    _submit_Button = "//button[@type = 'submit']"
    _course_Selection = "//h4[@class= 'dynamic-heading']"
    _enroll_Button = "//button[text()= 'Enroll in Course']"
    _cc_Num = "//input[@placeholder = 'Card Number']"
    _cc_Exp = "//input[@placeholder = 'MM / YY']"
    _cc_Cvv = "//input[@placeholder = 'Security Code']"
    _error_Message = "//ul[@class = 'list-unstyled']/li[1]"

    # Page objects
    def courseSelection(self, course):
        self.elementClick(self._all_Courses, locatorType="xpath")
        time.sleep(2)
        self.sendKeys(course, self._search_icon, locatorType="xpath")
        time.sleep(2)
        self.elementClick(self._submit_Button, locatorType="xpath")
        time.sleep(2)
        self.elementClick(self._course_Selection, locatorType="xpath")
        time.sleep(2)

    def courseEnroll(self):
        self.elementClick(self._enroll_Button, locatorType="xpath")

    def ccNumber(self, Num):
        self.switchToFrame(0)
        self.sendKeys(Num, self._cc_Num, locatorType="xpath")
        time.sleep(2)
        self.switchToDefaultContent()

    def ccExp(self, expDate):
        self.switchToFrame(2)
        self.sendKeys(expDate, self._cc_Exp, locatorType="xpath")
        time.sleep(2)
        self.switchToDefaultContent()

    def cvvNum(self, cvv):
        self.switchToFrame(4)
        self.sendKeys(cvv, self._cc_Cvv, locatorType="xpath")
        self.switchToDefaultContent()

    def enterCreditCardInfo(self, Num, expDate, cvv):
        self.ccNumber(Num)
        time.sleep(2)
        self.ccExp(expDate)
        time.sleep(2)
        self.cvvNum(cvv)
        time.sleep(2)

    def enrollCourse(self, Num="", expDate="", cvv=""):
        self.courseEnroll()
        time.sleep(2)
        self.scrolling(direction="down")
        time.sleep(2)
        self.enterCreditCardInfo(Num, expDate, cvv)
        time.sleep(2)

    def errorMessage(self):
        result = self.isElementDisplayed(self._error_Message, locatorType="xpath")
        return not result