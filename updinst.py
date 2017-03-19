import sys

from PyQt5.QtCore import Qt, Q_FLAGS
from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QLabel
from PyQt5.QtWidgets import QMainWindow
from PyQt5.QtWidgets import QProgressBar
from PyQt5.QtWidgets import QVBoxLayout
from PyQt5.QtWidgets import QWidget


class QVboxLayout(object):
    pass



def main():

    app = QApplication(sys.argv)

    window = MainWindow(flags=Q_FLAGS())
    window.show()

    exit(app.exec_())


class MainWindow(QMainWindow):

    def __init__(self, flags, *args, **kwargs):
        super().__init__(flags, *args, **kwargs)

        self.setupUi()

    def setupUi(self):
        self.central = QWidget()
        self.layout = QVBoxLayout(self.central)

        self.updating = QLabel("Updating PCS from NULL to NULL")
        self.progressBar = QProgressBar()

        self.progressBar.setMaximumHeight(14)
        self.progressBar.setTextVisible(False)

        self.layout.addWidget(self.updating, alignment=Qt.AlignLeft)
        self.layout.addWidget(self.progressBar,alignment=Qt.AlignVCenter)

        self.setCentralWidget(self.central)


if __name__ == "__main__":
    main()