from file_scanner import FileScanner
import os

"""
TODO: add full path to file and pass to file_scanner
"""

# temp dir
dir_linux = "/home/dominik/Desktop/Huawei"
dir_windows = "C:/Users/gawla/Desktop/documents"

# read all files in dir and pass them to file_sanner
for file in os.listdir(dir_windows):
    ext = file.split(".")[1]
    if ext in ["docx", "doc", "txt"]:
        fileScanner = FileScanner(ext)
    else:
        print("No supported file format")
