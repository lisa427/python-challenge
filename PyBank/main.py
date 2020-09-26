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

with open(budget_csv) as csv_file:
    s = csv.reader(csv_file, delimiter=",")
    for i in range(1):
        next(s)
    row2 = next(s)
    num2 = int(row2[1])

with open(budget_csv) as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=",")  
    next(csv_file)
    next(csv_file)
    for row in csv_reader:
        if int(row[1]) - num2 == greatest_increase:
            increase_date = row[0]
        elif greatest_decrease == int(row[1]) - num2:
            decrease_date = row[0]
        num2 = int(row[1])
  
print("Financial Analysis")
print("----------------------")
print(f"Total Months: {lines}")
print(f"Total: ${total}")
print(f"Average Change: ${round(average, 2)}")
print(f"Greatest Increase in Profits: {increase_date} (${greatest_increase})")
print(f"Greatest Decrease in Profits: {decrease_date} (${greatest_decrease})")

output_path = os.path.join("Analysis", "PyBank_analysis.txt")
output_file = open(output_path,"w")
output_file.write("Financial Analysis \n")
output_file.write("---------------------- \n")
output_file.write(f"Total Months: {lines} \n")
output_file.write(f"Total: ${total} \n")
output_file.write(f"Average Change: ${round(average, 2)} \n")
output_file.write(f"Greatest Increase in Profits: {increase_date} (${greatest_increase}) \n")
output_file.write(f"Greatest Decrease in Profits: {decrease_date} (${greatest_decrease})")
output_file.close()