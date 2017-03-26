import subprocess
import sys
import time

import depresolv

def main():

    launcher = depresolv.launch_main(["PyQt5", "demjson", "bs4", "lxml", "requests"])

    if launcher is depresolv.ALL_SATISFIED:

        flag = open("installed", "wb+")
        flag.close()

        from ui.MainWindow import MainWindow
        from PyQt5.QtCore import Q_FLAGS
        from PyQt5.QtWidgets import QApplication

        app = QApplication(sys.argv)
        window = MainWindow(app, flags=Q_FLAGS())
        window.show()
        exit(app.exec_())

    elif launcher is depresolv.INSTALLED_AND_SATISFIED:

        subprocess.Popen([sys.executable, sys.argv])
        exit(0)

    elif launcher is depresolv.INSTALL_FAILED:
        print("Some dependencies failed to install! Please report this!")

        # Prevent CMD window from closing
        while True:
            time.sleep(1)


if __name__=="__main__":
    main()

