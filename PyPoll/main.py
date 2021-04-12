import os
import csv

poll_csv = os.path.join('Resources', 'election_data.csv')

count = 0
votes = 0
khan_count = 0
canidate_1 = str("Khan")

#def print_percentages(wrestler_data):
#name =


with open(poll_csv, 'r') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    header = next(csvreader)

    print("Election Results")
    print("-------------------------")

    for row in csvreader:
        count = count + 1
        if canidate_1 == row:
            khan_vote = khan_count + 1
       



    print(f"Total Votes: {count}")
    print(f"-------------------------")

        #total_vote = votes + int(row[1])

    print(f"Khan:{khan_vote}")
    print(f"Correy:")
    print(f"Li")
    print(f"O'Tooley:")

    print("-------------------------")

    print("Winner: Khan")

    print("-------------------------")


import sys
with open('poll_csv.txt', 'w') as txt_file:
    txt_file.write(f"Total Votes: {count}\n")
    txt_file.write(f"-------------------------\n")
    txt_file.write(f"Khan:\n")
    txt_file.write(f"Correy:\n")
    txt_file.write(f"Li\n")
    txt_file.write(f"O'Tooley:\n")
    txt_file.write("-------------------------\n")
    txt_file.write("Winner: Khan\n")
    txt_file.write("-------------------------\n")


