import file_scanner
import os

dir = "/home/dominik/Desktop/Huawei"

for file in os.listdir(dir):
    #if ext is == x then fun
    if file.endswith(".txt"):
        file_scanner.read_txt()
    elif file.endswith(".docx"):
        file_scanner.read_doxc()