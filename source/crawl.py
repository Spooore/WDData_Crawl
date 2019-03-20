import os
import numpy as np     
import csv

takeout = "../Takeout"
csv_out = '../Consolidated.csv'
csv_header = 'Tytuł,Album,Artysta,Czas trwania (ms),Ocena,Liczba odsłuchań,Usunięto'


CSVFiles = []

#get all csv files and store them in CSVfiles array
for subdir, dirs, files in os.walk(takeout):
    for file in files:
        if "Ścieżki audio" in os.path.join(subdir, file):
            CSVFiles.append(os.path.join(subdir, file))


csv_merge = open(csv_out, 'w')
csv_merge.write(csv_header)
csv_merge.write('\n')

for csvFile in CSVFiles:
    with open (csvFile, 'r') as f:
        reader = csv.reader(f, delimiter=",")
        next(reader, None)
        for row in reader:
            csv_merge.write(','.join(row).replace('&quot;',''))
            csv_merge.write('\n')

 
print(csv_merge)