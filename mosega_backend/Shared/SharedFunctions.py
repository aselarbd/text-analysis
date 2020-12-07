import Shared.constants as constants
from Handlers.Config.ConfigHandler import *

DEBUG = constants.DEBUG


def loadConfigs():
    """
    Load config based on the mode
    """
    return loadYaml('config.yaml')


def loadIdentificationTerms():
    """
        Load identification terms based on the mode
        """
    return loadYaml('IdentificationTerms.yaml')


def loadYaml(fileName):
    """
        Load yaml file based on the mode
        """
    if DEBUG:
        yamlFile = ConfigHandler.load_config('../' + fileName)
    else:
        yamlFile = ConfigHandler.load_config(fileName)
    return yamlFile
