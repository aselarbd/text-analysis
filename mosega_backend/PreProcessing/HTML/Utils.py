import io
import os
import logging
from Shared.SharedFunctions import load_configs
import Shared.LogSetup as logSetup
import justext
import requests


configs = load_configs()
logSetup.setupLog()

LOGGER = logging.getLogger(__name__)


def cleanTags(url):
    """
    Clean HTML Tags of given URL
    """
    page = requests.get(url).text.encode('utf-8')
    formatted_text = ""
    paragraphs = justext.justext(page, justext.get_stoplist('English'))
    for paragraph in paragraphs:
        if paragraph.class_type == 'good':
            if paragraph.is_heading or header_checker(paragraph.words_count, paragraph.text):
                formatted_text += "########## " + paragraph.text + "\n"
            else:
                formatted_text += paragraph.text + "\n"

    LOGGER.debug("HTML file cleaned : "+url)
    return formatted_text


def header_checker(word_count, text):
    if word_count <= 7:
        if text.startswith("(") and text.endswith(")"):
            return False
        else:
            return True
    else:
        return False




def createFile(content, file_type):
    """
    write given content to given file
    """
    path = ""

    if file_type == "policy":
        path = configs['policyFiles']['path']
    elif file_type == "term":
        path = configs['termFiles']['path']

    file_path = os.getcwd()+"/"+path

    with io.open(file_path, mode="w+", encoding="utf-8") as f:
        try:
            f.write(content)
            LOGGER.debug("cleaned HTML was wrote a file")
        except IOError:
            LOGGER.debug("Error while writing the cleaned HTML to a file")


def generateFile(url, file_type):
    """
    given url is formatted by removing HTML tags and saved to a file  and return saved file name
    """
    content = cleanTags(url)
    createFile(content, file_type)
