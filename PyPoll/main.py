import os
import csv

ELECTION_CSV_DATA_PATH = os.path.join("Resources", "election_data.csv")
ANALYSIS_PATH = os.path.join("analysis", "results.txt")

os.chdir(os.path.dirname(os.path.realpath(__file__)))
with open(ELECTION_CSV_DATA_PATH) as csvfile:
    csvreader = csv.reader(csvfile)
    header = next(csvreader)

    total_votes = 0
    votes = {}
    canadates = []
    percentage = []
    previous_canadate = ''
    first_place = ''
    # master_list = {canadates[0]: votes[0], canadates[1]: votes[1], canadates[2]: votes[2]}

    for row in csvreader:
        # The total number of votes cast
        total_votes += 1

        current_vote = row[0]
        current_canadate = row[2]

         # A complete list of candidates who received votes
        if previous_canadate != current_canadate:
            canadates.append(current_canadate)
            votes[current_canadate] = 0
        votes[current_canadate] += 1  
        previous_canadate = current_canadate
    

    #  The percentage of votes each candidate won

    for canadate in votes:
        canadate_votes = votes[current_canadate]
        canadate_percentage = round(int(canadate_votes) / float(total_votes) * 100, 4)
        percentage.append(canadate_percentage)
        

# The winner of the election based on popular vote
first_place = max(votes)

output = (
    "Election Results\n"
    "----------------------------\n"
    f"Total votes: {total_votes}\n"
    "----------------------------\n"
    # The total number of votes each candidate won
    f"Charles Casper Stockham: {percentage[0:1]}% ({votes['Charles Casper Stockham']})\n"
    f"Diana DeGette: {percentage[1:2]}% ({votes['Diana DeGette']})\n"
    f"Raymon Anthony Doane: {percentage[0:1]}% ({votes['Raymon Anthony Doane']})\n"
    "----------------------------\n"
    f"Winner : {first_place}"

)
# Export result to text file
with open(ANALYSIS_PATH, "w") as output_file:
    output_file.write(output)
    print(output)