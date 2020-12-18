import copy
import io
import logging
import os
import re
import Shared.LogSetup as logSetup
from Shared.SharedFunctions import load_configs, load_identification_terms

configs = load_configs()
identificationTerms = load_identification_terms()
logSetup.setupLog()

LOGGER = logging.getLogger(__name__)


def readFile(path, file_type):
    """
    This function will read given file in file path and return the privacy policy / terms of conditions part.
    """

    id_terms = None

    # Predefined identification of policy / terms
    if file_type == "policy":
        id_terms = identificationTerms['policy']['identification']
    elif file_type == "term":
        id_terms = identificationTerms['term']['identification']

    # Boolean value to check identification terms found
    id_term_found = True

    # Temporary variable to store newly processed file after cross check with identification terms
    temporary_file_path = os.getcwd() + "/" + configs['temporaryFile']['path']
    given_file = open(path, 'r')

    with io.open(temporary_file_path, mode="w+", encoding="utf-8") as f:
        try:
            f.truncate(0)
            LOGGER.debug("Cleaned the temporary file")

            for line in given_file:

                if id_term_found:
                    f.write(line + '\n')
                else:
                    if re.compile('|'.join(id_terms), re.IGNORECASE).search(line):
                        id_term_found = True
                        f.write(line + '\n')
                        LOGGER.debug('Identification words found')
        except IOError:
            LOGGER.debug("Error while cleaning temporary file")

        given_file.close()

    LOGGER.debug("Read the" + file_type + " file : " + path)

    selected_file = open(temporary_file_path, "r+")
    read_file_context = copy.deepcopy(selected_file.read())
    selected_file.close()
    return read_file_context
