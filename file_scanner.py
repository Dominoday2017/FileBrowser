import docx
import datetime


"""
TODO: add other file extensions,
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


class FileScanner:
    @log
    def __init__(self, extension, directory, file, wordList):
        """
        init 4 elements and pass them to pass_path()
        :param extension: extension of file
        :param directory: shorted directory to file
        :param file: name of file with extension
        :param wordList: input word list to find
        """
        self.userWordList = wordList
        self.keywords = [] #final

        self.findSynonyms()
        self.pass_path(extension, directory, file)

    @log
    def pass_path(self, extension, directory, file):
        """
        pick correct extension and pass full path to method
        :param extension: file extension like: docx, txt
        :param directory: directory to file
        :param file: file name
        :return:
        """
        fullPath = directory + "/" + file

        print(extension)
        if extension == ".txt":
            txtValue = self.read_txt(fullPath)
            print(txtValue)
        elif extension == ".docx":
            docxValue = self.read_docx(fullPath)
            print(docxValue)

    @log
    def findSynonyms(self):
        """
        find all synonyms from word list and return them
        :return: list with all synonyms
        """

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

    @log
    def read_txt(self, path):
        """
        open file and read line by line. If word in wordList is in line, increase counter by one
        :param path: full path of file
        :return: number of words in file
        """
        counter = 0

        with open(path, "r") as file:
            for line in file:
                for word_list in self.keywords:
                    for word in word_list:
                        if word.lower() in line.lower():
                            counter += 1
        return counter

    @log
    def read_docx(self, path):
        """
        open file and read line by line. If word in wordList is in line, increase counter by one
        :return: number of words in file
        """
        import os
        print(os.path.abspath(path))

        doc = docx.Document(path)
        allParas = doc.paragraphs
        counter = 0

        for para in allParas:
            for word_list in self.keywords:
                for word in word_list:
                    if word in str(para.text).lower():
                        counter += 1

        print(counter)
        return counter

test = FileScanner(".docx", "C:/Users/gawla/Desktop/documents", "List.docx", "życzenia")
