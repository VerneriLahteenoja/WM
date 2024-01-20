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
        self.genChangeProfilePB: QPushButton = self.generalChangeProfilePushButton
        self.genSavePB: QPushButton = self.generalSavePushButton
        self.genClearPB: QPushButton = self.generalClearPushButton
        self.genAddWeightPB: QPushButton = self.genAddWeightPushButton
        self.genAddWeightPB.clicked.connect(self.enableAddBox)
        self.genCancelAddWeightPB: QPushButton = self.genCancelAddWeightPushButton
        self.genCancelAddWeightPB.clicked.connect(self.cancelAddBox)

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
        self.cancelPB: QPushButton = self.cancelEditPushButton
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

    def enableAddBox(self):
        # Enable elements in add box and disable/hide add button
        self.genWeightDSB.setEnabled(True)
        self.genWeightDE.setEnabled(True)
        self.genAddWeightPB.setEnabled(False)
        self.genAddWeightPB.setVisible(False)
        self.genCancelAddWeightPB.setEnabled(True)
        self.genCancelAddWeightPB.setVisible(True)
        self.genSavePB.setEnabled(True)
        self.genClearPB.setEnabled(True)

    def cancelAddBox(self):
        # Disable elements in add box and disable/hide cancel button
        self.genWeightDSB.setValue(0)
        self.genWeightDE.setDate(QDate(2020, 1, 1))
        self.genWeightDSB.setEnabled(False)
        self.genWeightDE.setEnabled(False)
        self.genAddWeightPB.setEnabled(True)
        self.genAddWeightPB.setVisible(True)
        self.genCancelAddWeightPB.setEnabled(False)
        self.genCancelAddWeightPB.setVisible(False)
        self.genSavePB.setEnabled(False)
        self.genClearPB.setEnabled(False)
if __name__=="__main__":
    app = QApplication(sys.argv)
    app.setStyle('Fusion')

    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
