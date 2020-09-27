import os
import csv

election_csv = os.path.join("Resources", "election_data.csv")

with open(election_csv) as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=",")  
    csv_header = next(csv_file)
    vote_total = len(list(csv_reader))

with open(election_csv) as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=",")  
    csv_header = next(csv_file)
    name_list = []
    for row in csv_reader:
        if row[2] not in name_list:
            name_list.append(row[2])

#candidate_count = len(name_list)
#for name in name_list:

#with open(election_csv) as csv_file:
    #csv_reader = csv.reader(csv_file, delimiter=",")  
    #csv_header = next(csv_file)
    #for row in csv_reader:
        #for name in name_list:
            #if name == row[2]:

with open(election_csv) as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=",")  
    next(csv_file)
    all_votes = []
    for row in csv_reader:
        all_votes.append(row[2])

counter = 0
vote_counts = []

for name in name_list:
    vote_counts.append(all_votes.count(name_list[counter]))
    counter = counter + 1

print(vote_total)
print(name_list)
#print(candidate_count)
print(vote_counts)