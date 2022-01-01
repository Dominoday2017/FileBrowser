#import file_scanner
import os

dir_linux = "/home/dominik/Desktop/Huawei"
dir_windows = "C:/Users/gawla/Desktop/documents"

for file in os.listdir(dir_windows):
    if file.endswith(".txt"):
        print("txt \n")
        #file_scanner.read_txt()
    elif file.endswith(".docx"):
        print("doxc \n")
        #file_scanner.read_doxc()
    elif file.endswith(".doc"):
        print("doc \n")
    elif file.endswith(".odt"):
        print("odt \n")
