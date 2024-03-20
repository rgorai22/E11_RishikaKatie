import RPi.GPIO as GPIO
import time
import sys
import csv

start_time = time.time()
run_time = sys.argv[1]
count_interval = sys.argv[2]

filename = sys.argv[3]

ifile = open(filename, 'w', newline='')
dwriter = csv.writer(ifile)
metadata = ['Count', 'Time']

GPIO.setmode(GPIO.BOARD)
GPIO.setup(31, GPIO.IN, pull_up_down=GPIO.PUD_UP)

def count_pulse(channel):
    global count
    count += 1
    #print("Count detected at:", time.strftime('%Y-%m-%d %H:%M:%S'))

GPIO.add_event_detect(31, GPIO.FALLING, callback=count_pulse)

count = 0

try:
    while (time.time()-int(start_time)) < int(run_time):
        time.sleep(int(count_interval))
        count
        print("Counts collected:", count, "at", time.strftime('%Y-%m-%d %H:%M:%S'))
        
        data = (count, time.strftime('%Y-%m-%d %H:%M:%S'))
        dwriter.writerow(data)
        count = 0 

    ifile.close()
except KeyboardInterrupt:
    GPIO.cleanup() 

