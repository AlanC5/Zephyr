'''Contains all the fans'''
#!/usr/bin/python3

import RPi.GPIO as GPIO

class Fan:
    '''A Fan with basic input to turn on and off'''
    def __init__(self, OUTPUT):
        '''OUTPIN pin sends a signal to turn on or off
        state is the fan's current state, 0 is off and 1 is on'''
        self.OUTPUT = OUTPUT
        self.state = 0
        self.setup()

    def get_state(self):
        '''Returns current state of fan'''
        return self.state

    def setup(self):
        '''Setup the OUTPUT PIN and turn off fan'''
        GPIO.setup(self.OUTPUT, GPIO.OUT)
        GPIO.output(self.OUTPUT, GPIO.LOW)

    def turn_on(self):
        '''Turn on Fan and set state to 1'''
        if  self.state == 1:
            return
        GPIO.output(self.OUTPUT, GPIO.HIGH)
        self.state = 1

    def turn_off(self):
        '''Turn off Fan and set state to 0'''
        if  self.state == 0:
            return
        GPIO.output(self.OUTPUT, GPIO.LOW)
        self.state = 0
