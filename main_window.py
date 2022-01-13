import sys
from file_scanner import DirScanner
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5 import QtWidgets, uic


"""
TODO: comments, empty values after search
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
        self.searchBtn.clicked.connect(self.file_scanner)

        self.resultTableWidget.setRowCount(int(self.resultBox.currentText()))
        header = self.resultTableWidget.horizontalHeader()
        header.setSectionResizeMode(0, QtWidgets.QHeaderView.Stretch)
        header.setSectionResizeMode(1, QtWidgets.QHeaderView.Stretch)

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

    def file_scanner(self):
        path = self.pathEdit.text()
        dirscanner = DirScanner(self.keywordsList, path)
        results = dirscanner.result

        countRow = int(self.resultBox.currentText())
        self.resultTableWidget.setRowCount(countRow)
        header = self.resultTableWidget.horizontalHeader()
        header.setSectionResizeMode(0, QtWidgets.QHeaderView.Stretch)
        header.setSectionResizeMode(1, QtWidgets.QHeaderView.ResizeToContents)

        #results = {'Chronologia ważniejszych faktów dot.docx': 25, 'Nowy Dokument tekstowy (2).txt': 15, 'Nowy Dokument tekstowy.txt': 5, "cos.txt" : 0}

        results = {k: v for k, v in sorted(results.items(), key=lambda item: item[1], reverse=True)}

        tempResult = {}
        totalValue = 0
        counter = 0

        for key, value in zip(results.keys(), results.values()):
            if counter < countRow:
                tempResult[key] = value
                counter += 1
                totalValue += value

        results = tempResult
        counter = 0
        for path, value in zip(results.keys(), results.values()):
            self.resultTableWidget.setItem(counter, 0, QTableWidgetItem(path))
            self.resultTableWidget.setItem(counter, 1, QTableWidgetItem(str(round(value / totalValue * 100, 2)) + "%"))
            counter += 1
