import csv
import os

csvpath = os.path.join("Resources", "budget_data.csv")
with open(csvpath) as csvfile:
    
    csvreader = csv.reader(csvfile, delimiter=',')
    csv_header = next(csvreader)
    
    months = 0
    netProfit = 0
    monthChange = []
    profitlist = []
    highestGain = 0
    highestLoss = 0
    
    for row in csvreader:
        months = months + 1
        netProfit = float(row[1]) + netProfit
            
        if float(row[1]) > float(highestGain):
            highestGain = row[1]
        else:
            highestGain = highestGain
            
        if float(row[1]) < float(highestLoss):
            highestLoss = row[1]
        else: highestLoss = highestLoss
            
                
      

        
        
    
print('Total Months: ' + str(months))
print('Total Profit/Loss: $' + str(netProfit))
print('Greatest increase in Profits: $' + str(highestGain))
print('Greatest decrease in Profits: $' + str(highestLoss))
    