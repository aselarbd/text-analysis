import requests
import os
import io
from bs4 import BeautifulSoup
import html2text
from lxml.html.clean import Cleaner
from urllib.parse import urlparse
import logging
from mosega_backend.ConfigHandler import *

# Load configs
configs = ConfigHandler.load_config('config.yaml')

# Logger
logger = logging.getLogger(__name__)
log_file_path = configs['logging']['abs_path']
log_level = configs['logging']['level']
log_format = configs['logging']['format']

logging.basicConfig(filename=os.path.abspath(log_file_path), level=logging.INFO, format=log_format)

"""
Function to extract privacy policies from given URL 
"""


def get_policy_from_url(url):
    response = requests.get(url)
    response.encoding = 'utf-8'

    name = urlparse(response.request.url).hostname.split(".")[1]

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

    soup = BeautifulSoup(cleaned_html_page)

    # Isolate body
    body = soup.body

    text_maker = html2text.HTML2Text()
    text_maker.ignore_links = True
    text_maker.ignore_images = True
    text_maker.drop_white_space = True

    formatted_text = html2text.html2text(body.prettify())

    msg = "HTML file cleaned"
    logger.info(msg)

    return name, formatted_text


"""
Function to write given policies to a file
"""


def write_policy_to_file(name, policy_to_write):
    base_path_policy_files = configs['policyfiles']['abs_path']
    filename = "%s/%s.txt" % (base_path_policy_files, name)

    with io.open(filename, mode="w", encoding="utf-8") as f:
        try:
            f.write(policy_to_write)

            msg = "file wrote successfully"
            logger.info(msg)
        except:

            msg = "Error while writing file"
            logger.info(msg)


"""
Function to get policy from URL => write a file and return the file name
"""


def get_file_of_policy_from_url(html_url):
    filename, policy_string = get_policy_from_url(html_url)
    write_policy_to_file(filename, policy_string)

    return filename
