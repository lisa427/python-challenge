import os
import csv

budget_csv = os.path.join("Resources", "budget_data.csv")

with open(budget_csv) as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=",")
   
    csv_header = next(csv_file)

    lines = len(list(csv_reader))

    print(lines)

    #for row in csv_reader: