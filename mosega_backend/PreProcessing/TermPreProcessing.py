from PreProcessing.HTML.Utils import get_written_file_name_from_url, create_data_structure
from PreProcessing.Text.Utils import read_file
from mosega_backend.ConfigHandler import *
import re

# Load configs
configs = ConfigHandler.load_config('config.yaml')

"""
Read policy from URL and returns a string
"""


def read_term(url):
    filename = get_written_file_name_from_url(url, "term")

    base_path_policy_files = configs['termfiles']['abs_path']
    filepath = "%s/%s.txt" % (base_path_policy_files, filename)

    return read_file(filepath, "term")


"""
Prepossessing pipeline
"""


def preprocess_pipeline(url):
    term = read_term(url)
    structured_term = create_data_structure(term)

    return structured_term
