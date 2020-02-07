#Importing the necessary GPIO tools module.
import RPi.GPIO as GPIO
import time
#set the mode to board numbering since we are using a breadboard. 
#Board is for pin numbering.
GPIO.setmode(GPIO.BOARD)

#These pins will be the ones that will be used for inputs
#Pin numbers that are now set to variables.
GPIO_Front_Trigger = 7
GPIO_LeftShoulder_Trigger = 11
#GPIO_RightShoulder_Trigger = 27
#GPIO_BackSide_Trigger = 22
#be sure to change the numbers to pins names instead.
GPIO.setup(GPIO_Front_Trigger, GPIO.IN)
GPIO.setup(GPIO_LeftShoulder_Trigger, GPIO.OUT)
#GPIO.setup(GPIO_RightShoulder_Trigger, GPIO.IN)
#GPIO.setup(GPIO_BackSide_Trigger, GPIO.IN)
#GPIO.setup(5, GPIO.IN)

#distance function
def distance():
    #output function for the front trigger will set to true.
    #As long as the script is running the trigger will fire.
    #Bare minumum code so far to try and see if trigger works.
    GPIO.output(GPIO_LeftShoulder_Trigger, True)
    print(GPIO.output(GPIO_LeftShoulder_Trigger, True))


    return distance

#This code will constantly fire, printing out the measurement from the sensor
while True:
    distance()
