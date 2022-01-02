import docx

"""
TODO: add other file extensions,
      edit method comments,
      lower text
"""

class FileScanner:
    def __init__(self, extension, directory, file, wordList):
        """
        init 3 elements and pass them to pass_path()
        :param extension: extension of file
        :param directory: shorted directory to file
        :param file: name of file with extension
        """
        self.userWordList = wordList
        self.findSynonyms()

        #self.pass_path(extension, directory, file)

    def pass_path(self, extension, directory, file):
        """ pick correct extension and pass full path to method """
        fullPath = directory + "/" + file
        print(fullPath)
        if extension == "txt":
            self.read_txt(fullPath)
        elif extension == "docx":
            self.read_docx(fullPath)

    def findSynonyms(self):
        self.wordList = []

        with open("words.txt", "r") as words:
            words = list(words)
            for line in words:
                for word in self.userWordList:
                    if word + "," in line:
                        line = line.replace(" ", "")
                        line = line.replace("\n", "")
                        line = line.split(",")
                        if word in line:
                            self.wordList.append(line)
        print(self.wordList)


    def read_txt(self, path):
        """
        get path, open file and read line by line. If word in wordList is in line, increase counter by one
        :param path: full path of file
        :return:
        """
        counter = 0

        with open(path, "r") as file:
            for line in file:
                for word in self.userWordList:
                    if word in line:
                        counter += 1

        #print(counter)

    def read_docx(self, path):
        """
        open docx, format to string and read word by word
        :return:
        """
        doc = docx.Document(path)
        allParas = doc.paragraphs
        counter = 0

        for para in allParas:
            for word in self.userWordList:
                if word in str(para.text):
                    counter += 1

        print(counter)

