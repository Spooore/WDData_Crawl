import os
import numpy as np     
import csv
import requests
import xml.etree.ElementTree as ET

takeout = "../Takeout/Muzyka Google Play/Playlisty"
csv_out = '../Consolidated.csv'
csv_header = 'Tytuł,Album,Artysta,Czas trwania (ms),Ocena,Liczba odsłuchań,Usunięto,Indeks playlisty,Genre'


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
            if row[0] is not "":
                line = ','.join(row).replace('&quot;','').replace('&amp;','').replace('&#39;','')
                line_splited=line.split(",")
                print(line_splited[2] + "////" + line_splited[0])
                request="http://ws.audioscrobbler.com/2.0/?method=track.getinfo&api_key=b25b959554ed76058ac220b7b2e0a026&artist="+line_splited[2]+"&track="+line_splited[0]
                response = requests.get(request)
                tree = ET.ElementTree(ET.fromstring(response.content))
                for child in tree.getroot().findall('./track/toptags/tag'):
                    genre = child.find('name')
                    csv_merge.write(line)
                    csv_merge.write(",")
                    csv_merge.write(genre.text) 
                    csv_merge.write("\n")
                if len(tree.getroot().findall('./track/toptags/tag'))==0:
                    csv_merge.write(line)
                    csv_merge.write(",")
                    csv_merge.write("other")
                    csv_merge.write("\n")

 
print(csv_merge)