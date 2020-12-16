import os
import logging
import Shared.SharedFunctions as functions

configs = functions.load_configs()


def setupLog():
    """
    Setup log levels
    """
    logFile = configs['logging']['path']
    logStyle = configs['logging']['format']
    fileName = os.path.abspath(logFile)

    # open(fileName, "w+")

    # logging.basicConfig(filename=fileName, level=logging.DEBUG, format=logStyle)
