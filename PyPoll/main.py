import csv
import os

# Files to load and open
csvpath = os.path.join("Resources", "election_data.csv")
textpath = os.path.join("ElectionResults.txt")

with open(textpath, "w") as textFile:    
    with open(csvpath) as csvfile:
    
        csvreader = csv.reader(csvfile, delimiter=',')
        csv_header = next(csvreader)
    
        #Vote counter and candidate list
        totalVotes = 0
        candidatesList = []
        candidateVotes = {i : 0 for i in candidatesList}
        
        #Loop through each row
        for row in csvreader:
            #Count the vote
            totalVotes = totalVotes + 1
            #Append the candidatesList and count the vote
            if row[2] not in candidatesList:
                candidatesList.append(row[2])
                candidateVotes[row[2]] = 1
            else:
                candidateVotes[row[2]] = int(candidateVotes[row[2]]) + 1
    

        #Function to print results fo the .csv
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

#Close election file
textFile.close()
