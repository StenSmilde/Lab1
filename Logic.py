from PyQt6.QtWidgets import *
from Gui import *


class Logic(QMainWindow, Ui_VotingMenu):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.pushButton.clicked.connect(lambda: self.submit())
        self.pushButton_2.clicked.connect(lambda: self.reset())
