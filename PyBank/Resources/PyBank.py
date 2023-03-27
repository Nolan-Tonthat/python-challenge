#import modules
import csv
import os

#file path
budget_csv = os.path.join('..', 'Resources', 'budget_data.csv')

#output text file
text_file = "output.txt"

#declaring variables
totalMonths = [] #total number of dates in data set
totalProfitLoss = [] #net total profit/losses over entire period
avgChange = 0 #avg. change in profit/losses over entire period
GreatInc = ["", 0] #greatest increase in profits (date & amount) over entire period
GreatDec = ["", float('inf')] #greatest decrease in profits (date & amount) over entire period
changeList = []  #list of all profit/loss changes in dataset



#opening the csv file
with open(budget_csv, 'r') as handler:
    csvreader = csv.reader(handler, delimiter = ",")
    
    #skips the first row since the document has a header
    header = next(csvreader) 

    #loop through entire dataset
    for row in csvreader:

        #counts total # of months
        totalMonths.append(str(row[0]))
        #calcuate net total profit/losses over entire period
        totalProfitLoss.append(int(row[1]))
        
        #calculate average change in profit/losses over entire period
    for i in range(len(totalProfitLoss)-1):
        #calculate average change in profit/losses over entire period
        change =  totalProfitLoss[i+1] - totalProfitLoss[i] #calculates change between current and previous profit/loss
        changeList.append(change)  #appends new change into list of changes
    
#find the month of greatest increase and decrease of profits/losses over entire period.  +1 to account for first month not being part of changes
MaxMonth = changeList.index(max(changeList))+1
MinMonth = changeList.index(min(changeList))+1
MaxProfit = max(changeList)
MinProfit = min(changeList)

sumChange = sum(changeList)
totalNumChanges = len(changeList)


avgChange = sumChange/totalNumChanges

print("Financial Analysis")
print("---------------------")
print(f"Total Months: {len(totalMonths)}")
print(f"Total: ${sum(totalProfitLoss)}")
print(f"Average Change: ${round((avgChange),2)}")
print(f"Greatest Increase in Profits: {totalMonths[MaxMonth]} (${(str(MaxProfit))})")
print(f"Greatest Decrease in Profits: {totalMonths[MinMonth]} (${(str(MinProfit))})")

with open(text_file, "w") as datafile:
    writer = csv.writer(datafile)

    datafile.write("Financial Analysis\n")
    datafile.write("---------------------\n")
    datafile.write(f"Total Months: {len(totalMonths)}\n")
    datafile.write(f"Total: ${sum(totalProfitLoss)}\n")
    datafile.write(f"Average Change: ${round((avgChange),2)}\n")
    datafile.write(f"Greatest Increase in Profits: {totalMonths[MaxMonth]} (${(str(MaxProfit))})\n")
    datafile.write(f"Greatest Decrease in Profits: {totalMonths[MinMonth]} (${(str(MinProfit))})\n")





