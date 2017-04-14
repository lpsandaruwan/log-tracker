"""
Text file reader
Helper class to read and tail log files as text files though paramiko sftp.

08/04/2017 lpsandaruwan <http://lahiru.site>
"""

import os
import time


class TextStreamReader:

    def __init__(self, sftp_client, text_file):
        self.__sftp_client = sftp_client
        self.__text_file = text_file
        self.__text_stream = None

    def close(self):
        self.__text_stream.close()

    def get_text_stream(self):
        if self.__text_stream is None:
            self.load()

        return self.__text_stream

    def load(self):
        self.__text_stream = self.__sftp_client.open(self.__text_file, "r")

    def tail(self):
        self.__text_stream.seek(os.SEEK_END)

        while True:
            line = self.__text_stream.readline()

            if not line:
                time.sleep(0.01)
                continue

            yield line
