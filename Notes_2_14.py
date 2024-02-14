# Coding Notes from 2/14 Lab
import sys
import random
import time
import csv

print(sys.argv)

start = time.time()
run_time = 30 #seconds
run_time = int(sys.argv[1])
now = start

filename = "test_data.csv"
filename = sys.argv[2] #input arguments
file = open(filename, "w",newline='')
dwriter = csv.writer(file)

meta_data = ["Time","Data"] # with sensors, replace with types of data gained from sensors
dwriter.writerow(meta_data)

print("Time","Data")

while (now-start) < run_time:
    time.sleep(1)
    data = random.random()
    now = time.time()
    datalist = [now,data]
    dwriter.writerow(datalist)
    print(datalist)
file.close()
#can access terminal, run python scripts (hard to find directory w/ python script though) 
    #cd ___ (accesses folder)
#code.py, change in time, new file
#input arguments, HAS to be run at the terminal