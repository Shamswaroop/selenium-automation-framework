"""POM for the login page, completely taking out the functionality of the in the pythin class into a
page object where all the operations will be carried out and the python class file/test case will have
only the high level info"""
from base.base_page import BasePage
import logging
import utilities.custom_logger as cl

class login_Page(BasePage):
    """Whenever any of the page class methods are required to use the common methods defined in the base page, then the
    Base page class need to be inherited by treating it as a super class"""

    log = cl.customLogger(logging.INFO)
    """log object created by calling the custom logger to have the class name login_Page() in the log file
    instead of having seleniumWebdriverCustom name in the log file"""

    def __init__(self, driver): # Instantiation of driver constructor
        super().__init__(driver) # Calling the init method of super class by providing the driver instance
        self.driver = driver

    # Locators
    _signIn_Link = "//a[text() = 'Sign In']"
    _emailIdField = "//input[@placeholder ='Email Address']"
    _password_Field = "password"
    _login_Button = "login"
    _successful_Login = "jqNotification"
    _unsuccessful_Login = "//span[@id='incorrectdetails']"
    _noPassword_Error = "//span[contains(text(),'The password field is required.')]"
    _noEmail_Error = "//span[contains(text(),'The email field is required.')]"
    _logo_element = "img-fluid"

    # Page objects
    def clickLoginLink(self):
        self.elementClick(self._signIn_Link, locatorType="xpath")

    def enterEmail(self, username):
        self.sendKeys(username, self._emailIdField, locatorType="xpath")

    def enterPassword(self, password):
        self.sendKeys(password, self._password_Field, locatorType="name")

    def clickLoginButton(self):
        self.elementClick(self._login_Button)

    def clearText(self):
        email = self.getElement(self._emailIdField, locatorType="xpath")
        email.clear()
        password = self.getElement(self._password_Field, locatorType="name")
        password.clear()

    def login(self, username="", password=""):
        """username and password are given with empty values, treating them as optional parameters. Such that
        whenever the method is called need not pass the values by default"""
        self.clickLoginLink()
        self.clearText()
        self.enterEmail(username)
        self.enterPassword(password)
        self.clickLoginButton()

    def successfulLogin(self):
        element = self.isElementPresent(self._successful_Login, locatorType="class")
        return element

    def unsuccessfulLogin(self):
        element = self.isElementPresent(self._unsuccessful_Login, locatorType="xpath")
        return element

    def noPasswordLogin(self):
        passwordElementError = self.isElementPresent(self._noPassword_Error, locatorType="xpath")
        return passwordElementError

    def noEmailLogin(self):
        emailElementError = self.isElementPresent(self._noEmail_Error, locatorType="xpath")
        return emailElementError

    def verifyLogo(self):
        element = self.isElementPresent(self._logo_element, "class")
        return element

    def verifyTitle(self):
        return self.verifyPageTitle("login")