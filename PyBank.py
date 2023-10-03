import os
import csv

budget_csv = os.path.join(r"C:\Users\jimmy\Downloads\Module_3\PyBank\Resources\budget_data.csv")

months = []
profits_losses = []
list_of_changes = []
previous_month_profit = 0
total_change_in_profit = 0

with open(budget_csv) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    next(csvreader)
    for row in csvreader:
        # Assigning column values to a new variable
        date = row[0]
        monthly_profit = int(row[1])
        # Appending each row value to an array
        months.append(date)
        profits_losses.append(monthly_profit)
        # The changes in "Profit/Losses" over the entire period
        change = monthly_profit - previous_month_profit
        list_of_changes.append(change)
        # Adding each output for change to a growing total
        total_change_in_profit += change
        #Storing the value of one row's monthly profit as the next subtracted value
        previous_month_profit = monthly_profit
        
# The total number of months included in the dataset
total_months = len(months)

# The total number of months included in the dataset
net_total = sum(profits_losses)

# The average of those changes in "Profits/Losses" over the entire period
average_change_in_profit = total_change_in_profit / len(months)

#The greatest increase in profits (date and amount) over the entire period
greatest_increase = max(list_of_changes)
largest_month = months[list_of_changes.index(greatest_increase)]

#The greatest decrease in profits (date and amount) over the entire period
greatest_decrease = min(list_of_changes)
lowest_month = months[list_of_changes.index(greatest_decrease)]

#Financial Analysis Output
print("")
print("----------------------------------------------------------------------------------------------------")
print("Financial Results (PyBank)")
print("-------------------------")
print(f'Total Months: {total_months}')
print(f'Total: {net_total}')
print(f'Average Change: {average_change_in_profit}')
print(f'Greatest Increase: {largest_month} (${greatest_increase})')
print(f'Greatest Decrease: {lowest_month} $({greatest_decrease})')
