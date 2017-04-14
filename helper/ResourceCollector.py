"""
Resource collector
Collect yaml resources from resource directory.

09/04/2017 lpsandaruwan <http://lahiru.site>
"""

import os


class ResourceCollector:

    def __init__(self, resource_directory):
        self.__resource_directory = resource_directory
        self.__resource_files = []

    def collect_yaml_files(self):
        for dir_path, _, file_names in os.walk(self.__resource_directory):
            for file_name in file_names:
                if file_name.endswith(".yml"):
                    self.__resource_files.append(
                        os.path.abspath(os.path.join(dir_path, file_name))
                    )

        return self.get_resource_files_list()

    def get_resource_files_list(self):
        return self.__resource_files
