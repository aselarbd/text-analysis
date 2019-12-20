import os
import re
import logging
import Shared.SharedFunctions as functions
import Shared.LogSetup as logSetup

configs = functions.loadConfigs()
identificationTerms = functions.loadIdentificationTerms()
logSetup.setupLog()

LOGGER = logging.getLogger(__name__)


def readFile(path, fileType):
    """
    This function will read given file in file path and return the privacy policy / terms of conditions part.

    :return: policy text
    @param path: path of the file
    @param fileType: type of the file policy or terms of conditions
    """

    idTerms = None

    # Predefined identification of policy / terms
    if fileType == "policy":
        idTerms = identificationTerms['policy']['identification']
    elif fileType == "term":
        idTerms = identificationTerms['term']['identification']

    # Boolean value to check identification terms found
    idTermFound = False

    # Temporary variable to store newly processed file after cross check with identification terms
    temporaryFile = open("temp.txt", "w+")

    given_file = open(path, 'r')
    for line in given_file:

        if idTermFound:
            temporaryFile.write(line + '\n')
        else:
            if re.compile('|'.join(idTerms), re.IGNORECASE).search(line):
                idTermFound = True
                temporaryFile.write(line + '\n')
                LOGGER.debug('Identification words found')

    temporaryFile.close()

    LOGGER.debug("Read the" + fileType + " file : " + path)

    selectedFile = open("temp.txt", "r")
    os.remove("temp.txt")
    return selectedFile.read()
