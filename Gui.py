# Form implementation generated from reading ui file 'Gui.ui'
#
# Created by: PyQt6 UI code generator 6.6.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_VotingMenu(object):
    def setupUi(self, VotingMenu):
        VotingMenu.setObjectName("VotingMenu")
        VotingMenu.resize(600, 600)
        VotingMenu.setMinimumSize(QtCore.QSize(600, 600))
        VotingMenu.setMaximumSize(QtCore.QSize(600, 600))
        self.centralwidget = QtWidgets.QWidget(parent=VotingMenu)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(parent=self.centralwidget)
        self.label.setGeometry(QtCore.QRect(100, 30, 400, 61))
        self.label.setTextFormat(QtCore.Qt.TextFormat.AutoText)
        self.label.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label.setObjectName("label")
        self.Parties = QtWidgets.QGroupBox(parent=self.centralwidget)
        self.Parties.setGeometry(QtCore.QRect(-11, 119, 1011, 311))
        self.Parties.setTitle("")
        self.Parties.setObjectName("Parties")
        self.radioButton = QtWidgets.QRadioButton(parent=self.Parties)
        self.radioButton.setGeometry(QtCore.QRect(50, 40, 95, 20))
        self.radioButton.setObjectName("radioButton")
        self.radioButton_2 = QtWidgets.QRadioButton(parent=self.Parties)
        self.radioButton_2.setGeometry(QtCore.QRect(175, 40, 95, 20))
        self.radioButton_2.setObjectName("radioButton_2")
        self.radioButton_3 = QtWidgets.QRadioButton(parent=self.Parties)
        self.radioButton_3.setGeometry(QtCore.QRect(300, 40, 95, 20))
        self.radioButton_3.setObjectName("radioButton_3")
        self.radioButton_4 = QtWidgets.QRadioButton(parent=self.Parties)
        self.radioButton_4.setGeometry(QtCore.QRect(425, 40, 95, 20))
        self.radioButton_4.setObjectName("radioButton_4")
        self.radioButton_5 = QtWidgets.QRadioButton(parent=self.Parties)
        self.radioButton_5.setGeometry(QtCore.QRect(50, 100, 95, 20))
        self.radioButton_5.setObjectName("radioButton_5")
        self.radioButton_6 = QtWidgets.QRadioButton(parent=self.Parties)
        self.radioButton_6.setGeometry(QtCore.QRect(175, 100, 95, 20))
        self.radioButton_6.setObjectName("radioButton_6")
        self.radioButton_7 = QtWidgets.QRadioButton(parent=self.Parties)
        self.radioButton_7.setGeometry(QtCore.QRect(300, 100, 95, 20))
        self.radioButton_7.setObjectName("radioButton_7")
        self.radioButton_8 = QtWidgets.QRadioButton(parent=self.Parties)
        self.radioButton_8.setGeometry(QtCore.QRect(425, 100, 95, 20))
        self.radioButton_8.setObjectName("radioButton_8")
        self.radioButton_9 = QtWidgets.QRadioButton(parent=self.Parties)
        self.radioButton_9.setGeometry(QtCore.QRect(50, 160, 95, 20))
        self.radioButton_9.setObjectName("radioButton_9")
        self.radioButton_10 = QtWidgets.QRadioButton(parent=self.Parties)
        self.radioButton_10.setGeometry(QtCore.QRect(175, 160, 95, 20))
        self.radioButton_10.setObjectName("radioButton_10")
        self.radioButton_11 = QtWidgets.QRadioButton(parent=self.Parties)
        self.radioButton_11.setGeometry(QtCore.QRect(300, 160, 95, 20))
        self.radioButton_11.setObjectName("radioButton_11")
        self.radioButton_12 = QtWidgets.QRadioButton(parent=self.Parties)
        self.radioButton_12.setGeometry(QtCore.QRect(425, 160, 95, 20))
        self.radioButton_12.setObjectName("radioButton_12")
        self.radioButton_13 = QtWidgets.QRadioButton(parent=self.Parties)
        self.radioButton_13.setGeometry(QtCore.QRect(50, 220, 95, 20))
        self.radioButton_13.setObjectName("radioButton_13")
        self.radioButton_14 = QtWidgets.QRadioButton(parent=self.Parties)
        self.radioButton_14.setGeometry(QtCore.QRect(175, 220, 95, 20))
        self.radioButton_14.setObjectName("radioButton_14")
        self.radioButton_15 = QtWidgets.QRadioButton(parent=self.Parties)
        self.radioButton_15.setGeometry(QtCore.QRect(300, 220, 95, 20))
        self.radioButton_15.setObjectName("radioButton_15")
        self.label_2 = QtWidgets.QLabel(parent=self.Parties)
        self.label_2.setGeometry(QtCore.QRect(420, 210, 141, 31))
        self.label_2.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.lineEdit = QtWidgets.QLineEdit(parent=self.Parties)
        self.lineEdit.setGeometry(QtCore.QRect(430, 240, 113, 22))
        self.lineEdit.setObjectName("lineEdit")
        self.pushButton = QtWidgets.QPushButton(parent=self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(50, 470, 120, 40))
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(parent=self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(430, 470, 120, 40))
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_3 = QtWidgets.QPushButton(parent=self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(240, 470, 120, 40))
        self.pushButton_3.setObjectName("pushButton_3")
        VotingMenu.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(parent=VotingMenu)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 600, 26))
        self.menubar.setObjectName("menubar")
        VotingMenu.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(parent=VotingMenu)
        self.statusbar.setObjectName("statusbar")
        VotingMenu.setStatusBar(self.statusbar)

        self.retranslateUi(VotingMenu)
        QtCore.QMetaObject.connectSlotsByName(VotingMenu)

    def retranslateUi(self, VotingMenu):
        _translate = QtCore.QCoreApplication.translate
        VotingMenu.setWindowTitle(_translate("VotingMenu", "MainWindow"))
        self.label.setText(_translate("VotingMenu", "<html><head/><body><p><span style=\" font-size:16pt;\">Voting Menu Dutch Parlement</span></p></body></html>"))
        self.radioButton.setText(_translate("VotingMenu", "PVV"))
        self.radioButton_2.setText(_translate("VotingMenu", "GLPVDA"))
        self.radioButton_3.setText(_translate("VotingMenu", "VVD"))
        self.radioButton_4.setText(_translate("VotingMenu", "NSC"))
        self.radioButton_5.setText(_translate("VotingMenu", "D66"))
        self.radioButton_6.setText(_translate("VotingMenu", "BBB"))
        self.radioButton_7.setText(_translate("VotingMenu", "SP"))
        self.radioButton_8.setText(_translate("VotingMenu", "CDA"))
        self.radioButton_9.setText(_translate("VotingMenu", "PVDD"))
        self.radioButton_10.setText(_translate("VotingMenu", "SGP"))
        self.radioButton_11.setText(_translate("VotingMenu", "FVD"))
        self.radioButton_12.setText(_translate("VotingMenu", "CU"))
        self.radioButton_13.setText(_translate("VotingMenu", "DENK"))
        self.radioButton_14.setText(_translate("VotingMenu", "VOLT"))
        self.radioButton_15.setText(_translate("VotingMenu", "JA21"))
        self.label_2.setText(_translate("VotingMenu", "<html><head/><body><p><span style=\" font-size:10pt;\">Multiplier:</span></p></body></html>"))
        self.pushButton.setText(_translate("VotingMenu", "Vote"))
        self.pushButton_2.setText(_translate("VotingMenu", "Clear"))
        self.pushButton_3.setText(_translate("VotingMenu", "View Parlement"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    VotingMenu = QtWidgets.QMainWindow()
    ui = Ui_VotingMenu()
    ui.setupUi(VotingMenu)
    VotingMenu.show()
    sys.exit(app.exec())