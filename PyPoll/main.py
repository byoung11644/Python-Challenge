import csv
import os

csvpath = os.path.join("Resources", "election_data.csv")
with open(csvpath) as csvfile:
    
    csvreader = csv.reader(csvfile, delimiter=',')
    csv_header = next(csvreader)
    
    totalVotes = 0
    candidates = []
    
    for row in csvreader:
        totalVotes = totalVotes + 1
        
        if row[2] not in candidates:
            candidates.append(row[2])
        
        
        
print(totalVotes)
print(candidates)
