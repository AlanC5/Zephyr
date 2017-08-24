# 1 We need the Adafruit DHT11 Library
# git clone https://github.com/adafruit/Adafruit_Python_DHT.git
# 2 Change directory
# cd Adafruit_Python_DHT
# 3 Install
# sudo apt-get install build-essential python-dev
# sudo python setup.py install

# Reading the data into Terminal
#!/usr/bin/python
import sys
import Adafruit_DHT

while True:
    # Celsius Reading, Fahrenheit reading is located inside Adafruit_DHT library
    # Try to grab a sensor reading.  Use the read_retry method which will retry up
    # to 15 times to get a sensor reading (waiting 2 seconds between each retry).
    # humidity, temperature = Adafruit_DHT.read_retry(sensor, pin)
    humidity, temperature = Adafruit_DHT.read_retry(11, 4)
    # Prints to terminal
    print 'Temp: {0:0.1f} C  Humidity: {1:0.1f} %'.format(temperature, humidity)
