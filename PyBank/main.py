import os
import csv

budget_csv = os.path.join("Resources", "budget_data.csv")

with open(budget_csv) as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=",")  
    csv_header = next(csv_file)
    total = 0
    for row in csv_reader:
        total += int(row[1])

with open(budget_csv) as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=",")  
    csv_header = next(csv_file)
    lines = len(list(csv_reader))

with open(budget_csv) as csv_file:
    r = csv.reader(csv_file)
    for i in range(1):
        next(r)
    row2 = next(r)
    num = row2[1]

print(lines)
print(total)
print(num)