import io
import logging
import os

import Shared.SharedFunctions as functions
from PreProcessing.CreateDataStructure import createDataStructure
from PreProcessing.HTML.Utils import generateFile
from PreProcessing.Text.Utils import readFile

configs = functions.loadConfigs()
LOGGER = logging.getLogger(__name__)


def readURL(url, URLType):
    """
    Fetch data from given URL -> clean HTML elements -> save content to temporary txt file ->
    read from temporary file -> remove temporary file

    @param URLType: policy or term
    @param url: page URL
    @return: cleaned content form given URL
    """

    generateFile(url, URLType)
    path = ""
    if URLType == "policy":
        path = configs['policyFiles']['path']
    elif URLType == "term":
        path = configs['termFiles']['path']
    filePath = os.getcwd() + "/" + path
    urlData = readFile(filePath, URLType)

    with io.open(filePath, mode="w+", encoding="utf-8") as f:
        try:
            f.truncate(0)
            LOGGER.debug("Successfully deleted temporary file")
        except IOError:
            LOGGER.debug("Error In deleting temporary file")
    return urlData


def startPipeline(url, URLType):
    """
    startPipeline gives structured policy

    @param URLType: policy or term
    @param url: url of the privacy policy or terms of conditions
    @return: structured policy statement
    """
    unstructuredData = readURL(url, URLType)
    structuredData = createDataStructure(unstructuredData)

    return structuredData


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
