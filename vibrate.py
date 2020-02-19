# Importing the different libraries to enable control.
import RPi.GPIO as GPIO
import time

# -------------------------------------------------------

# Setting up the methods of reading the board...

# We are telling python on how to differentiate from the differemt
# pins. In this case, we are using the numbers assigned in the Pi's
# firmware by setting it to GPIO.BOARD
GPIO.setmode(GPIO.BOARD)

# In the next line, we are setting the vibrator to pin 40 (or GPIO21)
vibrator = 40

# In the next line, the PIN is being pulsed at 3V by setting up the pin
# itself to output with GPIO.OUT
GPIO.setup(vibrator, GPIO.OUT)

# The following methods/definitions is setting the GPIO to HIGH or LOW, which
# essentially powers on/off the pin, respectively. 
def steadyPulse():
        GPIO.output(40, GPIO.HIGH)

def stopPulsing():
        GPIO.output(40, GPIO.LOW)

# Sending energy to the pin once the obstacle is about 12ft away (365cm)...
def quarterPulse():
        # start feeding the pin 3V
        steadyPulse()
        # the two following lines allow for the pin to be powered
        # for 1/4 of a second, and then finally stop.
        time.sleep(0.25)
        stopPulsing()
	time.sleep(0.25)
def minPulse():
	steadyPulse()
	time.sleep(1)
	stopPulsing()
	time.sleep(1)
# Executing the program, which starts the vibtrator for 5 seconds then
# stops.
#while True:
#	pulse()
