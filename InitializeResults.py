import csv
import numpy as np


with open('results.csv', 'w', newline='') as csv_file:
    content = csv.writer(csv_file)
    row_one = ["PVV", "GLPVDA", "VVD", "NSC", "D66", "BBB", "SP", "CDA", "PVDD", "SGP", "FVD", "CU", "DENK", "VOLT", "JA21"]
    row_two = np.zeros(15)  # initialize votes
    content.writerow(row_one)
    content.writerow(row_two)
