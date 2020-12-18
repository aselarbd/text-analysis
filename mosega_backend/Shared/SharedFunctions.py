import Shared.constants as constants
from Handlers.Config.ConfigHandler import *

DEBUG = constants.DEBUG


def load_configs():
    """
    Load config based on the mode
    """
    return load_yaml('config.yaml')


def load_identification_terms():
    """
        Load identification terms based on the mode
        """
    return load_yaml('IdentificationTerms.yaml')


def load_yaml(file_name):
    """
        Load yaml file based on the mode
        """
    if DEBUG:
        yaml_file = ConfigHandler.load_config('../' + file_name)
    else:
        yaml_file = ConfigHandler.load_config(file_name)
    return yaml_file


def generate_cache(cache_ref, database_ref):
    if cache_ref.is_empty():
        items = database_ref.get_all()
        cache_ref.init_cache_without_corpus(items=items)
