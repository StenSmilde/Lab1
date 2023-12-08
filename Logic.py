from PyQt6.QtWidgets import *
from Gui import *
import csv
import numpy as np
import matplotlib.pyplot as plt


class Logic(QMainWindow, Ui_VotingMenu):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.pushButton.clicked.connect(lambda: self.vote())
        self.pushButton_2.clicked.connect(lambda: self.clear())
        self.pushButton_3.clicked.connect(lambda: self.view_parlement())

    def vote(self):
        try:
            multiplier = int(self.lineEdit.text())
        except ValueError:
            self.label_3.setText(f'Multiplier should be an integer')
        else:
            with open('results.csv', 'r+', newline='') as csv_file:
                content = list(csv.reader(csv_file, delimiter=","))
                csv_file.seek(0)  # move the file cursor back to the beginning
                if self.radioButton.isChecked():
                    content[1][0] = str(float(content[1][0]) + multiplier)
                elif self.radioButton_2.isChecked():
                    content[1][1] = str(float(content[1][1]) + multiplier)
                elif self.radioButton_3.isChecked():
                    content[1][2] = str(float(content[1][2]) + multiplier)
                elif self.radioButton_4.isChecked():
                    content[1][3] = str(float(content[1][3]) + multiplier)
                elif self.radioButton_5.isChecked():
                    content[1][4] = str(float(content[1][4]) + multiplier)
                elif self.radioButton_6.isChecked():
                    content[1][5] = str(float(content[1][5]) + multiplier)
                elif self.radioButton_7.isChecked():
                    content[1][6] = str(float(content[1][6]) + multiplier)
                elif self.radioButton_8.isChecked():
                    content[1][7] = str(float(content[1][7]) + multiplier)
                elif self.radioButton_9.isChecked():
                    content[1][8] = str(float(content[1][8]) + multiplier)
                elif self.radioButton_10.isChecked():
                    content[1][9] = str(float(content[1][9]) + multiplier)
                elif self.radioButton_11.isChecked():
                    content[1][10] = str(float(content[1][10]) + multiplier)
                elif self.radioButton_12.isChecked():
                    content[1][11] = str(float(content[1][11]) + multiplier)
                elif self.radioButton_13.isChecked():
                    content[1][12] = str(float(content[1][12]) + multiplier)
                elif self.radioButton_14.isChecked():
                    content[1][13] = str(float(content[1][13]) + multiplier)
                elif self.radioButton_15.isChecked():
                    content[1][14] = str(float(content[1][14]) + multiplier)

                self.label_3.setText(f'')
                data = csv.writer(csv_file)
                data.writerows(content)  # write the entire modified content back to the file

    def clear(self):
        with open('results.csv', 'w', newline='') as csv_file:
            content = csv.writer(csv_file)
            row_one = ["PVV", "GLPVDA", "VVD", "NSC", "D66", "BBB", "SP", "CDA", "PVDD", "SGP", "FVD", "CU", "DENK",
                       "VOLT", "JA21"]
            row_two = np.zeros(15)
            content.writerow(row_one)
            content.writerow(row_two)
            self.lineEdit.setText(f'')
            self.radioButton.setChecked(True)
            self.label_3.setText(f'Results are cleared.')

    def view_parlement(self):
        # data
        with open('results.csv', 'r', newline='') as csv_file:
            content = list(csv.reader(csv_file, delimiter=","))
            parties = content[0][:]
            votes = content[1][:]
            vote_list = []
            data = 0
            for i in range(len(votes)):
                data += float(votes[i])
                vote_list.append(float(votes[i]))
            try:
                1 / data
            except ZeroDivisionError:
                self.label_3.setText(f'Vote at least once to show results.')
            else:
                self.close()
                # append data and assign color
                parties.append("")
                vote_list.append(data)  # 50% blank
                colors = ['cyan', 'darkred', 'slateblue', 'gold', 'mediumaquamarine', 'yellowgreen', 'darkolivegreen', 'red',
                          'darkturquoise', 'wheat', 'mediumorchid', 'darkorange', 'dodgerblue', 'palevioletred', 'darkblue',
                          'white']
                fig = plt.figure(figsize=(10, 8), dpi=100)
                ax = fig.add_subplot(1, 1, 1)
                ax.pie(vote_list, labels=parties, colors=colors)
                ax.legend(loc='lower right')
                ax.set_title("Voting Results")
                ax.add_artist(plt.Circle((0, 0), 0.2, color='white'))
                fig.show()
