from PreProcessing.HTML.Utils import getFileName
from PreProcessing.CreateDataStracure import create_data_structure
from PreProcessing.Text.Utils import readFile
import os
import Shared.SharedFunctions as functions

configs = functions.loadConfigs()


def readURL(url, URLType):
    """
    Fetch data from given URL -> clean HTML elements -> save content to temporary txt file ->
    read from temporary file -> remove temporary file

    @param URLType: policy or term
    @param url: page URL
    @return: cleaned content form given URL
    """

    name = getFileName(url, URLType)
    path = ""
    if URLType == "policy":
        path = configs['policyFiles']['path']
    elif URLType == "term":
        path = configs['termFiles']['path']
    filePath = path + "/" + name + ".txt"
    file = readFile(filePath, URLType)
    os.remove(filePath)
    return file


def startPipeline(url, URLType):
    """
    startPipeline gives structured policy

    @param URLType: policy or term
    @param url: url of the privacy policy or terms of conditions
    @return: structured policy statement
    """
    policy = readURL(url, URLType)
    structuredPolicy = create_data_structure(policy)

    return structuredPolicy


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
