"Set variables"
total_months=0
total_net=0
prev_net=0
total_dates=0
rev_inc=0
total_rev_change=0
max_inc=0
min_inc=0
greatest_dec_date=0
greatest_inc_date=0
date=0
prof_loss=0


"importing a csv file"
import os
import csv
csvpath=os.path.join('C:/Users/sledg/PythonData/python-challenge/PyBank Folder/Resources/02-Homework_03-Python_Instructions_PyBank_Resources_budget_data (1).csv.')
with open(csvpath)as csvfile:
    csvreader= csv.reader(csvfile, delimiter=',')
    print(csvreader)
    csv_header = next(csvreader)
    print(f"CSV Header: {csv_header}")
    print(type(csv_header))
    for row in csvreader:
        print(row)
"Analyze Script"
for row in csvreader:        
    first_row = next(csvreader)
for row in csvreader:    
    total_months += 1
    total_net += int(first_row[1])
    prev_net = int(first_row[1])
    total_rev_change= total_rev_change + rev_inc
    rev_change=int(row[1])-prev_net
    
    if (rev_inc>max_inc):
        max_inc=rev_inc
        greatest_inc_date= row[0]
    if (rev_inc<min_inc):
        min_inc=rev_inc
        greatest_inc_date= row[0]
print('Financial Analysis')
print('Total Months:' + str(total_months))
print("Total" + str(total_net))


    
        
    