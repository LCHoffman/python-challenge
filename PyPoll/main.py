import os
import csv

pypoll_csv = os.path.join('.','Resources','election_data.csv')

#create lists
candidate = []
voter = []

with open(pypoll_csv, 'r') as election:
    pypollcsv = csv.reader(election, delimiter = ',')
    next(pypollcsv)
    for row in pypollcsv:
        voter.append(row[0])
        candidate.append(row[2])

#Find total votes
total_votes = len(voter)

#List of unique candidates
unique = set(candidate) 
list_u = (list(unique))
#Unique List was originally printed to find all candidate names, those names were used for code below.
    
#Count number of votes per candidate
count1 = candidate.count("O'Tooley")
count2 = candidate.count("Li")
count3 = candidate.count("Correy")
count4 = candidate.count("Khan")

Names = ["O'Tooley", "Li", "Correy", "Khan"]

#Calculate percentage of votes per candidate
perO = round((count1 / total_votes) * 100, 3)
perL = round((count2 / total_votes) * 100, 3)
perC = round((count3 / total_votes) * 100, 3)
perK = round((count4 / total_votes) * 100, 3)

percent_list = [perO, perL, perC, perK]

#Determine the winner
combined_data = list(zip(Names, percent_list))

most_votes = []
for name in combined_data:
    if max(percent_list) == name[1]:
        most_votes.append(name[0])
        Winner = most_votes[0]

#Print results to terminal
print("Election Results")
print("------------------------")
print(f"Total Votes: {total_votes}")
print("------------------------")
print(f"O'Tooley: {perO}% ({count1} votes)")
print(f"Li: {perL}% ({count2} votes)")
print(f"Correy: {perC}% ({count3} votes)")
print(f"Khan: {perK}% ({count4} votes)")
print("------------------------")
print(f'The winner is {Winner}!')

#Print results to text file
Results = open("Results.txt", "w")
Results.write("Election Results")
Results.write("\n")
Results.write("------------------------")
Results.write("\n")
Results.write(f"Total Votes: {total_votes}")
Results.write("\n")
Results.write("------------------------")
Results.write("\n")
Results.write(f"O'Tooley: {perO}% ({count1} votes)")
Results.write("\n")
Results.write(f"Li: {perL}% ({count2} votes)")
Results.write("\n")
Results.write(f"Correy: {perC}% ({count3} votes)")
Results.write("\n")
Results.write(f"Khan: {perK}% ({count4} votes)")
Results.write("\n")
Results.write("------------------------")
Results.write("\n")
Results.write(f'The winner is {Winner}!')
Results.close()