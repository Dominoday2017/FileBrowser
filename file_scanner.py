"""
TODO: add other file extensions
"""


class FileScanner:
    def __init__(self, extension, directory, file, wordList):
        """
        init 3 elements and pass them to pass_path()
        :param extension: extension of file
        :param directory: shorted directory to file
        :param file: name of file with extension
        """
        self.wordList = wordList

        self.pass_path(extension, directory, file)

    def pass_path(self, extension, directory, file):
        """ pick correct extension and pass full path to method """
        fullPath = directory + "/" + file
        if extension == "txt":
            self.read_txt(fullPath)
        elif extension == "docx":
            self.read_docx(fullPath)

    def read_txt(self, path):
        """
        get path, open file and read line by line. If word in wordList is in line, increase counter by one
        :param path: full path of file
        :return:
        """
        counter = 0

        with open(path, "r") as file:
            for line in file:
                for word in self.wordList:
                    if word in line:
                        counter += 1

        print(counter)

    def read_docx(self, path):
        """
        open docx, format to string and read word by word
        :return:
        """
        print(path)
        return "docx"
