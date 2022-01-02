"""
TODO: add other file extensions,
      get full path to file and pass to specific function
"""


class FileScanner:
    def __init__(self, extension):
        self.extension = extension
        self.getExt(self.extension)

    def getExt(self, extension):
        if extension == "txt":
            self.read_txt()
        elif extension == "docx":
            self.read_docx()

    def read_txt(self):
        """
        open txt and read word by word
        :return:
        """
        print("txt")

        return "txt"

    def read_docx(self):
        """
        open docx, format to string and read word by word
        :return:
        """
        print("docx")
        return "docx"
