import os
import csv

employee_csv = os.path.join("Resources", "employee_data.csv")

# function to convert state name to state abbreviation
def get_state(full_state):
    us_state_abbrev = {
        'Alabama': 'AL',
        'Alaska': 'AK',
        'Arizona': 'AZ',
        'Arkansas': 'AR',
        'California': 'CA',
        'Colorado': 'CO',
        'Connecticut': 'CT',
        'Delaware': 'DE',
        'Florida': 'FL',
        'Georgia': 'GA',
        'Hawaii': 'HI',
        'Idaho': 'ID',
        'Illinois': 'IL',
        'Indiana': 'IN',
        'Iowa': 'IA',
        'Kansas': 'KS',
        'Kentucky': 'KY',
        'Louisiana': 'LA',
        'Maine': 'ME',
        'Maryland': 'MD',
        'Massachusetts': 'MA',
        'Michigan': 'MI',
        'Minnesota': 'MN',
        'Mississippi': 'MS',
        'Missouri': 'MO',
        'Montana': 'MT',
        'Nebraska': 'NE',
        'Nevada': 'NV',
        'New Hampshire': 'NH',
        'New Jersey': 'NJ',
        'New Mexico': 'NM',
        'New York': 'NY',
        'North Carolina': 'NC',
        'North Dakota': 'ND',
        'Ohio': 'OH',
        'Oklahoma': 'OK',
        'Oregon': 'OR',
        'Pennsylvania': 'PA',
        'Rhode Island': 'RI',
        'South Carolina': 'SC',
        'South Dakota': 'SD',
        'Tennessee': 'TN',
        'Texas': 'TX',
        'Utah': 'UT',
        'Vermont': 'VT',
        'Virginia': 'VA',
        'Washington': 'WA',
        'West Virginia': 'WV',
        'Wisconsin': 'WI',
        'Wyoming': 'WY',
    }
    abbrev_state = us_state_abbrev[full_state]
    return abbrev_state


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

# creates list of years
years = []
for date in dob:
    year = date.split("-")
    year = year[0]
    years.append(year)

# creates list of months
months = []
for date in dob:
    month = date.split("-")
    month = month[1]
    months.append(month)

# creates list of days
days = []
for date in dob:
    day = date.split("-")
    day = day[2]
    days.append(day)

# creates list of reformatted dates
new_dob = []
counter = 0
for date in dob:
    new_date = (months[counter] + "/" + days[counter] + "/" + years[counter])
    new_dob.append(new_date)
    counter = counter + 1

# creates a list from the SSN column from the csv file
with open(employee_csv) as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=",")  
    next(csv_file)
    ssns = []
    for row in csv_reader:
        ssns.append(row[3])

# creates list of last 4 digits of ssn
lastfour_ssn = []
for ssn in ssns:
    lastfour = ssn.split("-")
    lastfour = lastfour[2]
    lastfour_ssn.append(lastfour)

# creates list of reformatted ssns
new_ssns = []
counter = 0
for ssn in ssns:
    new_ssn = ("***-**-" + lastfour_ssn[counter])
    new_ssns.append(new_ssn)
    counter = counter + 1

# creates a list from the State column from the csv file
with open(employee_csv) as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=",")  
    next(csv_file)
    states = []
    for row in csv_reader:
        states.append(row[4])

# creates a list of reformatted states
new_states = []
counter = 0
for state in states:
    st = states[counter]
    st2 = get_state(st)
    new_states.append(st2)
    counter = counter + 1


print(emp_id[:10])
print(first_names[:10])
print(last_names[:10])
print(new_dob[:10])
print(new_ssns[:10])
print(states[:10])
print(new_states[:10])

