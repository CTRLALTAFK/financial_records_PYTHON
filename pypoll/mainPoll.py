import os
import csv
#reading csv
csvpath = os.path.join('election_data.csv')

#initiating variables
total_votes = []
candidate_total = {}
Khan = []
Kpercent = 0
Correy = []
Cpercent = 0
Li = []
Lpercent = 0
Ot = []
Opercent = 0
Maxvotes = 0

# Method 2: Improved Reading using CSV module
with open(csvpath, newline='') as csvfile:

    # CSV reader specifies delimiter and variable that holds contents
    election_data = csv.reader(csvfile, delimiter=',')

       # Read the header row first (skip this step if there is no header)
    csv_header = next(election_data)
    
    # Read each row of data after the header
    for i in election_data:
        total_votes.append(1)
        if i[2] == "Khan":
            Khan.append(1)
        elif i[2] == "Correy":
            Correy.append(1)
        elif i[2] == "Li":
            Li.append(1)
        else: Ot.append(1)
        
    #Created dictionary with votes
    candidate_total = {"Khan":len(Khan), "Correy":len(Correy), "Li":len(Li), "O'tooley":len(Ot)}
    #Loop through candidates and votes if value = max then winner = candidate
    for candidate, value in candidate_total.items():
        if value > Maxvotes:
            Maxvotes = value
            winner = candidate
    #function for Percentages
    def percent(name):
        return round(float(len(name))/float(len(total_votes))*100, 3)
    Kpercent = percent(Khan)
    Cpercent = percent(Correy)
    Lpercent = percent(Li)
    Opercent = percent(Ot)

#Printing and writing

# Specify the file to write to
output_path = os.path.join("Election_Results_Analysis.txt")

# Open the file using "write" mode. Specify the variable to hold the contents
with open(output_path, 'w', newline='') as txtfile:

    header = (f"Election Results \n--------------------------- \n" +
          f"Total Votes: {len(total_votes)}\n --------------------------- \n" +
          f"Khan: {Kpercent}%  ({len(Khan)})\n" +
          f"Correy: {Cpercent}% ({len(Correy)})\n" +
          f"Li: {Lpercent}% ({len(Li)})\n" +
          f"O'Tooley: {Opercent}% ({len(Ot)})\n----------------------------\n" +
          f"Winner: {winner}")
    print(header)
    txtfile.write(header)

