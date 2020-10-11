"Set variables"
total_months=0
total_net=0
total_rev_change=0
max_inc=0
min_inc=0
greatest_dec_date=0
greatest_inc_date=0
prof_loss=[]
date=[]

"Import csv"
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
"Analysis"
with open(csvpath)as csvfile:
    csvreader= csv.reader(csvfile, delimiter=',')
    print(csvreader)
    csv_header = next(csvreader)
    print(f"CSV Header: {csv_header}")
    print(type(csv_header))

    for row in csvreader:        
        first_row = next(csvreader)
        for row in csvreader: 
            date.append(row[0])
            prof_loss.append(int(row[1]))
            total_months += 1
            total_net += int(row[1])
            if int(row[1])> max_inc:
                max_inc= int(row[1])
                greatest_inc_date= row[0]
            if int(row[1])<min_inc:
                min_inc=int(row[1])
                greatest_dec_date=row[0]
        total_rev_change= (total_net/total_months, 2)       
        break
    
    print(int(total_net))
    print(int(total_months))
    print(total_rev_change)
    print(max_inc, greatest_inc_date)
    print(min_inc, greatest_dec_date)
 
"Final Product"   
print("Financial Analysis")
print("----------")
print(f"Total Months: {str(total_months)}")
print(f"Total: ${str(total_net)}")
print(f"Average Change: ${str(sum(total_rev_change,2))}")
print(f"Greatest Decrease: {greatest_dec_date} (${str(min_inc)})")
print(f"Greatest Increase in Profits: {greatest_inc_date} (${str(max_inc)})")

"Convert to TextFile"
text_file=open("PyBank script.py.txt", "w")
text_file.write("Financial Analysis\n")
text_file.write("--------------\n")
text_file.write("Total Months" + str(total_months) + "\n")
text_file.write("Total" + str(total_net) + "\n")
text_file.write("Average Monthly Change" + str(total_rev_change) + "\n")
text_file.write("Greatest Decrease" + str(min_inc) + "\n")
text_file.write("Greatest Increase" + str(max_inc) + "\n")
text_file.close()    
    
    
    

    
    

        
        




    
        
    