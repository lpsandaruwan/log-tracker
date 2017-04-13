"""
Configurer
Read and validate settings from user provided yaml files.

09/04/2017 lpsandaruwan <http://lahiru.site>
"""

from utility import SSHConnector
from utility import YamlCrud


class Configurer:

    def __init__(self, yaml_file):
        self.__settings = None
        self.__ssh_connection = SSHConnector()
        self.__yaml_file = yaml_file

    def create_ssh_connection(self):
        try:
            if self.__settings[
                "name"
            ] is not None and self.__settings[
                "hostname"
            ] is not None and self.__settings[
                "username"
            ] is not None:
                if self.__settings["key_file"] is not None:
                    self.__ssh_connection.connect_using_key_file(
                        hostname=self.__settings["hostname"],
                        username=self.__settings["username"],
                        key_file=self.__settings["key_file"]
                    )
                elif self.__settings["private_key"] is not None:
                    self.__ssh_connection.connect_using_private_key(
                        hostname=self.__settings["hostname"],
                        username=self.__settings["username"],
                        private_key=self.__settings["private_key"]
                    )
                elif self.__settings["password"] is not None:
                    self.__ssh_connection.connect_using_user_password(
                        hostname=self.__settings["hostname"],
                        username=self.__settings["username"],
                        password=self.__settings["password"]
                    )
                else:
                    return None

                self.__ssh_connection.open_sftp_connection()

        except:
            print("invalid data has been provided on YAML resource")
            return None

    def get_sftp_connection(self):
        if self.__settings is None:
            self.load()

        if self.__ssh_connection.get_sftp_client() is None:
            self.create_ssh_connection()

        return self.__ssh_connection.get_sftp_client()

    def load(self):
        yaml_object = YamlCrud(self.__yaml_file)
        yaml_object.load("r")
        self.__settings = yaml_object.get_yaml_data()
