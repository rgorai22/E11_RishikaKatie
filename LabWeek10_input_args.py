import RPi.GPIO as GPIO
import time
import sys
import csv

start_time = time.time()
runtime = sys.argv[1]
now = start_time
count_interval = sys.argv[2]

filename = sys.argv[3]

ifile = open(filename, 'w', newline='')
dwriter = csv.writer(file)

GPIO.setmode(GPIO.BOARD)
GPIO.setup(31, GPIO.IN, pull_up_down=GPIO.PUD_UP)

def count_pulse(channel):
    global count
    count += 1
    print("Count detected at:", time.strftime('%Y-%m-%d %H:%M:%S'))

GPIO.add_event_detect(31, GPIO.FALLING, callback=count_pulse)

count = 0

try:
    while (now-start_time) < run_time:
        time.sleep(count_interval)
        print("Counts collected:", count, "at", time.time())
        count = 0 

except KeyboardInterrupt:
    GPIO.cleanup() 