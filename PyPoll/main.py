import os
import csv

poll_csv = os.path.join("..", "Resources", "election_data.csv")




with open(election_data_csv) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    header = next(csvreader)