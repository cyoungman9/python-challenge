import os
import csv

bank_csv = os.path.join("Resources", "budget_data.csv")

#define functions - sole parameter set to wrestler_data



def print_percentage(bank_data):
    months = int(bank_data[0])
    profits = int(bank_data[1])
    losses = int(bank_data[2])

#calculate totals
    total_months = months

    total_amount = profits - losses


#total month count
with open(bank_csv, new line='') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    header = next(csvreader)

total_months = len(list())

# lists for csv file values
months = []
profit = []
profit_change = []

#read through the data
for row in csvreader:
    months.append = (rows[0])
    profit.append = (int(row[1]))

for x in range(1,len)

for row in range(len(month_list)):
    month_count == row[0] 
    
print(f"Month Count: {month_count}")


max_change = max(profit_change)
min_change = min(profit_change)




#seperate profits/losses?
with open(bank_csv, "w", newline="") as datafile:
    writer = csv.writer(datafile)

    writer.writerow(["Date", "Profits", "Losses"])

   




Print("Financial Analysis")

Print("----------------------------")

Print(f"Total Months: {months}")
Print(f"Total: {total_amount}")
Print(f"Average Change: {}")
Print(f"Greatest Increase in Profits: {} + {()}")
Print(f"Greatest Decrease in Profits: {} + {()}")


