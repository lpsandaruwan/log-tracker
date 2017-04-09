"""
Log Tracker - main

Track log text files on demand and identify and detect certain string occurring,
exceptions and warnings and report statistics as user requests.


(c) 2017 Lahiru Pathirage <lpsandaruwan@gmail.com>
"""

import threading

import tasks

TASKS = {
    "test": tasks.test_function
}


def main():
    for task in TASKS:
        threading.Thread(target=task).start()


if __name__ == "__main__":
    main()