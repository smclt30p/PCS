import sys

from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QMainWindow
from PyQt5.QtWidgets import QProgressBar
from PyQt5.QtWidgets import QVBoxLayout
from PyQt5.QtWidgets import QWidget


class QVboxLayout(object):
    pass


def main():

    app = QApplication(sys.argv)

    window = QMainWindow()

    layout = QVBoxLayout()


    progressBar = QProgressBar()

    layout.addWidget(progressBar, alignment=Qt.AlignVCenter)

    window.setLayout(layout)


    window.show()

    exit(app.exec_())

if __name__ == "__main__":
    main()