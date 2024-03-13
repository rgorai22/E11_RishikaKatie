import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BOARD)
GPIO.setup(31, GPIO.IN, pull_up_down=GPIO.PUD_UP)

def count_pulse(channel):
    global count
    count += 1
    print("Count detected at:", time.strftime('%Y-%m-%d %H:%M:%S'))

GPIO.add_event_detect(31, GPIO.FALLING, callback=count_pulse)

count = 0

try:
    while True:
        time.sleep(60)
        print("Counts collected in the last minute:", count)
        count = 0 

except KeyboardInterrupt:
    GPIO.cleanup() 
