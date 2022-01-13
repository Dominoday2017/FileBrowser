import docx
import datetime
import os
import time


"""
TODO: add other file extensions
"""


def log(func):
    """
    function logger
    :param func: function
    :return: function value
    """
    def wrapper(*args, **kwargs):
        value = func(*args, **kwargs)
        with open("logs.txt", "a+") as file:
            now = datetime.datetime.now()
            file.write(f"{now:%Y-%m-%d %H:%M:%S} >> {func.__name__} \n")
        return value
    return wrapper

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
        self.result = {}
        print("Slowa kluczoe dir scanner", keywords)
        self.iter_file()

    #@timer
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
                    self.result = self.result | fileScanner.result
                else:
                    print("No supported file extension")



class FileScanner:
    #@log
    def __init__(self, extension, directory, file, wordList):
        """
        init 4 elements and pass them to pass_path()
        :param extension: extension of file
        :param directory: shorted directory to file
        :param file: name of file with extension
        :param wordList: input word list to find
        """
        self.userWordList = wordList # Init keywords list (only user words)
        self.keywords = [] #final keywords list
        self.result = {}

        self.findSynonyms()
        self.pass_path(extension, directory, file)

    #@log
    def pass_path(self, extension, directory, file):
        """
        pick correct extension and pass full path to method
        :param extension: file extension like: docx, txt
        :param directory: directory to file
        :param file: file name
        :return:
        """
        fullPath = directory + "/" + file

        if extension == "txt":
            txtValue = self.read_txt(fullPath)
            self.result[file] = txtValue
        elif extension == "docx":
            docxValue = self.read_docx(fullPath)
            self.result[file] = docxValue


    #@log
    def findSynonyms(self):
        """
        find all synonyms from word list and return them
        :return: list with all synonyms
        """
        for wordStatic in self.userWordList:
            self.keywords.append(wordStatic)

        with open("words.txt", "r", encoding="utf8") as words:
            words = list(words)
            for line in words:
                for word in self.userWordList:
                    if word + "," in line:
                        line = line.replace(" ", "")
                        line = line.replace("\n", "")
                        line = line.split(",")
                        if word in line:
                            self.keywords.append(line)
                            if [word] not in self.keywords:
                                self.keywords.append([word])
                        else:
                            if [word] not in self.keywords:
                                self.keywords.append([word])

        #print(self.keywords)

    #@log
    def read_txt(self, path):
        """
        open file and read line by line. If word in wordList is in line, increase counter by one
        :param path: full path of file
        :return: number of words in file
        """
        counter = 0
        #print("read text")
        with open(path, "r") as file:
            for line in file:
                for word_list in self.keywords:
                    for word in word_list:
                        if word.lower() in line.lower():
                            counter += 1
        return counter

    #@log
    def read_docx(self, path):
        """
        open file and read line by line. If word in wordList is in line, increase counter by one
        :return: number of words in file
        """
        doc = docx.Document(path)
        allParas = doc.paragraphs
        counter = 0

        for para in allParas:                           # Read all paragraphs from text
            for word_list in self.keywords:             # Iterate lists in list ([["jajko", "musztarda"], ["kapusta", "pomidor"]]
                for word in word_list:                  # Iterate all words in list of word_list
                    if word in str(para.text).lower():  # If word is in paragraph
                        counter += 1
        return counter

# Example

#words = ["jajko", "mielonka", "rozwój", "produkowana"]
#test = DirScanner(words, "C:/Users/gawla/Desktop/documents")
