from PreProcessing.HTML.Utils import get_written_file_name_from_url, create_data_structure
from PreProcessing.Text.Utils import read_file
from mosega_backend.ConfigHandler import *
import re

# Load configs
configs = ConfigHandler.load_config('config.yaml')

# PreProcessing Testing
# configs = ConfigHandler.load_config('../config.yaml')

"""
Read policy from URL and returns a string
"""


def read_policy(url):
    filename = get_written_file_name_from_url(url, "policy")

    base_path_policy_files = configs['policyfiles']['path']
    filepath = "%s/%s.txt" % (base_path_policy_files, filename)

    return read_file(filepath, "policy")


"""
Prepossessing pipeline
"""


def preprocess_pipeline(url):
    policy = read_policy(url)
    structured_policy = create_data_structure(policy)

    return structured_policy
