import sys
from PyQt5.QtWidgets import QMainWindow, QAction, qApp, QApplication, QFileDialog
from PyQt5.QtGui import QIcon
from PyQt5 import QtWidgets, uic


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi("main_window.ui", self)
        self.show()

def main():
    app = QApplication(sys.argv)
    mainWindow = MainWindow()
    sys.exit(app.exec_()) #safe exit from app

if __name__ == "__main__":
    main()
