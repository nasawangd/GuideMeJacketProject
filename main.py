#Importing the necessary GPIO tools module.
import RPi.GPIO as GPIO
import time
#print(time)
#set the mode to board numbering since we are using a breadboard. 
#Board is for pin numbering
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)
#GPIO.setmode(GPIO.BCM)
#These pins will be the ones that will be used for inputs
#Pin numbers that are now set to variables.
GPIO_Front_Trigger = 7
GPIO_LeftShoulder_Trigger_Output = 11
#GPIO_RightShoulder_Trigger = 27
#GPIO_BackSide_Trigger = 22
#be sure to change the numbers to pins names instead.
GPIO.setup(GPIO_Front_Trigger, GPIO.OUT)
GPIO.setup(GPIO_LeftShoulder_Trigger_Output, GPIO.IN)
#GPIO.setup(GPIO_RightShoulder_Trigger, GPIO.IN)
#GPIO.setup(GPIO_BackSide_Trigger, GPIO.IN)
#GPIO.setup(5, GPIO.IN)
#print("Sensor Ready")

#distance function
def distance():
    #output function for the front trigger will set to true.
    #As long as the script is running the trigger will fire.
    #Bare minumum code so far to try and see if trigger works.
    #print("test")
    time.sleep(0.000001)
    #GPIO Trigger has been set to high here
    GPIO.output(GPIO_Front_Trigger, True)

    #Set sensor to sleep in 0.01 seconds. 
    #Reset Sensor back to off.
    time.sleep(0.01)
    GPIO.output(GPIO_Front_Trigger, False)

    #Set the time variables for distance
    startTime = time.time()
    endTime= time.time()

    #need to save the start and end time. That will count as one cycle
    #Save the initial start time
    while GPIO.input(GPIO_LeftShoulder_Trigger_Output) == 0:
        startTime = time.time()
    
    #End time will be when the signal comes back. 
    while GPIO.input(GPIO_LeftShoulder_Trigger_Output) == 1:
        endTime = time.time()
    
    #To figure out the time it takes for the signal to make one full cycle we can
    #print(startTime)
    #print(endTime) 
    TimeCycle = endTime - startTime

    #to calculate distance its (Time difference) * Sonic Speed (34300 cm\s / 2)
    #divide by 2 because the signal is going to destination and then bouncing back. 
    distance = (TimeCycle * 34300)/2

    #print("This works")
    #print(distance)
    return distance
  
    GPIO.cleanup()
    #print(GPIO.output(GPIO_LeftShoulder_Trigger, True))

#This code will constantly fire, printing out the measurement from the sensor
while 1 == 1:
    dist = distance()
    print("Your distance in cm is" + " " + str(dist))
    time.sleep(1)
    #print("YOOo this time is measured in" % dist)
    #time.sleep(1)

    #used to stop by ctrl-c
    #except KeyboardInterrupt:
     #   print("Measurement stopped by User")
     #   GPIO.cleanup()
