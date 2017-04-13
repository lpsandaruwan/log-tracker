"""
Text file reader
Helper class to read and tail log files as text files though paramiko sftp.

08/04/2017 lpsandaruwan <http://lahiru.site>
"""


class TextStreamReader:

    def __init__(self, sftp_client, text_file):
        self.__sftp_client = sftp_client
        self.__text_file = text_file
        self.__text_stream = None

    def close(self):
        self.__text_stream.close()

    def get_text_stream(self):
        return self.__text_stream

    def load(self):
        with self.__sftp_client.open(self.__text_file, "r") as text_stream:
            self.__text_stream = text_stream

    def tail(self):
        self.__text_stream.seek(0, 2)
        yield self.__text_stream.readline()
