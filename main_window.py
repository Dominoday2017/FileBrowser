import sys
from PyQt5.QtWidgets import QMainWindow, QAction, qApp, QApplication, QFileDialog, QMessageBox
from PyQt5.QtGui import *
from PyQt5 import QtWidgets, uic


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi("main_window.ui", self)

        self.pathBtn.clicked.connect(self.get_path) #binding pathBtn button
        self.searchBtn.clicked.connect(self.get_keywords)

        self.show()

    def get_path(self):
        path = str(QFileDialog.getExistingDirectory(self, "Select directory"))
        self.pathEdit.setText(path)

    def get_keywords(self):
        keywords = str(self.keywordsEdit.text())
        try:
            keywordsList = keywords.split(" ")
        except:
            warning = QMessageBox.warning(None, 'Błąd danych wejściowych', "Upewnij się że oddzieliłeś słowa kluczowe przecinkiem")
        print(keywordsList,keywords)




def main():
    app = QApplication(sys.argv)
    mainWindow = MainWindow()
    sys.exit(app.exec_()) #safe exit from app

if __name__ == "__main__":
    main()
