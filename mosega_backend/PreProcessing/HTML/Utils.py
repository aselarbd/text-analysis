import requests
import io
import re
import os
from bs4 import BeautifulSoup
import html2text
from lxml.html.clean import Cleaner
import logging
import Shared.SharedFunctions as functions
import Shared.LogSetup as logSetup


configs = functions.loadConfigs()
logSetup.setupLog()

LOGGER = logging.getLogger(__name__)


def cleanTags(url):
    """
    Clean HTML Tags of given URL

    @param url: URL that object contains
    @return: formatted text of URL
    """
    response = requests.get(url)
    response.encoding = 'utf-8'

    # Clean HTML page
    cleaner = Cleaner()
    cleaner.javascript = True
    cleaner.style = True
    cleaner.inline_style = True
    cleaner.comments = True
    cleaner.meta = True
    cleaner.forms = True
    cleaner.embedded = True
    cleaner.frames = True
    cleaner.remove_tags = ['div']
    cleaner.kill_tags = ['footer', 'header', 'navigation', 'title', 'nav', 'img', 'noscript', 'svg', 'ellipse']

    cleaned_html_page = cleaner.clean_html(response.text)

    soup = BeautifulSoup(cleaned_html_page, features="lxml")

    # Isolate body
    body = soup.body

    textMaker = html2text.HTML2Text()
    textMaker.ignore_links = True
    textMaker.ignore_images = True
    textMaker.drop_white_space = True

    formattedText = html2text.html2text(body.prettify())

    formattedText = re.sub('[*][*]$', "", formattedText)
    formattedText = re.sub('^[*][*]\d[\\][.]', "## ", formattedText)
    formattedText = re.sub('^[*]\d[\\][.]', "## ", formattedText)
    formattedText = re.sub('[1-9].[1-9].', "## ", formattedText)
    formattedText = re.sub('[1-9].', "# ", formattedText)
    formattedText = re.sub('[(]\S[)]', "## ", formattedText)
    formattedText = re.sub('^[-]', "## ", formattedText)
    formattedText = re.sub('^[*][*]', "## ", formattedText)
    formattedText = re.sub('^[*][*]\D[.][*][*]', "## ", formattedText)
    formattedText = re.sub('[*]\s[\d][\\][.]', "## ", formattedText)

    LOGGER.debug("HTML file cleaned : "+url)

    return formattedText


def createFile(content, fileType):
    """
    write given content to given file

    @param content: content of given file
    @param fileType: file type policy or terms
    """
    path = ""

    if fileType == "policy":
        path = configs['policyFiles']['path']
    elif fileType == "term":
        path = configs['termFiles']['path']

    filePath = os.getcwd()+"/"+path

    with io.open(filePath, mode="w+", encoding="utf-8") as f:
        try:
            f.write(content)
            LOGGER.debug("cleaned HTML was wrote a file")
        except IOError:
            LOGGER.debug("Error while writing the cleaned HTML to a file")


def generateFile(url, fileType):
    """
    given url is formatted by removing HTML tags and saved to a file  and return saved file name

    @param url: URL that need to retrieve data
    @param fileType: type of file policy or term
    """
    content = cleanTags(url)
    createFile(content, fileType)
