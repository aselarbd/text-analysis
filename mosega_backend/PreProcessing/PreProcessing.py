from PreProcessing.HTML.Utils import get_file_of_policy_from_url
from PreProcessing.Text.Utils import read_file
from mosega_backend.ConfigHandler import *
import re

# Load configs
configs = ConfigHandler.load_config('config.yaml')

"""
Read policy from URL and returns a string
"""


def read_policy(url):
    filename = get_file_of_policy_from_url(url)

    base_path_policy_files = configs['policyfiles']['abs_path']
    filepath = "%s/%s.txt" % (base_path_policy_files, filename)

    return read_file(filepath)


"""
Get string of policy and return a structured policy 
"""


def create_data_structure(policy):
    lines = policy.split("\n")
    patten = re.compile("#")

    structured_policy = {}

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

    structured_policy['heading'] = heading_list[0][heading_list[0].count('#'):].strip()
    structured_policy['text'] = ''.join(lines[heading_start_index[0] + 1:heading_end_index[0]])
    structured_policy['content'] = []

    for i in range(1, no_of_headings):
        temp = {'heading': heading_list[i][heading_list[i].count('#'):].strip(),
                'text': ''.join(lines[heading_start_index[i] + 1:heading_end_index[i]]),
                'content': []}
        structured_policy['content'].append(temp)

    return structured_policy


"""
Prepossessing pipeline
"""


def preprocess_pipeline(url):
    policy = read_policy(url)
    structured_policy = create_data_structure(policy)

    return structured_policy
