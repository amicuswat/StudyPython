import csv

with open('FL_insurance_sample.csv', newline='') as csvfile:
    insreader = csv.DictReader(csvfile)
    rows = list(insreader)
    for row in rows[1:3]:
        print(row)
