"""Common utilities class which can be made useful/inherited in the basepage for any methods, these are not
concrete methods user can define whichever utility required by making the page class simpler and code redundancy.
Basically performing the logics"""
import logging
import utilities.custom_logger as cl

class Util(object):

    log = cl.customLogger(logging.INFO)

    # For checking a sub string or full text contains or not
    def verifyTextContains(self, actualText, expectdText):
        """This is a utility method which takes two text parameters and matches the text then returns boolean, this
        will be useful in the base page class whenever there is a condition in any of the page to verify any title
        or text. Base page class will inherit this method into the methods defined in them, which will be in turn
        inherited in the different page class wherever the requirement is."""

        self.log.info("Actual Text From Application Web UI --> :: " + actualText)
        self.log.info("Expected Text From Application Web UI --> :: " + expectdText)
        if expectdText.lower() in actualText.lower():
            self.log.info("### VERIFICATION CONTAINS THE TEXT")
            return True
        else:
            self.log.error("### VERIFICATION DOES NOT CONTAINS THE TEXT")
            return False

    # For complete text compare or equating
    def verifyTextMatch(self, actualText, expectdText):

        self.log.info("Actual Text From Application Web UI --> :: " + actualText)
        self.log.info("Expected Text From Application Web UI --> :: " + expectdText)
        if expectdText.lower() == actualText.lower():
            self.log.info("### VERIFICATION MATCHED")
            return True
        else:
            self.log.error("### VERIFICATION DOES NOT MATCH")
            return False