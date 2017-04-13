"""
Log Tracker - main

Track log text files on demand and identify and detect certain string occurring,
exceptions and warnings and report statistics as user requests.


(c) 2017 Lahiru Pathirage <lpsandaruwan@gmail.com>
"""

import threading
import time

from helper import Configurer
from helper import ResourceCollector
from task_list import TASKS
from utility import TextStreamReader
from utility import YamlCrud


def main():
    try:
        # read app settings from config.yaml file
        __ltrk_settings = YamlCrud("./config.yml").load("r")

        # gather yaml resource files
        __resources = ResourceCollector(__ltrk_settings["resource_path"]).collect_yaml_files()

        # create configurer object pool
        __text_stream_list = {}

        for __resource in __resources:
            __text_stream_list[__resource["name"]] = TextStreamReader(
                Configurer(__resource).get_sftp_connection(),
                __resource["log"]
            )

        # create ssh connections and run tasks in background
        for key, __text_stream in __text_stream_list:
            # run appropriate function in background
            threading.Thread(target=TASKS[key], args=(__text_stream))

        for key, task in TASKS.items():
            threading.Thread(target=task)

        while True:
            time.sleep(99999)

    except KeyboardInterrupt:
        print("Exiting log tracker...")



if __name__ == "__main__":
    main()
