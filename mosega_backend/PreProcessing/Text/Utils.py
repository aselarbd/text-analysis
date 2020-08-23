import os
import re
import logging
import io
import copy
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
    temporaryFilePath = os.getcwd() + "/" + configs['temporaryFile']['path']
    given_file = open(path, 'r')

    with io.open(temporaryFilePath, mode="w+", encoding="utf-8") as f:
        try:
            f.truncate(0)
            LOGGER.debug("Cleaned the temporary file")

            for line in given_file:

                if idTermFound:
                    f.write(line + '\n')
                else:
                    if re.compile('|'.join(idTerms), re.IGNORECASE).search(line):
                        idTermFound = True
                        f.write(line + '\n')
                        LOGGER.debug('Identification words found')
        except IOError:
            LOGGER.debug("Error while cleaning temporary file")

        given_file.close()

    LOGGER.debug("Read the" + fileType + " file : " + path)

    selectedFile = open(temporaryFilePath, "r+")
    read_file_context = copy.deepcopy(selectedFile.read())
    selectedFile.close()
    return read_file_context
