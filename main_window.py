import datetime
import sys
import time
from file_scanner import DirScanner
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5 import QtWidgets, uic


"""
TODO: comments,
search by title,
add search by sentence,
advanced logger,
window name,
loading bar,
if no txt file in folder show notification,
jak nie ma slowa w pliku to i tak znajduje cos,
otwieranie plikow z list wynikow,
elementy przy anuluj sie usuwaja,
"""


class GetKeywords(QDialog):
    def __init__(self, actualKeywords=[]):
        """
        init previously added keywords if passed and add button functionality
        :param actualKeywords: previously added keywords
        """
        super().__init__()
        uic.loadUi("add_keywords.ui", self)

        self.setFixedSize(410, 300)
        self.keywords = []

        if actualKeywords:
            for el in actualKeywords:
                self.keywordsListWidget.addItem(el)

        self.cancelBtn.clicked.connect(self.close_window)
        self.addBtn.clicked.connect(self.add_keyword)
        self.removeBtn.clicked.connect(self.remove_element)
        self.saveBtn.clicked.connect(self.save_keywords)
        self.clearBtn.clicked.connect(self.clear_elements)

        self.show()

    def add_keyword(self):
        """
        Firstly check if any keywords already exits, if not get text from keywordsEdit and display in keywordsListWidget
        :return: None
        """
        keyword = self.keywordEdit.text()
        wordList = []
        if keyword == "":
            warning = QMessageBox.warning(None, "Błąd danych wejściowych", "Nie można dodawać pustych elementów do listy.")
        elif "," in keyword or ";" in keyword or "." in keyword:
            warning = QMessageBox.warning(None, "Błąd danych wejściowych", "Nie można korzystać z kropek, przecinków i średników")
        else:
            for el in range(self.keywordsListWidget.count()):
                wordList.append(self.keywordsListWidget.item(el).text())

            if keyword in wordList:
                    waring = QMessageBox.warning(None, "Błąd danych wejściowych", "Podany element już się znajduje na liście.")
            else:
                self.keywordsListWidget.addItem(keyword)
                self.keywordEdit.setText("")

    def remove_element(self):
        """
        remove selected item from keywordsListWidget
        :return: None
        """
        item = self.keywordsListWidget.currentRow()
        self.keywordsListWidget.takeItem(item)

    def clear_elements(self):
        self.keywordsListWidget.clear()

    def save_keywords(self):
        """
        Take element (keyword) from keywordsListWidget and add to keywords list
        :return: None
        """
        for el in range(self.keywordsListWidget.count()):
            self.keywords.append(self.keywordsListWidget.item(el).text())

        self.close()

    def close_window(self):
        """
        close window on close button
        :return: None
        """
        self.close()


class LoadWidget(QWidget):
    def __init__(self):
        super().__init__()
        uic.loadUi("loading.ui", self)
        self.show()
        self.movie = QMovie("loading.gif")
        self.loadLbl.setMovie(self.movie)
        self.movie.start()
        time.sleep(2)


class MainWindow(QMainWindow):
    def __init__(self):
        """
        load window ui, add button functionality, init all necessary objects
        """
        super().__init__()
        uic.loadUi("main_window.ui", self)

        self.setFixedSize(610, 530)
        #self.setWindowModality(QtCore.Qt.ApplicationModal)

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
        """
        get path from QFileDialog
        :return: None
        """
        self.path = str(QFileDialog.getExistingDirectory(self, "Select directory"))
        self.pathEdit.setText(self.path)

    def get_keywords(self):
        """

        :return: None
        """
        if self.keywordsEdit.text() != "":
            temp = self.keywordsEdit.text().split(",")
            actualKeywords = [x.replace(" ", "") for x in temp]
            self.getKeywords = GetKeywords(actualKeywords)
        else:
            self.getKeywords = GetKeywords()

        self.setEnabled(False)  # Disable main window
        self.getKeywords.exec()


        if not self.getKeywords.isVisible():
            keywordsStr = ""
            self.keywords = self.getKeywords.keywords

            for el in self.keywords:
                keywordsStr += el + ", "
                #self.keywordsList.append(el)

            keywordsStr = keywordsStr[0:len(keywordsStr)-2]
            self.keywordsEdit.setText(keywordsStr)
            self.setEnabled(True)   # Enable main window

    def file_scanner(self):
        try:
            path = self.pathEdit.text()
            keywordsList = [x.replace(" ", "") for x in self.keywordsEdit.text().split(",")]

            print(path, keywordsList)

            if path != "" and keywordsList[0] != "":    # if path and keywords are added
                #self.movie = QMovie("loading.gif")
                #self.loadWidget = LoadWidget()
                #self.loadWidget.show()

                dirscanner = DirScanner(keywordsList, path)
                results = dirscanner.result

                countRow = int(self.resultBox.currentText())    # Get selected row count by user (1-5)
                self.resultTableWidget.setRowCount(countRow)

                """ Set result table headers view """
                header = self.resultTableWidget.horizontalHeader()
                header.setSectionResizeMode(0, QtWidgets.QHeaderView.Stretch)
                header.setSectionResizeMode(1, QtWidgets.QHeaderView.ResizeToContents)

                """ sort dict with results """
                results = {k: v for k, v in sorted(results.items(), key=lambda item: item[1], reverse=True)}
                tempResult = {}     # temp dict to store result dict
                totalValue = 0      # total result value
                counter = 0

                """ count total result value until counter is lower than expected results count (countRow) """
                for key, value in zip(results.keys(), results.values()):
                    if counter < countRow:
                        tempResult[key] = value
                        counter += 1
                        totalValue += value
                if totalValue == 0:
                    warning = QMessageBox.warning(None, "Błąd", "Nie znaleziono pasującego pliku. Spróbuj z innymi słowami")
                else:
                    results = tempResult
                    counter = 0

                    """ Add results to result table """
                    for path, value in zip(results.keys(), results.values()):
                        self.resultTableWidget.setItem(counter, 0, QTableWidgetItem(path))
                        self.resultTableWidget.setItem(counter, 1, QTableWidgetItem(str(round(value / totalValue * 100, 2)) + "%"))
                        counter += 1
            else:
                warning = QMessageBox.warning(None, "Błąd danych wejściowych", "Ścieżka i słowa kluczowe nie mogą być puste.")
        except:
            warning = QMessageBox.warning(None, "Błąd danych wejściowych", "Niepoprawne dane wejsciowe")
