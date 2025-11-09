"""This is a different approach to assert methods. In general when there are multiple assertion check points in a test
case and any one of the initial checkpoint/assertion fails the rest of the steps execution in that test case will
not take place.
To overcome this, this class can be utilized where all the checkpoints are collected and stored in a list not
asserting them to any results, once completing all the checkpoints in the test case this list is asserted at the
final checkpoint stating the results, if any FAIL assertion is present the whole test case is marked as FAILEd.
This approach eliminates the stopping of test execution when an assertion fails"""
import logging
from base.selenium_webdriver import seleniumWebdriverCustom
import utilities.custom_logger as cl

class TestStatus(seleniumWebdriverCustom):
    """It inherits from another class seleniumWebdriverCustom. This means TestStatus will get all the methods
     and attributes defined in seleniumWebdriverCustom."""

    log = cl.customLogger(logging.INFO)

    def __init__(self, driver):

        super(TestStatus, self).__init__(driver)
        # This calls the parent class (seleniumWebdriverCustom) constructor, and passes driver to it.
        self.resultList = []

    def setResult(self, result, resultMessage):
        """This is the method which takes the return value from the page object methods created for any assertion used
        in the test class and verify the return booleans and append them to a list. The return value either True or
        False it doesn't matter since it is not asserted yet"""
        try:
            if result is not None:
                if result: #(if result is True)
                    self.resultList.append("PASS")
                    self.log.info("### VERIFICATION SUCCESSFUL:: " + resultMessage)
                else:
                    self.resultList.append("FAIL")
                    self.log.error("### VERIFICATION FAILED:: " + resultMessage)
                    self.screenshots(resultMessage) # to take screenshots when test fails
            else:
                self.resultList.append("FAIL")
                self.log.error("### VERIFICATION FAILED:: " + resultMessage)
                self.screenshots(resultMessage)
        except:
            self.resultList.append("FAIL")
            self.log.error("### EXCEPTION OCCURRED")
            self.screenshots(resultMessage)

    def mark(self, result, resultMessage):
        """This method mark the result of the checkpoints into the list using the setResult method, maintaining a list
        of the results, no assertion. This method is called in the initial checkpoints"""
        self.setResult(result, resultMessage)

    def markFinal(self, testName, result, resultMessage):
        """This is the method which will be called in the final test step/checkpoint in a test case. This method
        will assert the failed/passed test steps based on the result stored in the list created. Thus, passing or
        failing that particular test case without affecting the test execution of all the test steps"""
        self.setResult(result, resultMessage)

        if "FAIL" in self.resultList:
            self.log.error(testName + " TEST FAILED")
            self.resultList.clear()
            assert True is False
        else:
            self.log.info(testName + " TEST PASSED")
            self.resultList.clear()
            assert True is True