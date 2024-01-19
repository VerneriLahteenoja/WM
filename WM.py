import sys
from PyQt5.uic import loadUi
from PyQt5.QtWidgets import (QMainWindow, QApplication, 
                             QPushButton, QDoubleSpinBox, 
                             QComboBox, QDateEdit, QLabel, 
                             QProgressBar, QLineEdit, 
                             QSpinBox, QStatusBar)


class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()

        loadUi('WM_MainWindow.ui', self)

        # General tab
        self.genChangeProfilePB: QPushButton = self.generalChageProfilePushButton
        self.genSavePB: QPushButton = self.generalSavePushButton
        self.genClearPB: QPushButton = self.generalClearPushButton
        self.genAddWeightPB: QPushButton = self.genAddWeightPushButton
        self.genWeightDSB: QDoubleSpinBox = self.generalWeightDoubleSpinBox
        self.genWeightDE: QDateEdit = self.generalWeightDateEdit
        self.genConditionProgBar: QProgressBar = self.genConditionProgressBar

        # Current profile display
        self.genProfileLabel: QLabel = self.generalProfileLabel
        # Info Labels
        self.genHeightLabel: QLabel = self.genInfoHeightLabel
        self.genWeightLabel: QLabel = self.genInfoWeightLabel
        self.genAgeLabel: QLabel = self.genInfoAgeLabel
        self.genSexLabel: QLabel = self.genInfoSexLabel
        self.genConditionLabel: QLabel = self.genInfoConditionLabel

        # Edit tab
        self.editPB: QPushButton = self.editPushButton
        self.cancelPB: QPushButton = self.cancelPushButton
        self.editNameLE: QLineEdit = self.editNameLineEdit
        self.editAgeSB: QSpinBox = self.editAgeSpinBox
        self.editHeightDSB: QDoubleSpinBox = self.editHeightDoubleSpinBox
        self.editWeightDSB: QDoubleSpinBox = self.editWeightDoubleSpinBox
        self.editDateDE: QDateEdit = self.editDateDateEdit
        self.editSexCB: QComboBox = self.editSexComboBox

        # Graph tab
        #TODO: Modify to be selected by year and month / whole year / multiple years
        self.showGraphPB: QPushButton = self.showGraphPushButton
        
        # Status Bar
        self.genStatusBar: QStatusBar = self.statusbar

if __name__=="__main__":
    app = QApplication(sys.argv)
    app.setStyle('Fusion')

    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
