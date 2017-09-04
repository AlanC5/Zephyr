'''Main file to run the code'''
#!/usr/bin/python3
import RPi.GPIO as GPIO
# import time
import Adafruit_DHT
from resources.DISTANCE_SENSOR import DistanceSensor
from resources.TEMPERATURE_SENSOR import TemperatureHumiditySensor

# Distance Sensor
# TRIG is the output PIN, triggers the sensor
# ECHO is the input PIN, reads the signal
TRIG = 23
ECHO = 24

# Temperature Humidity Sensor
INPUT_PIN = 4
DHT_TYPE = Adafruit_DHT.DHT11

# Set up GPIO using BCM numbering
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
FAN_OUTPUT_PIN = 18
GPIO.setup(FAN_OUTPUT_PIN, GPIO.OUT)
# Initially turn off fan
GPIO.output(FAN_OUTPUT_PIN, GPIO.LOW)

# Set up sensors
DISTANCE_SENSOR = DistanceSensor(TRIG, ECHO)
TEMPERATURE_SENSOR = TemperatureHumiditySensor(INPUT_PIN, DHT_TYPE)

# TODO: Create a fan_state and after turning it on, check if conditions to turn the fan off

while True:
    DISTANCE_SENSOR.measure_distance()
    TEMPERATURE_SENSOR.read_inputs()

    DISTANCE = DISTANCE_SENSOR.get_distance()
    TEMPERATURE = TEMPERATURE_SENSOR.get_temperature()

    # Turn on fan under these conditions
    if DISTANCE is not None and DISTANCE < 100 and TEMPERATURE is not None and TEMPERATURE > 20:
        GPIO.output(FAN_OUTPUT_PIN, GPIO.HIGH)
    else:
        GPIO.output(FAN_OUTPUT_PIN, GPIO.LOW)

GPIO.cleanup()
