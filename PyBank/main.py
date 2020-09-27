import os
import csv

pybank_csv = os.path.join('.','Resources','budget_data.csv')

#Creating lists to store data
months = []

with open(pybank_csv, 'r') as budgetreader:
    pybankcsv = csv.reader(budgetreader, delimiter = ',')
    next(pybankcsv)

#Loop through file to add to the month and profit lists
    for row in pybankcsv:
        months.append(row[0])

#calculate total months
total_month = len(months)

#List to hold money
pandl = []
profit_change = []

with open(pybank_csv, 'r') as budgetreader:
    pybankcsv = csv.reader(budgetreader, delimiter = ',')
    next(pybankcsv)

#Loop through file to add to profit lists
    for row in pybankcsv:
        pandl.append(float(row[1]))

#Find the change in profits from month to month and add to list
    for i in range(len(pandl)-1):
        profit_change.append(pandl[i+1]-pandl[i])

#Total revenue for all months
sum_pandl = sum(pandl)  

#Find greastest increase and decrease
Increase = max(profit_change)
Decrease = min(profit_change)

#Index function to match increase/decrease with month occuring
month_increase = profit_change.index(Increase)+1
month_decrease = profit_change.index(Decrease)+1

#Identify month from months list
monthUP = months[month_increase]
monthDOWN = months[month_decrease]

#Financial Statement Printout
print("Financial Analysis")
print("----------------------")
print(f"Total Months: {total_month}")
print(f"Total Amount: ${sum_pandl}")
print(f"Greatest Increase in Profit: {monthUP} ${Increase}")
print(f"Greatest Decrease in Profit: {monthDOWN} ${Decrease}")

#Print to text file
Analysis = open("Financial_Analysis.txt","w")
Analysis.write("Financial Analysis")
Analysis.write("\n")
Analysis.write("----------------------")
Analysis.write("\n")
Analysis.write(f"Total Months: {total_month}")
Analysis.write("\n")
Analysis.write(f"Total Amount: ${sum_pandl}")
Analysis.write("\n")
Analysis.write(f"Greatest Increase in Profit: {monthUP} ${Increase}")
Analysis.write("\n")
Analysis.write(f"Greatest Decrease in Profit: {monthDOWN} ${Decrease}")
Analysis.close()