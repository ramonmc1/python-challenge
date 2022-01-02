import os
import csv

csv_path = os.path.join("Resources", "budget_data.csv")

with open(csv_path) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    csvheader = next(csvreader)
    total_count = 0
    total_net = 0
    result = 0
    change = 0
    averagechange = 0
    changemax = change
    changemin = change

    for row in csvreader:
        total_count += 1
        total_net += int(row[1])
        last_result = result
        result = int(row[1])
        changelast = change
        if total_count!=1: #since there is not data before Jan-10, the initial change is omitted
            change = result - last_result
            averagechange = (averagechange + change)
            total_average_change = averagechange / (total_count - 1)
        
        if (change >= changemax):
                changemax = change
                maxperiod = row[0]
        if (change <= changemin):
                changemin = change
                minperiod = row[0]
        
    print ("```````")
    print ("Financial Analysis") 
    print ("------------------------------------------") 
    print ("Total Months: " + str(total_count))  
    print ("Total Revenue: $" + str(total_net))
    print ("Average Change: $" + str(round(total_average_change)))
    print ("Greatest Increase in Profits: " + str(maxperiod) + " " + str(changemax))
    print ("Greatest Decrease in Profits: " + str(minperiod) + " " + str(changemin))
    print ("```````")

with open('analysis/financial_analysis.txt', 'w') as txtf:
    txtf.write("Financial Analysis"'\n')
    txtf.write("------------------------------------------"'\n') 
    txtf.write("Total Months: " + str(total_count)) 
    txtf.write('\n')
    txtf.write("Total Revenue: $" + str(total_net))
    txtf.write('\n')
    txtf.write("Average Change: $" + str(round(total_average_change)))
    txtf.write('\n')
    txtf.write("Greatest Increase in Profits: " + str(maxperiod) + " " + str(changemax))
    txtf.write('\n')
    txtf.write("Greatest Decrease in Profits: " + str(minperiod) + " " + str(changemin))