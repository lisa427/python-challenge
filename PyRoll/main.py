import os
import csv

election_csv = os.path.join("Resources", "election_data.csv")

with open(election_csv) as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=",")  
    csv_header = next(csv_file)
    lines = len(list(csv_reader))

with open(election_csv) as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=",")  
    csv_header = next(csv_file)
    name_list = []
    for row in csv_reader:
        if row[2] not in name_list:
            name_list.append(row[2])


print(lines)
print(name_list)