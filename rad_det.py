import RPi.GPIO as GPIO
import time

# Set up GPIO
GPIO.setmode(GPIO.BOARD)
GPIO.setup(<GPIO_PIN_NUMBER>, GPIO.IN, pull_up_down=GPIO.PUD_UP)  # Assuming you're using Board numbering

# Define callback function
def count_pulse(channel):
    global count
    count += 1
    print("Count detected at:", time.strftime('%Y-%m-%d %H:%M:%S'))

# Add event detection
GPIO.add_event_detect(<GPIO_PIN_NUMBER>, GPIO.FALLING, callback=count_pulse)

# Initialize count
count = 0

try:
    while True:
        time.sleep(60)  # Sleep for a minute
        print("Counts collected in the last minute:", count)
        count = 0  # Reset count for the next minute

except KeyboardInterrupt:
    GPIO.cleanup()  # Clean up GPIO on Ctrl+C exit
