import os
import logging
import Shared.SharedFunctions as functions

configs = functions.loadConfigs()


def setupLog():
    """
    Setup log levels
    """
    logFile = configs['logging']['path']
    logStyle = configs['logging']['format']
    logging.basicConfig(filename=os.path.abspath(logFile), level=logging.DEBUG, format=logStyle)
