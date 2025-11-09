"""This is wrapper/framework or a customized selenium webdriver methods to perform different operations as
required. The methods defined in this wrapper can be utilized anywhere in the test/page classes thus enabling
predefined basic selenium webdriver methods. This may include clicking, element checking, presence of the element,
generic explict wait, generic screenshot etc. Whichever required methods can be called anywhere in the page/test
classes"""
import logging
import selenium
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
# IMPORT FOR ec
from selenium.webdriver.support.ui import WebDriverWait
# IMPORT FOR EXPLICIT WAIT METHOD
from selenium.common.exceptions import *
# IMPORT FOR IGNORING COMMON SELENIUM EXCEPTIONS
from traceback import print_stack
# TO PRINT THE TRACEBACK FROM THE TERMINAL WHENEVER A TEST FAILS
import utilities.custom_logger as cl
import time
import os

class seleniumWebdriverCustom():

    log = cl.customLogger(logging.ERROR)
    # Called the custom logger method by creating a log variable at the class level, applies to all methods

    def __init__(self, driver):     # Constructor
        self.driver = driver

    # method to capture the screenshots
    def screenshots(self, resultMessage):
        fileName = resultMessage + "." + str(round(time.time() * 1000)) + ".png"
        # file name generator along with the timestamp to differentiate
        screenshotDirectory = "../screenshots/"
        relativeFileName = screenshotDirectory + fileName  # ../screenshots/.png
        # this variable gives the screenshot name along with the screenshots directory
        currentDirectory = os.path.dirname(__file__)
        # variable with the os method which gives the actual directory where the screenshot is taken
        destinationFileName = os.path.join(currentDirectory, relativeFileName)
        # this is the complete file name including the complete directory and correct file name
        destinationDirectory = os.path.join(currentDirectory, screenshotDirectory)
        # this is the complete directory where the screenshots will be saved

        try:
            if not os.path.exists(destinationDirectory):
                os.makedirs(destinationDirectory)
                # this if creates a directory of it is not created manually
            self.driver.save_screenshot(destinationFileName)
            self.log.info("Screenshot save to directory: " + destinationDirectory)
        except:
            self.log.error("### Exception Occurred when taking screenshot")
            print_stack()

    # to get the title
    def getTitle(self):
        return self.driver.title
            # OR
        # Title_value = self.driver.title
        # self.log.info(str(Title_value))
        # return Title_value

    # generic method to get the BY type
    def getByType(self, locatorType):
        locatorType = locatorType.lower()
        if locatorType == "id":
            return By.ID
        elif locatorType == "xpath":
            return By.XPATH
        elif locatorType == "class":
            return By.CLASS_NAME
        elif locatorType == "css":
            return By.CSS_SELECTOR
        elif locatorType == "name":
            return By.NAME
        elif locatorType == "link":
            return By.LINK_TEXT
        else:
            print("Proper locator type is not specified")
        return False

    # Finding the element
    def getElement(self, elementLocator, locatorType):
        element = None
        try:
            locatorType = locatorType.lower()
            byType = self.getByType(locatorType)
            element = self.driver.find_element(byType, elementLocator)
            self.log.info("Element found with locator: " + elementLocator +
                          " and locator type: " + locatorType)
        except:
            self.log.critical("element not found")
        return element

    # Custom method to click an element which is found using the getElement() method in this wrapper
    def elementClick(self, elementLocator="", locatorType="id", element=None):
        try:
            if elementLocator:
                element = self.getElement(elementLocator, locatorType)
            element.click()
            # print("element is clicked with the locator " + elementLocator + " and locator type " + locatorType)
            # used to self.log.info to treat the print statements as log messages
            self.log.info("element is clicked with the locator " + elementLocator + " and locator type " + locatorType)
        except:
            self.log.error("element was not clickable with " + elementLocator + " and locator type " + locatorType)
            print_stack()

    # For sending the data this method id created, can be called wherever required in the page class
    def sendKeys(self, data, elementLocator, locatorType = "id"):
        try:
            element = self.getElement(elementLocator, locatorType)
            element.send_keys(data)
            self.log.info("Data is passed to the element with the locator " + elementLocator +
                          " and locator type " + locatorType)
        except:
            self.log.error("Data was not passed with " + elementLocator + " and locator type " + locatorType)
            print_stack()

    # checking element present or not
    def isElementPresent(self, elementLocator, locatorType = "id"):
        element = None
        try:
            locatorType = locatorType.lower()
            byType = self.getByType(locatorType)
            element = self.driver.find_element(byType, elementLocator)
            # this format(first byType and then elementlocator) is standard, otherwise it will return false
            if element is not None:
                self.log.info("element is present")
                return True
            else:
                self.log.error("element not present")
                return False
        except:
            print("element not found")
            return False

    # Explicit wait
    def genericExplicitWait(self, locator, timeout=10, poll_frequency=1, locatorType="id"):
        element = None
        try:
            self.driver.implicitly_wait(0)
            # making the implicit wait defined in the ExplicitWait_wrapper to '0'
            byType = self.getByType(locatorType)
            # using the getByType method to pass the bytype to wait method
            print("waiting for " + str(timeout) + " seconds of time in finding the element")
            # EXPLICIT WAIT SYNTAX
            wait = WebDriverWait(self.driver, timeout=timeout, poll_frequency=poll_frequency,
                                 ignored_exceptions=[NoAlertPresentException,
                                                     NoSuchElementException,
                                                     NoSuchDriverException])
            element = wait.until(EC.visibility_of_element_located((byType, locator)))
            print("the required element is found")
        except:
            print("element could not be found")
        self.driver.implicitly_wait(2)
        return element

    # ADDITIONAL USEFUL METHODS

    # To find the list of elements which will have common elementLocator
    def getElementList(self, elementLocator, locatorType="ID"):

        element = None
        try:
            locatorType = locatorType.lower()
            byType = self.getByType(locatorType)
            element = self.driver.find_elements(byType, elementLocator)
            self.log.info("The list of element is found with: " + elementLocator +
                          " and with locator: " + locatorType)
        except:
            self.log.error("element list not found")
            print_stack()
            return False
        return element

    # To scroll the webpage
    def scrolling(self, direction=""):
        if direction == "up":
            self.driver.execute_script("window.scrollBy(0, -750);")

        if direction == "down":
            self.driver.execute_script("window.scrollBy(0, 750);")

    # To get the text and attribute from the element
    def getText(self, elementLocator="", locatorType="ID", element=None, Info=""):
        text = None
        try:
            if elementLocator:
                element = self.getElement(elementLocator, locatorType)
            text = element.text
            self.log.info("The length of the text is: " + str(len(text)))
            if len(text) == 0:
                text = element.get_attribute("inner text")
            if len(text) != 0:
                self.log.info("The text is: " + text)
                text = text.strip()
        except:
            self.log.error("Cannot retrieve the text of the element")
            print_stack()
            return False
        return text

    # To check whether the element is displayed in the UI or not
    def isElementDisplayed(self, elementLocator="", locatorType="ID", element=None):
        isDisplayed = True
        try:
            if elementLocator:
                element = self.getElement(elementLocator, locatorType)
            if element is not None:
                isDisplayed = self.driver.is_displayed()
                self.log.info("The element is displayed in the UI with locator: " + elementLocator +
                              " and with locator type: " + locatorType)
            else:
                self.log.error("The element is not displayed in the UI with locator: " + elementLocator +
                               " and with locator type: " + locatorType)
            return isDisplayed
        except:
            self.log.error("element not found")
            print_stack()
            return False

    # to switch frames
    def switchToFrame(self, frameNumber):
        try:
            self.driver.switch_to.frame(frameNumber)
            self.log.info("Driver is switched to frame: " + frameNumber)
        except:
            self.log.error("Frame cannot be found")
            return False

    # to switch to default content
    def switchToDefaultContent(self):
        self.driver.switch_to.default_content()
        self.log.info("Driver switched back to default content")