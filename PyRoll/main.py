import os
import csv

election_csv = os.path.join("Resources", "election_data.csv")

# finds total count of votes by counting the lines in csv file
# does not count the header row
with open(election_csv) as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=",")  
    csv_header = next(csv_file)
    vote_total = len(list(csv_reader))

# creates a list of the candidate names 
with open(election_csv) as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=",")  
    csv_header = next(csv_file)
    name_list = []
    for row in csv_reader:
        if row[2] not in name_list:
            name_list.append(row[2])

# creates a list from the Candidate column from the csv file
with open(election_csv) as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=",")  
    next(csv_file)
    all_votes = []
    for row in csv_reader:
        all_votes.append(row[2])

# creates a list that contains the total count of each candidate name
# each vote count will correspond with the same index number of the name_list
counter = 0
vote_counts = []
for name in name_list:
    vote_counts.append(all_votes.count(name_list[counter]))
    counter = counter + 1

# finds the winner by determining which vote count in the vote_count list
# is the largest number
winner_count = 0
for num in vote_counts:
    if num > winner_count:
        winner_count = num
winner_index = vote_counts.index(winner_count)
winner_name = name_list[winner_index]

# creates a list of the percentage of votes for each candidate name
# corresponds with the same index number of the name_list and vote_counts
percentages = []
for number in vote_counts:
    percentages.append(number/vote_total*100)

#prints the results to the terminal
print("Election Results")
print("----------------------")
print(f"Total Votes: {vote_total}")
print("----------------------")
counter2 = 0
for names in name_list:
    print(f"{names}: {round(percentages[counter2])}% ({vote_counts[counter2]})")
    counter2 = counter2 + 1
print("----------------------")
print(f"Winner: {winner_name}")
print("----------------------")

# writes the results to a text file
output_path = os.path.join("Analysis", "PyPoll_analysis.txt")
output_file = open(output_path,"w")
output_file.write("Election Results \n")
output_file.write("---------------------- \n")
output_file.write(f"Total Votes: {vote_total} \n")
output_file.write("---------------------- \n")
counter3 = 0
for names in name_list:
    output_file.write(f"{names}: {round(percentages[counter3])}% ({vote_counts[counter3]}) \n")
    counter3 = counter3 + 1
output_file.write("---------------------- \n")
output_file.write(f"Winner: {winner_name} \n")
output_file.write("----------------------")
output_file.close()