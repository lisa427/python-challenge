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
    r = csv.reader(csv_file, delimiter=",")
    for i in range(1):
        next(r)
    row2 = next(r)
    num = int(row2[1])

#with open(budget_csv) as csv_file:
    #csv_reader = csv.reader(csv_file, delimiter=",")  
    #next(csv_file)
    #next(csv_file)
    #for row in csv_reader:
        #row.append(int(row[1]) - num)
        #num = int(row[1])
    #change_list = [row[2]]
    #print(change_list[3])

with open(budget_csv) as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=",")  
    next(csv_file)
    next(csv_file)
    change_list = []
    for row in csv_reader:
        change_list.append(int(row[1]) - num)
        num = int(row[1])

average = sum(change_list) / len(change_list)

greatest_increase = change_list[0]
greatest_decrease = change_list[0]

for j in change_list:
    if j > greatest_increase:
        greatest_increase = j
    elif j < greatest_decrease:
        greatest_decrease = j


print(lines)
print(total)
print(round(average, 2))
print(greatest_increase)
print(greatest_decrease)