import csv
import operator
with open('students.csv',newline='') as csvfile:
    spamreader = csv.DictReader(csvfile, delimiter=";")
    sortedlist = sorted(spamreader, key=lambda row:(row['ФИО']), reverse=False)
    for row in sortedlist:
        print(row)



