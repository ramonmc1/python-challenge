import os
import csv

csv_path = os.path.join("Resources", "budget_data.csv")

with open(csv_path) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    csvheader = next(csvreader)
    total_count = 0 #setting initial counts for variables
    total_net = 0
    result = 0
    change = 0
    averagechange = 0
    changemax = 0
    changemin = 0

    for row in csvreader: #for loop to get the total count and to add the monthly revenue
        total_count += 1
        total_net += int(row[1])
        last_result = result # capture previous value to calculate change (i-1)
        result = int(row[1]) # set up new value (i=1)

        if total_count!=1: #since there is not data before Jan-10, the initial change is omitted
            change = result - last_result
            averagechange = (averagechange + change) #add average change to calculate the 'average change'
            total_average_change = averagechange / (total_count - 1)
        
        if (change >= changemax): #this boolean will only save the highest change as the loop goes through the list
                changemax = change
                maxperiod = row[0]
        if (change <= changemin): #saves the min change as the loop goes through the list
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

with open('analysis/financial_analysis.txt', 'w') as txtf: #create and export txt file to analysis folder
    txtf.write("Financial Analysis"'\n')
    txtf.write("------------------------------------------") 
    txtf.write('\n'"Total Months: " + str(total_count)) 
    txtf.write('\n'"Total Revenue: $" + str(total_net))
    txtf.write('\n'"Average Change: $" + str(round(total_average_change)))
    txtf.write('\n'"Greatest Increase in Profits: " + str(maxperiod) + " " + str(changemax))
    txtf.write('\n'"Greatest Decrease in Profits: " + str(minperiod) + " " + str(changemin))