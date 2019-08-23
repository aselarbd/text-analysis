from PreProcessing.HTML.Utils import get_file_of_policy_from_url
from PreProcessing.Text.Utils import read_file
from mosega_backend.ConfigHandler import *
import re

# Load configs
configs = ConfigHandler.load_config('../config.yaml')


def read_policy(url):
    filename = get_file_of_policy_from_url(url)

    base_path_policy_files = configs['policyfiles']['abs_path']
    filepath = "%s/%s.txt" % (base_path_policy_files, filename)

    return read_file(filepath)


def create_data_structure(policy):
    words = policy.split("\n")
    print(words)


