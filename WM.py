import sys
from PyQt5.uic import loadUi
from PyQt5.QtWidgets import QMainWindow, QApplication


class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()

        loadUi('MainWindow.ui', self)



if __name__=="__main__":
    app = QApplication(sys.argv)
    app.setStyle('Fusion')

    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
