import os
import csv

csv_path = os.path.join("Resources", "election_data.csv")

with open(csv_path) as csvfile: #open the csv file
    csvreader = csv.reader(csvfile, delimiter=",")
    csvheader = next(csvreader) # csv header is skipped
        
    #I used the code below first to identify all the canidates, including any "write in" candidates
    #for row in csvreader:
    #   if row[2] not in candidates: 
    #      candidates.append(row[2])
    candidates = ['Khan', 'Correy', 'Li', "O'Tooley"]
    candidate_count = [0, 0, 0, 0] #setup initial count as a list
    total_count = 0 

    # Going through each row to count the votes and assign them to a list called "candidate_count"
    for row in csvreader:
        total_count += 1
        if row[2] == candidates[0]:
            candidate_count[0] +=1
        elif row[2] == candidates[1]:
            candidate_count[1] +=1
        elif row[2] == candidates[2]:
            candidate_count[2] +=1
        elif row[2] == candidates[3]:
            candidate_count[3] +=1

    #created a list with percent win (results)
    highercount = 0
    results = []
    for i in range(4):
        percent_win = (round((100 * (candidate_count[i]/ total_count)), 3)) #round percent to 3 decimal places
        if candidate_count[i] >= highercount: #boolean to identify the candidate with more votes
            highercount = candidate_count[i]
            winner = candidates[i]
        results.append(percent_win) # create a list with the results for each candidate 
    print ("```````")
    print ("Election Results") 
    print ("------------------------------------------") 
    print ("Total Votes: " + str(total_count))  
    print ("------------------------------------------")  
    for i in range(4): #loop to print the results for each candidade
       print(f'{candidates[i]}: {results[i]}% ({candidate_count[i]})') 
    print ("------------------------------------------")
    print("Winner: " + winner)
    print ("------------------------------------------")
    print ("```````")

with open('analysis/poll_results.txt', 'w') as txtf: #create and write a txt file in analysis folder
    txtf.write("Election Results"'\n')
    txtf.write("------------------------------------------"'\n') 
    txtf.write("Total Votes: " + str(total_count))  
    txtf.write('\n')
    txtf.write("------------------------------------------"'\n')  
    for i in range(4): #use a loop to create the results candidate - percent votes - raw count
       txtf.writelines(f' {candidates[i]}: {results[i]}% ({candidate_count[i]})''\n')
    txtf.write("------------------------------------------"'\n') 
    txtf.writelines(f'Winner: {winner}''\n')
    txtf.write("------------------------------------------"'\n') 
