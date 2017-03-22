from sys import argv
import depresolv

def main():

    try:
        depresolv.launch_main(["PyQt5", "demjson", "bs4", "lxml", "requests"])
    except depresolv.DepresolvMain:

        from ui.MainWindow import MainWindow
        from PyQt5.QtCore import Q_FLAGS
        from PyQt5.QtWidgets import QApplication

        app = QApplication(argv)
        window = MainWindow(app, flags=Q_FLAGS())
        window.show()
        exit(app.exec_())

    except depresolv.DepresolvFailed as e:
        print(str(e))

if __name__=="__main__":
    main()

