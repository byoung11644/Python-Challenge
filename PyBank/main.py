import csv
import os

csvpath = os.path.join("Resources", "budget_data.csv")
with open(csvpath) as csvfile:
    
    csvreader = csv.reader(csvfile, delimiter=',')
    csv_header = next(csvreader)
    
    months = 0
    netProfit = 0
    
    for row in csvreader:
        months = months + 1
        netProfit = float(row[1]) + netProfit
        
        
    print('Total Months: ' + str(months))
    print('Total Profit/Loss: $' + str(netProfit))
    