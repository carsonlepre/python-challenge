#Importing the necessary modules/libraries
import csv
import os

#Creating an object out of the CSV file
file = os.path.join("budget_data.csv")

total_months = 0 #declaring integer
total_pl = 0     #declaring integer
value = 0        #declaring integer
change = 0       #declaring integer
dates = []       #declaring (an empty) list   
profits = []     #declaring (an empty) list

#Opening and reading the CSV file
with open(file, newline = "") as csvfile: #using "open" method from csv libraries
    csvreader = csv.reader(csvfile, delimiter = ",")

    #Reading the header row
    csv_header = next(csvreader) #

    #Reading the first row (so that we track the changes properly)
    first_row = next(csvreader)
    total_months += 1
    total_pl += int(first_row[1])
    value = int(first_row[1])
    
    #Going through each row of data after the header & first row 
    for row in csvreader:
        # Keeping track of the dates
        dates.append(row[0])
        
        # Calculate the change, then add it to list of changes
        change = int(row[1])-value
        profits.append(change)
        value = int(row[1])
        
        #Total number of months
        total_months += 1

        #Total net amount of "Profit/Losses over entire period"
        total_pl = total_pl + int(row[1])

    #Greatest increase in profits
    greatest_increase = max(profits)
    greatest_index = profits.index(greatest_increase)
    greatest_date = dates[greatest_index]

    #Greatest decrease (lowest increase) in profits 
    greatest_decrease = min(profits)
    worst_index = profits.index(greatest_decrease)
    worst_date = dates[worst_index]

    #Average change in "Profit/Losses between months over entire period"
    avg_change = sum(profits)/len(profits)
    

#Print data to console per homework instructions
print("Financial Analysis")
print("---------------------")
print("Total Months:" + str(total_months))
print("Total:" + str(total_pl))
print("Average Change:" + str(avg_change))
print("Greatest Increase in Profits:" + str(greatest_increase))
print("Greatest Decrease in Profits:" + str(greatest_decrease))

#Generate Report as markdown file
output = open("PyBankResult.md", "w")

line1 = "Financial Analysis"
line2 = "---------------------"
line3 = str("Total:" + str(total_months))
line4 = str("Total:" + str(total_pl))
line5 = str("Average Change:" + str(avg_change))
line6 = str("Greatest Increase in Profits:" + str(greatest_increase))
line7 = str("Greatest Decrease in Profits:" + str(greatest_decrease))
output.write('{}\n{}\n{}\n{}\n{}\n{}\n{}\n'.format(line1,line2,line3,line4,line5,line6,line7))
