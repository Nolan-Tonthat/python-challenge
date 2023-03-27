#import modules
import csv
import os

#filepath
election_csv = os.path.join('..', 'Resources', 'election_data.csv')

#output text file
text_file = "output.txt"

#declaring variables
totalVotes = 0
candidates = {}
names = []
winnerVotes = 0
winnerName = ""

#opening the csv file
with open(election_csv, 'r') as handler:
    csvreader = csv.reader(handler, delimiter = ",")
   
    #skips the first row since the document has a header
    header = next(csvreader) 

    for row in csvreader:
        #increments 1 for each vote in the data set
        totalVotes += 1

        #checks if candidate is NOT in dictionary.  If so, update dictionary with new candidate
        if row[2] not in candidates:
            candidates.update({f"{row[2]}": 1})

        #Otherwise, add 1 vote to candidate
        elif row[2] in candidates:
            candidates[row[2]] += 1

    #splits dictionary data into 2 arrays: an array for candidate names and an array for % votes
    for name in candidates:
       
        #checks for candidate with highest number of votes.  Replace winnerName and winnerVotes variables w/ the candidate's name and vote #
        if candidates[name] > winnerVotes:
            winnerName = name
            winnerVotes = candidates[name]


print("Election Results")
print("-----------------")
print(f"Total Votes: {(totalVotes)}")
print("-----------------")
for name in candidates:
    percentVotes = round((candidates[name] / totalVotes)*100,3) #calculates % of votes for each candidate
    print(f"{name}: {percentVotes}% ({candidates[name]})")
print("-----------------")
print(f"Winner: {winnerName}")
print("-----------------")

with open(text_file, "w") as datafile:
    writer = csv.writer(datafile)

    datafile.write("Election Results\n")
    datafile.write("---------------------\n")
    datafile.write(f"Total Votes: {(totalVotes)}\n")
    datafile.write("---------------------\n")
    for name in candidates:
        percentVotes = round((candidates[name] / totalVotes)*100,3)
        datafile.write(f"{name}: {percentVotes}% ({candidates[name]})\n")
    datafile.write("---------------------\n")
    datafile.write(f"Winner: {winnerName}")
    datafile.write("---------------------\n")

        

