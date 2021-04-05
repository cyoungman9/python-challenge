import os
import csv

bank_csv = os.path.join('..', 'Resources', 'budget_data.csv')

#define functions - sole parameter set to wrestler_data
def print_percentage(bank_data):
    months = int(bank_data[0])
    profits = int(bank_data[1])
    losses = int(bank_data[2])

    total_months = months

    total_amount = profits - losses


#total month count
with open(bank_csv, 'r') as csvfile:

    csvreader = csv.reader(csvfile, delimiter=',')

    header = next(csvreader)

month_list = [months]

for row in range(len(month_list)):
    month_count == row[0] 
    
print(f"Month Count: {month_count}")

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



      new_length = row[1].split("-")
    length.append(float(new_length[0]))