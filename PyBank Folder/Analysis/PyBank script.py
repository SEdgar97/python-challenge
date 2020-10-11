"importing a csv file"
import os
import csv
csvpath=os.path.join('C:/Users/sledg/PythonData/python-challenge/PyBank Folder/02-Homework_03-Python_Instructions_PyBank_Resources_budget_data (1).csv.')
with open(csvpath)as csvfile:
    csvreader= csv.reader(csvfile, delimiter=',')
    print(csvreader)
    
    csv_header = next(csvreader)
    print(f"CSV Header: {csv_header}")
    print(type(csv_header))
    for row in csvreader:
        print(row)
"Analyze Script"
"Total Number of Months"
        

    