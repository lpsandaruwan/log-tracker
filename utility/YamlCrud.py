"""
YAML CRUD operations
Helper class to manipulate YAML files.

08/04/2017 lpsandaruwan <http://lahiru.site>
"""

import yaml


class YamlCrud:

    def __init__(self, yaml_file):
        self.__yaml_file = yaml_file
        self.__yaml_data = None

    def get_yaml_data(self):
        return self.__yaml_data

    def set_yaml_data(self, yaml_data):
        self.__yaml_data = yaml_data

    def set_yaml_file(self, yaml_file):
        self.__yaml_file = yaml_file

    def load(self, mode):
        with open(self.__yaml_file, mode) as text_stream:
            try:
                self.__yaml_data = yaml.load(text_stream)
            except yaml.YAMLError as ex:
                print(ex.message)

    def save_data(self):
        yaml.dump(self.__yaml_data, self.__yaml_file, default_flow_style=True)
