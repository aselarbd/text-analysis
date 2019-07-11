import yaml


# Configuration handler class

class ConfigHandler:

    @staticmethod
    def load_config(config_file):
        with open(config_file, 'r') as stream:
            try:
                return yaml.safe_load(stream)
            except yaml.YAMLError as exc:
                print(exc)
