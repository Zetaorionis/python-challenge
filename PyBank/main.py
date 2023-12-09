import os
import csv

budget_data_csv = os.path.join("Resources", "budget_data.csv")

with open(budget_data_csv) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")

#### Print top of file
print("Financial Analysis")
print("----------------------------")


##### The Total # of Months included in the dataset
#counter
months = 0
# loop
for  in :



    months += months

# display total
print(months)
    
    
#### The net total amount of "Profit/Losses" over the entire period

#### The changes in "Profit/Losses" over the entire period, and then the average of those changes

#### he greatest increase in profits (date and amount) over the entire period

#### The greatest decrease in profits (date and amount) over the entire period

#### Export result to text file
