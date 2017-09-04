'''Main file to run the code'''
#!/usr/bin/python3
import RPi.GPIO as GPIO
# import time
import Adafruit_DHT
from devices.FAN import Fan
from resources.DISTANCE_SENSOR import DistanceSensor
from resources.TEMPERATURE_SENSOR import TemperatureHumiditySensor

# Set up GPIO using BCM numbering
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

# Fan
# OUTPIN PIN for fan
FAN_OUTPUT = 18

# Distance Sensor
# TRIG is the output PIN, triggers the sensor
# ECHO is the input PIN, reads the signal
D_TRIG = 23
D_ECHO = 24

# Temperature Humidity Sensor
TH_INPUT_PIN = 4
TH_DHT_TYPE = Adafruit_DHT.DHT11

# Set up fan
FAN = Fan(FAN_OUTPUT)

# Set up sensors
DISTANCE_SENSOR = DistanceSensor(D_TRIG, D_ECHO)
TEMPERATURE_SENSOR = TemperatureHumiditySensor(TH_INPUT_PIN, TH_DHT_TYPE)

while True:
    DISTANCE_SENSOR.measure_distance()
    TEMPERATURE_SENSOR.read_inputs()

    DISTANCE = DISTANCE_SENSOR.get_distance()
    TEMPERATURE = TEMPERATURE_SENSOR.get_temperature()

    # Turn on fan under these conditions
    if DISTANCE is not None and DISTANCE < 100 and TEMPERATURE is not None and TEMPERATURE > 20:
        FAN.turn_on()
    else:
        FAN.turn_off()

GPIO.cleanup()
