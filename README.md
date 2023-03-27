.DS.Store
# python-challenge
UCB Data Analytics - Module 3 Python Challenge

I felt that PyBank was super tough for me only to find out I had to change one character for my code to work completely fine.  However, PyPoll was much much easier for me!  I even  felt that I had fun making PyPoll as well.  I do believe that I overcomplicated things with PyPoll though.

**Before You Begin**

Before starting the assignment, be sure to complete the following steps:
1. Create a new repository for this project called python-challenge. Do not add this homework assignment to an existing repository.
2. Clone the new repository to your computer.
3. Inside your local Git repository, create a folder for each Python assignment and name them PyBank and PyPoll.
4. In each folder that you just created, add the following content:
5. A new file called main.py. This will be the main script to run for each analysis.
6. A Resources folder that contains the CSV files you used. Make sure that your script has the correct path to the CSV file.
7. An analysis folder that contains your text file that has the results from your analysis.
8. Push these changes to GitHub or GitLab.


**PyBank Instructions**

In this Challenge, you are tasked with creating a Python script to analyze the financial records of your company. You will be given a financial dataset called budget_data.csv. The dataset is composed of two columns: "Date" and "Profit/Losses".

Your task is to create a Python script that analyzes the records to calculate each of the following values:

1. The total number of months included in the dataset

2. The net total amount of "Profit/Losses" over the entire period

3. The changes in "Profit/Losses" over the entire period, and then the average of those changes

4. The greatest increase in profits (date and amount) over the entire period

5. The greatest decrease in profits (date and amount) over the entire period

Your analysis should align with the following results:

Financial Analysis
----------------------------
Total Months: 86
Total: $22564198
Average Change: $-8311.11
Greatest Increase in Profits: Aug-16 ($1862002)
Greatest Decrease in Profits: Feb-14 ($-1825558)


In addition, your final script should both print the analysis to the terminal and export a text file with the results.

**PyPoll Instructions**

In this Challenge, you are tasked with helping a small, rural town modernize its vote-counting process.
You will be given a set of poll data called election_data.csv. The dataset is composed of three columns: "Voter ID", "County", and "Candidate". Your task is to create a Python script that analyzes the votes and calculates each of the following values:

1. The total number of votes cast
2. A complete list of candidates who received votes
3. The percentage of votes each candidate won
4. The total number of votes each candidate won
5. The winner of the election based on popular vote

Your analysis should align with the following results:

Election Results
-------------------------
Total Votes: 369711
-------------------------
Charles Casper Stockham: 23.049% (85213)
Diana DeGette: 73.812% (272892)
Raymon Anthony Doane: 3.139% (11606)
-------------------------
Winner: Diana DeGette
-------------------------

In addition, your final script should both print the analysis to the terminal and export a text file with the results.



