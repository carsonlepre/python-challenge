#Importing the necessary modules/libraries
import csv
import os

#declaring path to our csv file
file = os.path.join("budget_data.csv")

num_of_months = 0 #declaring integer
running_ProfLoss = 0     #declaring integer
value = 0        #declaring integer
change = 0       #declaring integer
dates = []       #declaring (an empty) list   
profits = []     #declaring (an empty) list

with open(file, newline = "") as csvfile: #using "open" method from csv libraries
    csvreader = csv.reader(csvfile, delimiter = ",")

    csv_header = next(csvreader) #establishes header

    first_row = next(csvreader) 
    num_of_months += 1
    running_ProfLoss += int(first_row[1])
    value = int(first_row[1])
    
    for row in csvreader: #for loop that moves the program through the imported csv file
       
        dates.append(row[0]) #using .append() method to update dates column
        
        change = int(row[1])-value 
        profits.append(change)
        value = int(row[1])
        
        num_of_months += 1 #use concatenation to move for loop through the rows

        running_ProfLoss = running_ProfLoss + int(row[1])

    
    greatest_increase = max(profits) #codeblock logs greatest daily...
    greatest_index = profits.index(greatest_increase) #...increase for eventual printing
    greatest_date = dates[greatest_index]

    greatest_loss = min(profits) #codeblock logs greatest daily...
    worst_index = profits.index(greatest_loss) #...loss for eventual printing
    worst_date = dates[worst_index]

    avg_change = sum(profits)/len(profits) #divides total volume by number of changes
    

#print data to console per homework instructions
print("Financial Analysis")
print("---------------------")
print("Total Months:" + str(num_of_months))
print("Total:" + str(running_ProfLoss))
print("Average Change:" + str(avg_change))
print("Greatest Increase in Profits:" + str(greatest_increase))
print("Greatest Decrease in Profits:" + str(greatest_loss))

# using open method to generate report as markdown file
output = open("PyBankResultCarson.md", "w")

line1 = "Financial Analysis"
line2 = "---------------------"
line3 = str("Total:" + str(num_of_months))
line4 = str("Total:" + str(running_ProfLoss))
line5 = str("Average Change:" + str(avg_change))
line6 = str("Greatest Increase in Profits:" + str(greatest_increase))
line7 = str("Greatest Decrease in Profits:" + str(greatest_loss))
output.write('{}\n{}\n{}\n{}\n{}\n{}\n{}\n'.format(line1,line2,line3,line4,line5,line6,line7))
#writes markdown file line by line using empty dictionaries, the "/n" carriage return command, 
# and the .write() and .format() methods.