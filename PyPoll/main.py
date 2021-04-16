import os
import csv

poll_csv = os.path.join('Resources', 'election_data.csv')

count = 0
votes = 0
khan_vote = 0
canidate_1 = str("Khan")
canidate_2 = str("Correy")
correy_vote = 0
canidate_3 = str("Li")
Li_vote = 0
canidate_4 = str("O'Tooley")
OTooley_vote = 0


#def print_percentages(wrestler_data):
#name =


with open(poll_csv, 'r') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    header = next(csvreader)


    

    for row in csvreader:
        count = count + 1
        if row[2] == canidate_1:
            khan_vote = khan_vote + 1
        elif row[2] == canidate_2:
            correy_vote = correy_vote + 1
        elif row[2] == canidate_3:
            Li_vote = Li_vote + 1
        elif row[2] == canidate_4:
            OTooley_vote = OTooley_vote + 1


    total_khan = khan_vote/count * 100   
    total_correy = correy_vote/count * 100 
    total_Li = Li_vote/count * 100 
    total_OTooley = OTooley_vote/count * 100 

    print("Election Results")
    print("-------------------------")

    print(f"Total Votes: {count}")
    print(f"-------------------------")


    print(f"Khan:{total_khan:.3f}% {khan_vote}")
    print(f"Correy:{total_correy:.3f}% {correy_vote}")
    print(f"Li:{total_Li:.3f}% {Li_vote}")
    print(f"O'Tooley:{total_OTooley:.3f}% {OTooley_vote}")

    print("-------------------------")

    print("Winner: Khan")

    print("-------------------------")


import sys
with open('poll_csv.txt', 'w') as txt_file:
    txt_file.write(f"Election Results\n")
    txt_file.write(f"-------------------------\n")
    txt_file.write(f"Total Votes: {count}\n")
    txt_file.write(f"-------------------------\n")
    txt_file.write(f"Khan:{total_khan:.3f}% {khan_vote}\n")
    txt_file.write(f"Correy:{total_correy:.3f}% {correy_vote}\n")
    txt_file.write(f"Li:{total_Li:.3f}% {Li_vote}\n")
    txt_file.write(f"O'Tooley:{total_OTooley:.3f}% {OTooley_vote}\n")
    txt_file.write("-------------------------\n")
    txt_file.write("Winner: Khan\n")
    txt_file.write("-------------------------\n")


