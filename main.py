from PyQt5.QtWidgets import QApplication
import sys
import main_window


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = main_window.MainWindow()
    sys.exit(app.exec_())
