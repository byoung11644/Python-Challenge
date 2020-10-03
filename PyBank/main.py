import csv
import os

csvpath = os.path.join("Resources", "budget_data.csv")
with open(csvpath) as csvfile:
    
    csvreader = csv.reader(csvfile, delimiter=',')
    csv_header = next(csvreader)
    
    months = 0
    netProfit = 0
    changeList = []
    prevMonth = 0
    highestGain = 0
    highestLoss = 0

    
    for row in csvreader:
        months = months + 1
        
        netProfit = float(row[1]) + netProfit
        
        monthChange = float(row[1]) - prevMonth
        
        changeList.append(monthChange)
        
        prevMonth = float(row[1])
            
        if float(row[1]) > float(highestGain):
            highestGain = row[1]
        else:
            highestGain = highestGain
            
        if float(row[1]) < float(highestLoss):
            highestLoss = row[1]
        else: highestLoss = highestLoss
    
        
               
changeList.pop(0)
averageChange = sum(changeList) / float(len(changeList))
    
print('Total Months: ' + str(months))
print('Total Profit/Loss: $' + str(netProfit))
print('Average Change: $' + str(averageChange))
print('Greatest increase in Profits: $' + str(highestGain))
print('Greatest decrease in Profits: $' + str(highestLoss))
 