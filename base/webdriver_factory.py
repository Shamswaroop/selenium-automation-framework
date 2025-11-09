"""This is a base file which provides a driver instance of browsers, it takes hte browser as the command line
argument and returns it"""
from selenium import webdriver

class WebDriverFactory():

    def __init__(self, browser):
        self.browser = browser

    def getWebDriverInstancce(self):

        if self.browser == "Chrome":
            driver = webdriver.Chrome()
        elif self.browser == "Edge":
            driver = webdriver.Edge()
        elif self.browser == "Firefox":
            driver = webdriver.Firefox()
        else:
            driver = webdriver.Chrome()

        driver.get("https://www.letskodeit.com/")
        driver.maximize_window()
        driver.implicitly_wait(5)
        return driver