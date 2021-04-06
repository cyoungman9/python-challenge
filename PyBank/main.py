import os
import csv

bank_csv = os.path.join("Resources", "budget_data.csv")

# lists for csv file values
months = []
profit = 0
profit_change = []
var = list()
count = 0
dif_profit = 0
prev_profit = 0
max_profit = 0
min_profit = 999999
max_date = ""
min_date = ""

# def print_percentage(bank_data):
#     months = int(bank_data[0])
#     profits = int(bank_data[1])

with open(bank_csv, 'r') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    header = next(csvreader) 

    print("Financial Analysis")
    print("----------------------------")  

#read through the data
    for row in csvreader:
        count = count + 1
        profit = profit +int(row[1])
        dif_profit = int(row[1]) - prev_profit
        profit_change.append(dif_profit)
        prev_profit = int(row[1])
        if dif_profit > max_profit: 
            max_profit = dif_profit
            max_date = row[0]

        if dif_profit < min_profit: 
            min_profit = dif_profit
            min_date = row[0]

    avg_profit= sum(profit_change[1:])/ len(profit_change[1:])


# import sys
# original_stdout = sys.stdout



print(f"Total Months: {count}")
print(f"Total: {profit}")
# print(profit_change)
print(f"Average Change:{avg_profit:.2f}")
print(f"Greatest Increase in Profits: {max_date} + ${(max_profit)}")
print(f"Greatest Decrease in Profits: {min_date} + ${(min_profit)}")


