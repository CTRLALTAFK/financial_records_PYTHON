import os
import csv
#reading csv
csvpath = os.path.join('budget_data.csv')

# Initiating Variables
total_months = []
total_profit = []
revenue_change = []
greatest_increase = []
greatest_decrease = []


# Method 2: Improved Reading using CSV module
with open(csvpath, newline='') as csvfile:

    # CSV reader specifies delimiter and variable that holds contents
    budget_data = csv.reader(csvfile, delimiter=',')

       # Read the header row first (skip this step if there is no header)
    csv_header = next(budget_data)
    
    # Read each row of data after the header
    for row in budget_data:
       
        # Total months = adding each loop
        total_months.append(row[0])
        # Total Profit/losses =  add all in row[1] (and convert row to integer)
        total_profit.append(int(row[1]))
    
    #New loop for average change    
    for i in range(len(total_profit)-1):
        # Month 2 subtract Month 1 and add to list:
        revenue_change.append(total_profit[i+1]-total_profit[i])

greatest_increase = max(revenue_change) 
greatest_decrease = min(revenue_change) 
avg_change = sum(revenue_change) / len(revenue_change)

# find index for max and min
increase_month = revenue_change.index(max(revenue_change)) + 1
decrease_month = revenue_change.index(min(revenue_change)) + 1 

#Printing and writing

# Specify the file to write to
output_path = os.path.join("Financial_Analysis.txt")

# Open the file using "write" mode. Specify the variable to hold the contents
with open(output_path, 'w', newline='') as txtfile:

    header = (f"Financial Analysis \n -------------------------------------------------------\n"
            f"Total months: {len(total_months)}\n"
            f"Total Profit/losses: ${sum(total_profit)}\n"
            f"Average Change: ${avg_change:.2f}\n"
            f"Greatest Increase in Profits: {total_months[increase_month]}  $({greatest_increase}) \n" 
            f"Greatest Decrease in Profits:{total_months[decrease_month]} $({greatest_decrease}) \n")
    print(header)
    txtfile.write(header)

