import os
import csv

bank_csv = os.path.join("..", "Resources", "budget_data.csv")

# lists for csv file values
months = []
profit = 0
profit_change = []
var = list()
count = 0

def print_percentage(bank_data):
    months = int(bank_data[0])
    profits = int(bank_data[1])




with open(bank_csv, 'r') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    header = next(csvreader) 

    Print("Financial Analysis")
    Print("----------------------------")  

#read through the data
    for row in csvreader:
        count = count + 1
        profit = profit +int(row[1])
        #months.append = (row[0])
        #profit.append = (int(row[1]))


#total_months = len(months)   
#print(f"Month Count: {months}")  


#for row in range(len(month_list)):
#month_count == row[0] 



# max_change = max(profit_change)
# min_change = min(profit_change)

# if min_change == row[0]:
#     print_percentages(row)

# if max_change == row[0]:
#     print_percentages(row)

# import sys
# original_stdout = sys.stdout



Print(f"Total Months: {months}")
Print(f"Total: {total_amount}")
Print(f"Average Change: {}")
Print(f"Greatest Increase in Profits: {} + {()}")
Print(f"Greatest Decrease in Profits: {} + {()}")


