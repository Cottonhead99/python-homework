import csv

# Define the file path to the CSV data
file_path = "budget_data.csv"

# Initialize variables to store financial metrics
total_months = 0
net_total_profit_losses = 0
average_change = 0
greatest_increase_date = ""
greatest_increase_amount = float("-inf")
greatest_decrease_date = ""
greatest_decrease_amount = float("inf")

# Read the CSV file and calculate financial metrics
with open(file_path, "r") as file:
    csvreader = csv.reader(file)
    next(csvreader)  # Skip the header row
    previous_profit_loss = None

    for row in csvreader:
        date = row[0]
        profit_loss = int(row[1])

        # Calculate the total number of months
        total_months += 1

        # Calculate the net total of Profit/Losses
        net_total_profit_losses += profit_loss

        # Calculate the change in profit/loss since the previous month
        if previous_profit_loss is not None:
            change = profit_loss - previous_profit_loss

            # Update the greatest increase if applicable
            if change > greatest_increase_amount:
                greatest_increase_date = date
                greatest_increase_amount = change

            # Update the greatest decrease if applicable
            if change < greatest_decrease_amount:
                greatest_decrease_date = date
                greatest_decrease_amount = change

        previous_profit_loss = profit_loss

# Calculate the average change in profit/loss
if total_months > 1:
    average_change = net_total_profit_losses / (total_months - 1)

# Print the results
print("Financial Analysis")
print("-----------------------------")
print(f"Total Months: {total_months}")
print(f"Total: ${net_total_profit_losses}")
print(f"Average Change: ${average_change:.2f}")
print(f"Greatest Increase in Profits: {greatest_increase_date} (${greatest_increase_amount})")
print(f"Greatest Decrease in Losses: {greatest_decrease_date} (${greatest_decrease_amount})")

# Optionally, you can save the results to a text file
with open("financial_analysis.txt", "w") as output_file:
    output_file.write("Financial Analysis\n")
    output_file.write("-----------------------------\n")
    output_file.write(f"Total Months: {total_months}\n")
    output_file.write(f"Total: ${net_total_profit_losses}\n")
    output_file.write(f"Average Change: ${average_change:.2f}\n")
    output_file.write(f"Greatest Increase in Profits: {greatest_increase_date} (${greatest_increase_amount})\n")
    output_file.write(f"Greatest Decrease in Losses: {greatest_decrease_date} (${greatest_decrease_amount})\n")
