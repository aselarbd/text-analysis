"""
This File contains the text file reading methods
"""
import os

import re
import logging
from mosega_backend.ConfigHandler import *

# Load text processing constants and configs
text_processing_constants = ConfigHandler.load_config('TextProcessingConstants.yaml')
configs = ConfigHandler.load_config('config.yaml')


# Logger
logger = logging.getLogger(__name__)
log_file_path = configs['logging']['abs_path']
log_level = configs['logging']['level']
log_format = configs['logging']['format']

logging.basicConfig(filename=os.path.abspath(log_file_path), level=logging.INFO, format=log_format)


def read_file(path):
    """
    This function will read given file in file path and return the privacy policy part.

    :param path: file path
    :return: policy text
    """

    msg = 'Read the file : ' + path
    logger.info(msg)

    # Predefined identification terms of privacy policy
    identification_terms = text_processing_constants['policy']['identification']

    # Boolean value to check identification terms found
    is_identification_terms_found = False

    # Temporary variable to store newly processed file after cross check with identification terms
    processed_file = open("temp_policy.txt", "w+")

    given_file = open(path, 'r')
    for line in given_file:

        if is_identification_terms_found:
            processed_file.write(line + '\n')
        else:

            if re.compile('|'.join(identification_terms), re.IGNORECASE).search(line):
                is_identification_terms_found = True
                processed_file.write(line + '\n')

                msg = 'Identification words found'
                logger.info(msg)

    processed_file.close()

    read_policy = open("temp_policy.txt", "r")
    os.remove("temp_policy.txt")

    return read_policy.read()




