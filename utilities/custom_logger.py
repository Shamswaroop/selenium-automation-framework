"""This is a customized logger example, which can be used anywhere in the project or with any other class files
by calling the methods defined and by providing the log level.

inspect python module helps to retrieve the class or method name along with the log message, in whichever the
class/methods this custom logger is called."""
import inspect # this python module helps to retrieve the class or method name for the log message
import logging

def customLogger(logLevel=logging.INFO):
    # given the DEBUG as the default parameter, if nothing is passed when the method is called

    loggerName = inspect.stack()[1][3]
    logger = logging.getLogger(loggerName)
    logger.setLevel(logging.INFO)

    fileHandler = logging.FileHandler(filename="testlogs.log", mode="w") # a-append, w-write
    fileHandler.setLevel(logLevel)
    formatter = logging.Formatter("%(asctime)s- %(name)s- %(levelname)s: %(message)s ",
                    datefmt="%m/%d/%Y %H:%M:%S %p")
    fileHandler.setFormatter(formatter)
    logger.addHandler(fileHandler)

    return logger
    # returning the logger to outside