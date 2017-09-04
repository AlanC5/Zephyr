'''Contains all distance sensors'''
#!/usr/bin/python3
import time
import RPi.GPIO as GPIO

class DistanceSensor:
    '''HC-SR04 distance sensor'''
    def __init__(self, TRIG, ECHO):
        '''TRIG is the output PIN, triggers the sensor
        ECHO is the input PIN, reads the signal'''
        self.TRIG = TRIG
        self.ECHO = ECHO
        self.distance = None
        self.setup()

    def get_distance(self):
        '''Getter for distance'''
        return self.distance

    def setup(self):
        '''Turns the sensor on '''
        print('Distance Measurement In Progress')
        GPIO.setup(self.TRIG, GPIO.OUT)
        GPIO.setup(self.ECHO, GPIO.IN)

        # Let the sensor settle first
        GPIO.output(self.TRIG, False)
        print('Waiting For Sensor To Settle')
        time.sleep(2)

        # HC-SR04 sensor requires a short 10uS pulse to start the ranging program
        GPIO.output(self.TRIG, True)
        time.sleep(0.00001)
        GPIO.output(self.TRIG, False)

    def measure_distance(self):
        '''Begin measuring the actual distance'''
        # Calculates distances by measuring time differences
        while GPIO.input(self.ECHO) == 0:
            # Records the final time the signal is low
            pulse_start = time.time()

        while GPIO.input(self.ECHO) == 1:
            # Records the final time the signal is high
            pulse_end = time.time()

        # Difference between pulse_end and pulse_start will tells
        # us how long the signal remained high
        pulse_duration = pulse_end - pulse_start

        # Formula Speed = Distance / Time
        # Speed is 343m/s
        # Time is Time / 2 because pulse_duration is how long it took to go and come back
        # Solve for Distance
        self.distance = 17150 * pulse_duration
        self.distance = round(self.distance, 2)

        print('Distance: ', self.distance, 'cm')



# Note RPi.GPIO only works on Raspberry Pi and is currently unavailable on other environments
# import time
# import RPi.GPIO as GPIO
# GPIO.setmode(GPIO.BCM)
#
# # TRIG is the output PIN, triggers the sensor
# # ECHO is the input PIN, reads the signal
# TRIG = 23
# ECHO = 24
#
# print "Distance Measurement In Progress"
#
# GPIO.setup(TRIG, GPIO.OUT)
# GPIO.setup(ECHO, GPIO.IN)
#
# # Let the sensor settle first
# GPIO.output(TRIG, False)
# print "Waiting For Sensor To Settle"
# time.sleep(2)
#
# # HC-SR04 sensor requires a short 10uS pulse to start the ranging program
# GPIO.output(TRIG, True)
# time.sleep(0.00001)
# GPIO.output(TRIG, False)
#
# # Calculates distances by measuring time differences
# while GPIO.input(ECHO) == 0:
#     # Records the final time the signal is low
#     pulse_start = time.time()
#
# while GPIO.input(ECHO) == 1:
#     # Records the final time the signal is high
#     pulse_end = time.time()
#
# # Difference between pulse_end and pulse_start will tells
# # us how long the signal remained high
# pulse_duration = pulse_end - pulse_start
#
# # Formula Speed = Distance / Time
# # Speed is 343m/s
# # Time is Time / 2 because pulse_duration is how long it took to go and come back
# # Solve for Distance
# distance = 17150 * pulse_duration
# distance = round(distance, 2)
#
# print "Distance: ", distance,"cm"
#
# GPIO.cleanup()
