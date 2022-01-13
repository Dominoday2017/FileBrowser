import sys
from file_scanner import DirScanner
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5 import QtWidgets, uic


"""
TODO: comments
"""


dir_linux = "/home/dominik/Desktop/documents"
dir_windows = "C:/Users/gawla/Desktop/documents"


class GetKeywords(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        uic.loadUi("add_keywords.ui", self)
        self.keywords = []

        self.cancelBtn.clicked.connect(self.close_window)
        self.addBtn.clicked.connect(self.add_keyword)
        self.removeBtn.clicked.connect(self.remove_element)
        self.saveBtn.clicked.connect(self.save_keywords)
        self.show()

    def add_keyword(self):
        keyword = self.keywordEdit.text()
        wordList = []
        if keyword == "":
            warning = QMessageBox.warning(None, "Błąd danych wejściowych", "Nie można dodawać pustych elementów do listy.")
        else:
            for el in range(self.keywordsListWidget.count()):
                wordList.append(self.keywordsListWidget.item(el).text())

            if keyword in wordList:
                    waring = QMessageBox.warning(None, "Błąd danych wejściowych", "Podany element już się znajduje na liście.")
            else:
                self.keywordsListWidget.addItem(keyword)
                self.keywordEdit.setText("")

    def remove_element(self):
        item = self.keywordsListWidget.currentRow()
        self.keywordsListWidget.takeItem(item)

    def save_keywords(self):
        for el in range(self.keywordsListWidget.count()):
            self.keywords.append(self.keywordsListWidget.item(el).text())

        self.close()

    def close_window(self):
        self.close()


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi("main_window.ui", self)

        self.keywordsList = []
        self.path = ""

        self.pathBtn.clicked.connect(self.get_path)
        self.addBtn.clicked.connect(self.get_keywords)
        self.searchBtn.clicked.connect(self.run_dirscanner)

        self.show()

    def get_path(self):
        self.path = str(QFileDialog.getExistingDirectory(self, "Select directory"))
        self.pathEdit.setText(self.path)

    def get_keywords(self):
        self.getKeywords = GetKeywords()
        self.getKeywords.exec_()

        if not self.getKeywords.isVisible():
            keywordsStr = ""
            self.keywords = self.getKeywords.keywords

            for el in self.keywords:
                keywordsStr += el + ", "
                self.keywordsList.append(el)

            keywordsStr = keywordsStr[0:len(keywordsStr)-2]
            self.keywordsEdit.setText(keywordsStr)

    def run_dirscanner(self):
        #keywords = self.keywordsEdit.text()
        path = self.pathEdit.text()

        #print(self.keywordsList, path)
        dirscanner = DirScanner(self.keywordsList, path)
        print(dirscanner.result)
