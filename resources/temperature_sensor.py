#!/usr/bin/python3
# 1 We need the Adafruit DHT11 Library
# git clone https://github.com/adafruit/Adafruit_Python_DHT.git
# 2 Change directory
# cd Adafruit_Python_DHT
# 3 Install
# sudo apt-get install build-essential python-dev
# sudo python setup.py install

# Reading the data into Terminal
import sys
import Adafruit_DHT

class TemperatureHumiditySensor:
    def __init__(self, INPUT_PIN, DHT_TYPE):
        self.INPUT_PIN = INPUT_PIN
        self.DHT_TYPE = DHT_TYPE
        self.humidity = 0
        self.temperature = 0
        self.units = 'Celsisu'

    # Try to grab a sensor reading.  Use the read_retry method which will retry up
    # to 15 times to get a sensor reading (waiting 2 seconds between each retry).
    def read_inputs(self):
        self.humidity, self.temperature = Adafruit_DHT.read_retry(self.DHT_TYPE, self.INPUT_PIN)

    # units to determine temperature units (Celsius, Fahrenheit)
    def print_output(self, units='Celsius'):
        if self.humidity is not None and self.temperature is not None:
            if units == 'Fahrenheit':
                self.temperature = self.temperature * 9/5.0 + 32
                self.units = units

            print 'Temp: {0:0.1f} {1} Humditiy: {2:0.1f} %'.format(self.temperature, units self.humidity)
        else:
            print('Failed to get reading. Try again!')




# while True:
#     # Celsius Reading
#     # Try to grab a sensor reading.  Use the read_retry method which will retry up
#     # to 15 times to get a sensor reading (waiting 2 seconds between each retry).
#     # humidity, temperature = Adafruit_DHT.read_retry(sensor, pin)
#     INPUT_PIN = 4
#     DHT_TYPE = Adafruit_DHT.DHT11
#
#     humidity, temperature = Adafruit_DHT.read_retry(DHT_TYPE, INPUT_PIN)
#
#     if humidity is not None and temperature is not None:
#         # Un-comment the line below to convert the temperature to Fahrenheit.
#         # temperature = temperature * 9/5.0 + 32
#         # Prints to terminal
#         print 'Temp: {0:0.1f} C  Humidity: {1:0.1f} %'.format(temperature, humidity)
#     else:
#         print 'Failed to get reading. Try again!'
