import sys
import random
import time
import csv
import board
import busio 
from digitalio
import DigitalInOut, Direction, Pull

print(sys.argv)

start_time = time.time()
run_time = 30
run_time = int(sys.argv[1])
now = start_time

filename = "test_data.csv"
filename = sys.argv[2]
file = open(filename, "w", newline='')
dwriter = csv.writer(file)

meta_data = ["Time", "Data"]
dwriter.writerow(meta_data)
print(meta_data)


# air quality
reset_pin = None

import serial
uart = serial.Serial("/dev/ttyS0", baudrate=9600, timeout=0.25)

from adafruit_pm25.uart import PM25_UART
pm25 = PM25_UART(uart, reset_pin)

print("Found PM2.5 sensor, reading data...")

### WEATHER
import adafruit_bme680
import time
import datetime
import board

i2c = board.I2C()   # uses board.SCL and board.SDA
bme680 = adafruit_bme680.Adafruit_BME680_I2C(i2c)

bme680.sea_level_pressure = 1013.25

while (now - start_time) < run_time:

    try:
        aqdata = pm25.read()
        # print(aqdata)
    except RuntimeError:
        print("Unable to read from sensor, retrying...")
        continue

    print()
    print("Concentration Units (standard)")
    print("---------------------------------------")
    print(
        "PM 1.0: %d\tPM2.5: %d\tPM10: %d"
        % (aqdata["pm10 standard"], aqdata["pm25 standard"], aqdata["pm100 standard"])
    )
    print("Concentration Units (environmental)")
    print("---------------------------------------")
    print(
        "PM 1.0: %d\tPM2.5: %d\tPM10: %d"
        % (aqdata["pm10 env"], aqdata["pm25 env"], aqdata["pm100 env"])
    )
    print("---------------------------------------")
    print("Particles > 0.3um / 0.1L air:", aqdata["particles 03um"])
    print("Particles > 0.5um / 0.1L air:", aqdata["particles 05um"])
    print("Particles > 1.0um / 0.1L air:", aqdata["particles 10um"])
    print("Particles > 2.5um / 0.1L air:", aqdata["particles 25um"])
    print("Particles > 5.0um / 0.1L air:", aqdata["particles 50um"])
    print("Particles > 10 um / 0.1L air:", aqdata["particles 100um"])
    print("---------------------------------------")
    
    "\nTemperature: %0.1f C" % bme680.temperature,
    "Gas: %d ohm" % bme680.gas,
    "Humidity: %0.1f %%" % bme680.relative_humidity,
    "Pressure: %0.3f hPa" % bme680.pressure,
    "Altitude = %0.2f meters" % bme680.altitude
    print("Weather",data)

    time.sleep(1)
    data = random.random()
    now = time.time()
    datalist = [now, data]
    dwriter.writerow(datalist)

    print(datalist)
    
file.close()

# terminal 
    # cd E11_RishikaKatieVic -> if in gitrepo
    # cd ENGIN11 -> in Documents, Cal, Classes, ENGIN11
    # ls
    # python daq_test.py
    # python daq_test.py 10 'test_data.csv'