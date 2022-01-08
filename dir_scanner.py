from file_scanner import FileScanner
import os
import time
import datetime


"""
TODO:
"""


def timer(func):
    """
    Function worktime counter
    :param func: function to run and check worktime
    :return:
    """
    def wrapper(*args, **kwargs):
        before = time.time()
        v = func(*args, **kwargs)
        workTime = time.time() - before
        with open("timer_logs", "a+") as file:
            file.write(f"{datetime.datetime.now():%Y-%m-%d %H:%M:%S} >> Work time: {workTime} \n")
        return v

    return wrapper


class DirScanner:
    def __init__(self, keywords, directory):
        self.keywords = keywords
        self.directory = directory

    @timer
    def iter_file(self):
        """
        read all files in dir and pass them to file_scanner
        :return:
        """
        for file in os.listdir(self.directory):
            if "." not in file:
                print("No supported file format")
            else:
                extension = file.split(".")[1]
                if extension in ["docx", "doc", "txt"]:
                    fileScanner = FileScanner(extension, self.directory, file, self.keywords)
                else:
                    print("No supported file format")
