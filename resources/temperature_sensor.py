'''Contains all Temperature and Humditiy Sensors'''
#!/usr/bin/python3
# 1 We need the Adafruit DHT11 Library
# git clone https://github.com/adafruit/Adafruit_Python_DHT.git
# 2 Change directory
# cd Adafruit_Python_DHT
# 3 Install
# sudo apt-get install build-essential python-dev
# sudo python setup.py install

# Reading the data into Terminal
from Adafruit_Python_DHT import Adafruit_DHT

class TemperatureHumiditySensor:
    '''Adafruit_DHT sensor'''
    def __init__(self, INPUT_PIN, DHT_TYPE):
        self.INPUT_PIN = INPUT_PIN
        self.DHT_TYPE = DHT_TYPE
        self.humidity = None
        self.temperature = None
        self.units = 'Celsius'

    def get_temperature(self):
        '''Getter for temperature'''
        return self.temperature

    def get_humditiy(self):
        '''Getter for humidity'''
        return self.humidity

    def read_inputs(self, units='Celsius'):
        '''Try to grab a sensor reading.  Use the read_retry method which will retry up
        to 15 times to get a sensor reading (waiting 2 seconds between each retry)
        units to determine temperature units (Celsisu, Fahrenheit)'''
        self.humidity, self.temperature = Adafruit_DHT.read_retry(self.DHT_TYPE, self.INPUT_PIN)

        if self.temperature is not None and units == 'Fahrenheit':
            self.temperature = self.temperature * 9/5.0 + 32
            self.units = units

        self.print_output()

    def print_output(self):
        '''Prints the temperature and humidity as long as either of them aren't None'''
        if self.temperature is not None and self.humidity is not None:
            print('Temp: {0:0.1f} {1} Humditiy: {2:0.1f} %'.format(self.temperature, self.units, self.humidity))
        else:
            print('Failed to get reading. Try again!')



# 1 We need the Adafruit DHT11 Library
# git clone https://github.com/adafruit/Adafruit_Python_DHT.git
# 2 Change directory
# cd Adafruit_Python_DHT
# 3 Install
# sudo apt-get install build-essential python-dev
# sudo python setup.py install

# Reading the data into Terminal
# import Adafruit_DHT
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
