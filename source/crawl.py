import os
import numpy as np     

takeout = "../Takeout"
CSVFiles = []

#get all csv files and store them in CSVfiles array
for subdir, dirs, files in os.walk(takeout):
    for file in files:
        print (os.path.join(subdir, file))
        CSVFiles.append(os.path.join(subdir, file))

for scv in CSVFiles:
    
