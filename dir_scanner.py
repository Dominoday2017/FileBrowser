from file_scanner import FileScanner
import os
import time
import datetime

"""
TODO: change script to OOP
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
        now = time.time() - before
        with open("timer_logs", "a+") as file:
            file.write(f"{datetime.datetime.now():%Y-%m-%d %H:%M:%S} >> Work time: {now} \n")
        return v

    return wrapper


""" temp dir and word list """
dir_linux = "/home/dominik/Desktop/documents"
dir_windows = "C:/Users/gawla/Desktop/documents"
wordList = ["dominik", "sylwester"]


@timer
def iter_file():
    """
    read all files in dir and pass them to file_scanner
    :return:
    """
    for file in os.listdir(dir_linux):
        if "." not in file:
            print("No supported file format")
        else:
            extension = file.split(".")[1]
            if extension in ["docx", "doc", "txt"]:
                fileScanner = FileScanner(extension, dir_linux, file, wordList)
            else:
                print("No supported file format")


iter_file()
