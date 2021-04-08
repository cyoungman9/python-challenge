import os
import csv

poll_csv = os.path.join('..', 'Resources', 'election_data.csv')

count = 0
votes = 0


with open(poll_csv, 'r') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    header = next(csvreader)

    print("Election Results")
    print("-------------------------")

    for row in csvreader:
        count = count + 1

        print(f"Total Votes: {count}")
        print(f"-------------------------")

        total_vote = votes + int(row[1])

    print(f"Khan:")
    print(f"Correy:")
    print(f"Li")
    print(f"O'Tooley:")

    print("-------------------------")

    print("Winner: Khan")

    print("-------------------------")


import sys
sys.stdout = open('poll_csv.txt', 'w')
print('Write this to file.')

