"Variables List"
totalvotes= 0
canvotes=0
candidates={}
percentvotes=0
mostvotes=0
mostvoted=""

"Inmport csv"
import os
import csv
csvpath=os.path.join('C:/Users/sledg/PythonData/python-challenge/PyPoll Folder/Resources/PyPoll HW.csv')
with open(csvpath) as csvfile:
    csvreader= csv.reader(csvfile, delimiter=',')
    print(csvreader)
    csv_header = next(csvreader)
    print(f"CSV Header: {csv_header}")
    print(type(csv_header))

"Analysis"
with open(csvpath) as csvfile:
    csvreader= csv.reader(csvfile, delimiter=',')
    print(csvreader)
    csv_header = next(csvreader)
    print(f"CSV Header: {csv_header}")
    print(type(csv_header))
    for row in csvreader:
        candidate= row[2]
        totalvotes+=1
        if candidate in candidates:
            candidates[candidate]+=1
        else:
            candidates[candidate]=1
        break 
print("Election Results")
print("-----------")
print(f"Total Votes: {totalvotes}")
with open(csvpath) as csvfile:
    csvreader= csv.reader(csvfile, delimiter=',')
    print(csvreader)
    csv_header = next(csvreader)
    print(f"CSV Header: {csv_header}")
    print(type(csv_header))    
    for row in csvreader:
        canvotes+=candidates[candidate]+1
        percentvotes=(candidates[candidate]/totalvotes)*100
        if candidates[candidate]> mostvotes:
            mostvoted= candidate
            mostvotes= candidates[candidate]
            break
print(f"{candidate}: {int(percentvotes)}% {totalvotes}")
print("-----------")
print(f"Winner: {mostvoted}")
print("----------")


      
    



        
    
                
