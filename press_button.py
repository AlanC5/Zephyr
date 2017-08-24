# Note RPi.GPIO only works on Raspberry Pi and is currently unavailable on other environments
import RPi.GPIO as GPIO

# Set up GPIO using BCM numbering
GPIO.setmode(GPIO.BCM)

# PIN setup constants
# Pull up is looking for a high voltage
# Pull down is looking for a low voltage
PULL_UP = 23
PULL_DOWN = 24

GPIO.cleanup()

GPIO.setup(PULL_UP, GPIO.IN, pull_up_down = GPIO.PUD_DOWN)
GPIO.setup(PULL_DOWN, GPIO.IN, pull_up_down = GPIO.PUD_UP)

# Rising-Edge is defined by changes from low to high
# Falling-Edge is defined by changes from high to low

# while True:
#     GPIO.wait_for_edge(23, GPIO.RISING)
#     print(“Button 1 Pressed”)
#     GPIO.wait_for_edge(23, GPIO.FALLING)
#     print(“Button 1 Released”)
#     GPIO.wait_for_edge(24, GPIO.FALLING)
#     print(“Button 2 Pressed”)
#     GPIO.wait_for_edge(24, GPIO.RISING)
#     print(“Button 2 Released”)

# Callback Function
def printFunction(channel):
    print(“Button 1 pressed!”)
    print(“Note how the bouncetime affects the button press”)

# Adding a listener to listen for a button push on the pin
GPIO.add_event_detect(PULL_UP, GPIO.RISING, callback=printFunction, bouncetime=300)

# Multiple Threads are running at once
while True:
    GPIO.wait_for_edge(PULL_DOWN, GPIO.FALLING)
    print(“Button 2 Pressed”)
    GPIO.wait_for_edge(PULL_DOWN, GPIO.RISING)
    print(“Button 2 Released”)

# Remove listener from pin
GPIO.remove_event_detect(PULL_UP)
