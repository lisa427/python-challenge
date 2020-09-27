import os
import csv

election_csv = os.path.join("Resources", "election_data.csv")

with open(election_csv) as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=",")  
    csv_header = next(csv_file)
    vote_count = len(list(csv_reader))

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
    votes = []
    counter = 0
    for row in csv_reader:
        votes.append(row[2])

print(votes.count(name_list[counter]))
    

print(vote_count)
print(name_list)
#print(candidate_count)