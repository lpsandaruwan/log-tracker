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

    def connect_using_private_key(self, **kwargs):
        self.__connector.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        self.__connector.connect(
            hostname=kwargs["hostname"],
            username=kwargs["username"],
            pkey=kwargs["private_key"]
        )

    def connect_using_user_password(self, **kwargs):
        self.__connector.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        self.__connector.connect(
            hostname=kwargs["hostname"],
            username=kwargs["username"],
            password=kwargs["password"]
        )

    # create SFTP connection
    def open_sftp_connection(self):
        self.__sftp_client = self.__connector.open_sftp()

    def get_connector(self):
        return self.__connector

    def get_sftp_client(self):
        return self.__sftp_client
