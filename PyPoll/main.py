import csv
import os

csvpath = os.path.join("Resources", "election_data.csv")
with open(csvpath) as csvfile:
    
    csvreader = csv.reader(csvfile, delimiter=',')
    csv_header = next(csvreader)
    
    totalVotes = 0
    candidatesList = []
    candidateVotes = {i : 0 for i in candidatesList}
        
    
    for row in csvreader:
        totalVotes = totalVotes + 1
        
        if row[2] not in candidatesList:
            candidatesList.append(row[2])
            candidateVotes[row[2]] = 1
        else:
            candidateVotes[row[2]] = int(candidateVotes[row[2]]) + 1
    


def electionResults(csvreader):
    
    print("Election Results")
    print("----------------------------")
    print(f"Total Votes: {totalVotes}")
    print("----------------------------")
    
    for key, value in candidateVotes.items():
        votePercentage = (value / totalVotes)
        votePercentage = "{:.3%}".format(votePercentage)
        print(f"{key}: {votePercentage} ({value})")
        
    print("----------------------------")
    print(f"Winner: {max(candidateVotes, key=candidateVotes.get)}")
    



electionResults(csvreader)      