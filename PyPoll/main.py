import os
import csv

pypoll_csv = os.path.join('.','Resources','election_data.csv')

#create lists
candidate = []
county = []
voter = []

with open(pypoll_csv, 'r') as election:
    pypollcsv = csv.reader(election, delimiter = ',')
    next(pypollcsv)
    for row in pypollcsv:
        voter.append(row[0])
        county.append(row[1])
        candidate.append(row[2])