#Importing the necessary GPIO tools module.
import RPi.GPIO as GPIO
import time
#set the mode to board numbering since we are using a breadboard. 
#Board is for pin numbering.
GPIO.setmode(GPIO.BOARD)

#These pins will be the ones that will be used for inputs
GPIO.setup(4, GPIO.IN)
GPIO.setup(17, GPIO.IN)
GPIO.setup(27, GPIO.IN)
GPIO.setup(22, GPIO.IN)
GPIO.setup(5, GPIO.IN)

#GPIO inputs are all boolean values 1 or 0. 
