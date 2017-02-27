from sys import argv

from PyQt5.QtCore import Q_FLAGS
from PyQt5.QtWidgets import QApplication

from ui.MainWindow import MainWindow


def main():
    try:
        app = QApplication(argv)
        window = MainWindow(flags=Q_FLAGS())
        window.show()
        exit(app.exec_())
    except BaseException as e:
        print(str(e))

if __name__=="__main__":
    main()

