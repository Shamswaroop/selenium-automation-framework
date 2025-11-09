"""This is a common base page class where the defined methods can be inherited in any of the page classes. This will
become useful when there are similar methods between different pages, in that case instead of defining the logic
in all of them this class can be inherited"""
from base.selenium_webdriver import seleniumWebdriverCustom
from utilities.util import Util
from traceback import print_stack

class BasePage(seleniumWebdriverCustom):    # inheriting the seleniumWebdriverCustom to use the method defined in it

    def __init__(self, driver):

        super(BasePage, self).__init__(driver)  # super class instantiation
        self.driver = driver
        self.util = Util()
        """Creating an object of util class in the constructor such that when this class is inherited or instance is
        created the object will be instantiated"""

    def verifyPageTitle(self, titleToVerify):

        try:
            actualTitle = self.getTitle() # method defined in the seleniumWebdriverCustom
            return self.util.verifyTextContains(actualTitle, titleToVerify)
            # calling the util method by passing the input parameters
        except:
            self.log.error("Failed to get the title")
            print_stack()
            return False


