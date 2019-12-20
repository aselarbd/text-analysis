import Shared.constants as constants
from mosega_backend.ConfigHandler import *

DEBUG = constants.DEBUG


def loadConfigs():
    """
    Load config based on the mode
    @return: configs
    """
    return loadYaml('config.yaml')


def loadIdentificationTerms():
    """
        Load identification terms based on the mode
        @return: configs
        """
    return loadYaml('IdentificationTerms.yaml')


def loadYaml(fileName):
    """
        Load yaml file based on the mode
        @return: yaml file
        """
    if DEBUG:
        yamlFile = ConfigHandler.load_config('../' + fileName)
    else:
        yamlFile = ConfigHandler.load_config(fileName)
    return yamlFile
