import os
import csv

employee_csv = os.path.join("Resources", "employee_data.csv")

# creates a list from the header
with open(employee_csv) as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=",")  
    csv_header = next(csv_file)

# creates a list from the Emp ID column from the csv file
with open(employee_csv) as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=",")  
    next(csv_file)
    emp_id = []
    for row in csv_reader:
        emp_id.append(row[0])

# creates a list from the Name column from the csv file
with open(employee_csv) as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=",")  
    next(csv_file)
    names = []
    for row in csv_reader:
        names.append(row[1])

# creates list of first names
first_names = []
for name in names:
    fname = name.split()
    fname = fname[0]
    first_names.append(fname)

# creates list of last names
last_names = []
for name in names:
    lname = name.split()
    lname = lname[1]
    last_names.append(lname)

# creates a list from the DOB column from the csv file
with open(employee_csv) as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=",")  
    next(csv_file)
    dob = []
    for row in csv_reader:
        dob.append(row[2])

# creates a list from the SSN column from the csv file
with open(employee_csv) as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=",")  
    next(csv_file)
    ssn = []
    for row in csv_reader:
        ssn.append(row[3])

# creates a list from the State column from the csv file
with open(employee_csv) as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=",")  
    next(csv_file)
    state = []
    for row in csv_reader:
        state.append(row[4])

print(first_names[:10])
print(last_names[:10])
