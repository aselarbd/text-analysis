import io
import logging
import os
from Shared.SharedFunctions import loadConfigs
from PreProcessing.CreateDataStructure import createDataStructure
from PreProcessing.HTML.Utils import generateFile
from PreProcessing.Text.Utils import readFile
configs = loadConfigs()
LOGGER = logging.getLogger(__name__)


def readURL(url, url_type):
    """
    Fetch data from given URL -> clean HTML elements -> save content to temporary txt file ->
    read from temporary file -> remove temporary file
    """

    generateFile(url, url_type)
    path = ""
    if url_type == "policy":
        path = configs['policyFiles']['path']
    elif url_type == "term":
        path = configs['termFiles']['path']
    file_path = os.getcwd() + "/" + path
    url_data = readFile(file_path, url_type)

    with io.open(file_path, mode="w+", encoding="utf-8") as f:
        try:
            f.truncate(0)
            LOGGER.debug("Successfully deleted temporary file")
        except IOError:
            LOGGER.debug("Error In deleting temporary file")
    return url_data


def startPipeline(url, url_type):
    """
    startPipeline gives structured policy
    """
    unstructured_data = readURL(url, url_type)
    structured_data = createDataStructure(unstructured_data)

    return structured_data


def getPolicy(url):
    """
    Get policy for given URL

    @param url: policy URL
    @return: policy structure
    """
    return startPipeline(url, "policy")


def getTerm(url):
    """
    Get term for given URL

    @param url: Term URL
    @return: policy structure
    """
    return startPipeline(url, "term")
