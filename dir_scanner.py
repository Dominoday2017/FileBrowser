from file_scanner import FileScanner
import os

"""
TODO:
"""

# temp dir
dir_linux = "/home/dominik/Desktop/documents/"
dir_windows = "C:/Users/gawla/Desktop/documents"
wordList = ["jajko", "szynka", "mielonka"]

# read all files in dir and pass them to file_scanner
for file in os.listdir(dir_linux):
    if "." not in file:
        print("No supported file format")
    else:
        extension = file.split(".")[1]
        if extension in ["docx", "doc", "txt"]:
            fileScanner = FileScanner(extension, dir_linux, file, wordList)
        else:
            print("No supported file format")
