import pytest
from selenium import webdriver
from base.webdriver_factory import WebDriverFactory
from pages.login.login_page import login_Page
@pytest.fixture()   # this decorator will run once before and after each test methods are run in a module
def setUp():
    print("SetUp for each method")
    yield
    print("Teardown for each method")

@pytest.fixture(scope="class")
def oneTimeSetup(request, browser):
    print("SetUp at module level")

    wdf = WebDriverFactory(browser)      # creating an object for the WebDriverFactory class by passing the browser arg
    driver = wdf.getWebDriverInstancce()    # calling the method which returns the driver instance to driver variable
    if request.cls is not None:
        request.cls.driver = driver     # adding the driver as the class level attribute which will be returned
    yield driver
    driver.quit()       # added after the yield, such that it will be a tear down method
    print("Teardown at module level")

def pytest_addoption(parser):   # Python hook which takes the parser as the arg
    parser.addoption("--browser")

@pytest.fixture(scope="module")
def browser(request):
    return request.config.getoption("--browser")