import io
import os
import logging
from Shared.SharedFunctions import loadConfigs
import Shared.LogSetup as logSetup
import justext
import requests


configs = loadConfigs()
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
            if paragraph.is_heading:
                formatted_text += "## " + paragraph.text + "\n"
            else:
                formatted_text += paragraph.text + "\n"

    LOGGER.debug("HTML file cleaned : "+url)
    return formatted_text


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
