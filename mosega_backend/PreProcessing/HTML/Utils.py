import requests
import os
import io
import re
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


def get_cleaned_content_from_url(url):
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
Function to write given policies / terms to a file
"""


def write_to_file(name, content, url_type):
    base_file_path = ""

    if url_type == "policy":
        base_file_path = configs['policyfiles']['abs_path']
    elif url_type == "term":
        base_file_path = configs['termfiles']['abs_path']

    filename = "%s/%s.txt" % (base_file_path, name)

    with io.open(filename, mode="w", encoding="utf-8") as f:
        try:
            f.write(content)

            msg = "file wrote successfully"
            logger.info(msg)
        except:

            msg = "Error while writing file"
            logger.info(msg)


"""
Function to get policy/ term from URL => write a file and return the file name
"""


def get_written_file_name_from_url(html_url, url_type):
    filename, content = get_cleaned_content_from_url(html_url)
    write_to_file(filename, content, url_type)

    return filename


"""
Function to create data structure
"""


def create_data_structure(unstructured_string):
    lines = unstructured_string.split("\n")
    patten = re.compile("#")

    data_structure = {}

    heading_list = list(filter(patten.match, lines))
    no_of_headings = len(heading_list)

    no_of_hash_list = [0] * no_of_headings
    heading_start_index = [0] * no_of_headings
    heading_end_index = [0] * no_of_headings

    for i in range(no_of_headings):
        no_of_hash_list[i] = heading_list[i].count('#')
        heading_start_index[i] = lines.index(heading_list[i])

        normalize = no_of_hash_list[i] - no_of_hash_list[0] + 1
        if normalize < 0:
            no_of_hash_list[i] = 0
        else:
            no_of_hash_list[i] = normalize

    for i in range(no_of_headings - 1):
        heading_end_index[i] = heading_start_index[i + 1] - 1

    heading_end_index[-1] = len(lines) - 1

    # TODO : Need to improve with nested levels

    data_structure['heading'] = heading_list[0][heading_list[0].count('#'):].strip()
    data_structure['text'] = ''.join(lines[heading_start_index[0] + 1:heading_end_index[0]])
    data_structure['content'] = []

    for i in range(1, no_of_headings):
        temp = {'heading': heading_list[i][heading_list[i].count('#'):].strip(),
                'text': ''.join(lines[heading_start_index[i] + 1:heading_end_index[i]]),
                'content': []}
        data_structure['content'].append(temp)

    return data_structure
