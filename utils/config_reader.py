import yaml

class Config:
    def __init__(self, config_file='config.yaml'):
        with open(config_file, 'r') as file:
            self.config = yaml.safe_load(file)

    def get_base_url(self):
        return self.config.get('base_url', '')

config = Config()
