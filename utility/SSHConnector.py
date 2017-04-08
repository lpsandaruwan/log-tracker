"""
SSH connector
Create SSH connections using paramiko.

08/04/2017 lpsandaruwan <http://lahiru.site>
"""

import paramiko


class SSHConnector:

    def __init__(self):
        self.__connector = paramiko.SSHClient()
        self.__sftp_client = None
        self.__options = {
            0: self.connect_using_key_file,
            1: self.connect_using_private_key,
            2: self.connect_using_user_password
        }

    # close SSH connection
    def close_connection(self):
        self.__connector.close()

    def connect_using_key_file(self, **kwargs):
        self.__connector.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        self.__connector.connect(
            hostname=kwargs["hostname"],
            username=kwargs["username"],
            key_filename=kwargs["key_file"]
        )

    def connect_using_user_password(self, **kwargs):
        self.__connector.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        self.__connector.connect(
            hostname=kwargs["hostname"],
            username=kwargs["username"],
            password=kwargs["password"]
        )

    def connect_using_private_key(self, **kwargs):
        self.__connector.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        self.__connector.connect(
            hostname=kwargs["hostname"],
            username=kwargs["username"],
            pkey=kwargs["private_key"]
        )

    # create SFTP connection
    def open_sftp_connection(self):
        self.__sftp_client = self.__connector.open_sftp()

    # open connection using mode index, for mode index refer self.__options
    def open_ssh_connection(self, mode, **kwargs):
        self.__options[mode](kwargs)

    def get_connector(self):
        return self.__connector

    def get_sftp_client(self):
        return self.__sftp_client
