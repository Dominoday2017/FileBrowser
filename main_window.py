import sys
import dir_scanner
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5 import QtWidgets, uic


"""
TODO: check if keywords already exists
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
        if keyword == "":
            warning = QMessageBox.warning(None, 'Błąd danych wejściowych', "Nie można dodawać pustych elementów do listy.")
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

        self.pathBtn.clicked.connect(self.get_path)
        self.addBtn.clicked.connect(self.get_keywords)

        self.show()

    def get_path(self):
        path = str(QFileDialog.getExistingDirectory(self, "Select directory"))
        self.pathEdit.setText(path)

    def get_keywords(self):
        self.getKeywords = GetKeywords()
        self.getKeywords.exec_()

        if not self.getKeywords.isVisible():
            keywordsStr = ""
            print( keywords := self.getKeywords.keywords)
            for el in keywords:
                keywordsStr += el + ", "

            keywordsStr = keywordsStr[0:len(keywordsStr)-2]
            self.keywordsEdit.setText(keywordsStr)
