# Importing the different libraries to enable control.
import RPi.GPIO as GPIO
import time

# -------------------------------------------------------

# Setting up the methods of reading the board...

# We are telling python on how to differentiate from the differemt
# pins. In this case, we are using the numbers assigned in the Pi's
# firmware by setting it to GPIO.BOARD
GPIO.setmode(GPIO.BOARD)

# In the next line, we are setting the front left vibrator to pin 14 (or GPIO14)
front_left_vibrator = 8
# In the next line, we are setting the rear left vibrator to pin 22 (or GPIO25)
rear_left_vibrator= 22
# In the next line, we are setting the front right vibrator to pin 32 (or GPIO12)
front_right_vibrator=32
# In the next line, we are setting the rear right vibrator to pin 36 (or GPIO16)
rear_right_vibrator=36

# In the next lines, the PIN is being pulsed at 3V by setting up the pin
# itself to output with GPIO.OUT
GPIO.setup(front_left_vibrator, GPIO.OUT)
GPIO.setup(rear_left_vibrator, GPIO.OUT)
GPIO.setup(front_right_vibrator, GPIO.OUT)
GPIO.setup(rear_right_vibrator, GPIO.OUT)

# The following methods/definitions is setting the GPIO to HIGH or LOW, which
# essentially powers on/off the pin, respectively. 
def front_left_steadyPulse():
        GPIO.output(8, GPIO.HIGH)
def rear_left_steadyPulse():
        GPIO.output(22, GPIO.HIGH)
def front_right_steadyPulse():
        GPIO.output(32, GPIO.HIGH)
def rear_right_steadyPulse():
        GPIO.output(36, GPIO.HIGH)

def front_left_stopPulsing():
        GPIO.output(8, GPIO.LOW)
def rear_left_stopPulsing():
        GPIO.output(22, GPIO.LOW)
def front_right_stopPulsing():
        GPIO.output(32, GPIO.LOW)
def rear_right_stopPulsing():
        GPIO.output(36, GPIO.LOW)

# Sending energy to the pin once the obstacle is about 12ft away (365cm)...
def front_left_quarterPulse():
        # start feeding the pin 3V
        front_left_steadyPulse()
        # the two following lines allow for the pin to be powered
        # for 1/4 of a second, and then finally stop.
        time.sleep(0.25)
        front_left_stopPulsing()
	time.sleep(0.25)
def front_left_minPulse():
	front_left_steadyPulse()
	time.sleep(1)
	front_left_stopPulsing()
	time.sleep(1)

# Sending energy to the pin once the obstacle is about 12ft away (365cm)...	
def rear_left_quarterPulse():
        # start feeding the pin 3V
        rear_left_steadyPulse()
        # the two following lines allow for the pin to be powered
        # for 1/4 of a second, and then finally stop.
        time.sleep(0.25)
        rear_left_stopPulsing()
	time.sleep(0.25)
def rear_left_minPulse():
	rear_left_steadyPulse()
	time.sleep(1)
	rear_left_stopPulsing()
	time.sleep(1)

# Sending energy to the pin once the obstacle is about 12ft away (365cm)...
def front_right_quarterPulse():
        # start feeding the pin 3V
        front_right_steadyPulse()
        # the two following lines allow for the pin to be powered
        # for 1/4 of a second, and then finally stop.
        time.sleep(0.25)
        front_right_stopPulsing()
	time.sleep(0.25)
def front_right_minPulse():
	front_right_steadyPulse()
	time.sleep(1)
	front_right_stopPulsing()
	time.sleep(1)

# Sending energy to the pin once the obstacle is about 12ft away (365cm)...
def rear_right_quarterPulse():
        # start feeding the pin 3V
        rear_right_steadyPulse()
        # the two following lines allow for the pin to be powered
        # for 1/4 of a second, and then finally stop.
        time.sleep(0.25)
        rear_right_stopPulsing()
	time.sleep(0.25)
def rear_right_minPulse():
	rear_right_steadyPulse()
	time.sleep(1)
	rear_right_stopPulsing()
	time.sleep(1)
	

	


# Executing the program, which starts the vibtrator for 5 seconds then
# stops.
#while True:
#	pulse()
