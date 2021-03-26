
import csv
import os


#Copy in the .csv path and open
csvpath = os.path.join("Resources", "budget_data.csv")

with open(csvpath) as csvfile:
    
    csvreader = csv.reader(csvfile, delimiter=',')
    # Extract first row headers to avoid appending
    csv_header = next(csvreader)
    
    months = 0
    netProfit = 0
    changeList = []
    prevMonth = 0
    highestGain = 0
    highestMonth = 0
    highestLoss = 0
    lowestMonth = 0

    #Loop through for each row
    for row in csvreader:
        #Track the months and changes to a list
        months = months + 1
        
        netProfit = float(row[1]) + netProfit
        
        monthChange = float(row[1]) - prevMonth
        
        changeList.append(monthChange)
        
        prevMonth = float(row[1])
        #Check for the max and min gain or month    
        if float(row[1]) > float(highestGain):
            highestGain = row[1]
            highestMonth = row[0]
        else:
            highestGain = highestGain
            highestMonth = highestMonth
            
        if float(row[1]) < float(highestLoss):
            highestLoss = row[1]
            lowestMonth = row[0]
        else: 
            highestLoss = highestLoss
            lowestMonth = lowestMonth
            
    
        
#Drop first row change and get the average               
changeList.pop(0)
averageChange = sum(changeList) / float(len(changeList))

print('Financial Analysis')
print('----------------------------')    
print('Total Months: ' + str(months))
print('Total Profit/Loss: $' + '{:.2f}'.format(netProfit))
print('Average Change: $' + '{:.2f}'.format((averageChange)))
print('Greatest increase in Profits: ' + str(highestMonth) + ' $' + highestGain)
print('Greatest decrease in Profits: ' + str(lowestMonth) + ' $' + highestLoss)