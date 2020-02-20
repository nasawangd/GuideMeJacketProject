#Importing the necessary GPIO tools module.
import RPi.GPIO as GPIO
import time
import vibrate
#print(time)
#set the mode to board numbering since we are using a breadboard. 
#Board is for pin numbering
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)
#GPIO.setmode(GPIO.BCM)
#These pins will be the ones that will be used for inputs
#Pin numbers that are now set to variables.
GPIO_Front_Left_Trigger = 5
GPIO_Front_Left_Trigger_Output = 7
#***Old pin numbers***
#GPIO_Front_Left_Trigger = 7
#GPIO_Front_Left_Trigger_Output = 11
#GPIO_RightShoulder_Trigger = 27
#GPIO_BackSide_Trigger = 22
#be sure to change the numbers to pins names instead.
GPIO.setup(GPIO_Front_Left_Trigger, GPIO.OUT)
GPIO.setup(GPIO_Front_Left_Trigger_Output, GPIO.IN)
#GPIO.setup(GPIO_RightShoulder_Trigger, GPIO.IN)
#GPIO.setup(GPIO_BackSide_Trigger, GPIO.IN)
#GPIO.setup(5, GPIO.IN)
print("Front Left Sensor Ready")

GPIO_Rear_Left_Trigger = 13
GPIO_Rear_Left_Trigger_Output = 15
GPIO.setup(GPIO_Rear_Left_Trigger, GPIO.OUT)
GPIO.setup(GPIO_Rear_Left_Trigger_Output, GPIO.IN)
print("Rear Left Sensor Ready")

GPIO_Front_Right_Trigger = 21
GPIO_Front_Right_Trigger_Output = 23
GPIO.setup(GPIO_Front_Right_Trigger, GPIO.OUT)
GPIO.setup(GPIO_Front_Right_Trigger_Output, GPIO.IN)
print("Front Right Sensor Ready")

GPIO_Rear_Left_Trigger = 35
GPIO_Rear_Left_Trigger_Output = 37
GPIO.setup(GPIO_Rear_Left_Trigger, GPIO.OUT)
GPIO.setup(GPIO_Rear_Left_Trigger_Output, GPIO.IN)
print("Rear Right Sensor Ready")

#distance function for the front left ultrasonic sensor
def front_left_distance():
    #output function for the front trigger will set to true.
    #As long as the script is running the trigger will fire.
    #Bare minumum code so far to try and see if trigger works.
    #print("test")
    time.sleep(0.000001)
    #GPIO Trigger has been set to high here
    GPIO.output(GPIO_Front_Left_Trigger, True)

    #Set sensor to sleep in 0.01 seconds. 
    #Reset Sensor back to off.
    time.sleep(0.01)
    GPIO.output(GPIO_Front_Left_Trigger, False)

    #Set the time variables for distance
    startTime = time.time()
    endTime= time.time()

    #need to save the start and end time. That will count as one cycle
    #Save the initial start time
    while GPIO.input(GPIO_Front_Left_Trigger_Output) == 0:
        startTime = time.time()
    
    #End time will be when the signal comes back. 
    while GPIO.input(GPIO_Front_Left_Trigger_Output) == 1:
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
    return front_left_distance
  
    GPIO.cleanup()
    #print(GPIO.output(GPIO_LeftShoulder_Trigger, True))

#distance function for the rear left ultrasonic sensor
def rear_left_distance():
    #output function for the front trigger will set to true.
    #As long as the script is running the trigger will fire.
    #Bare minumum code so far to try and see if trigger works.
    #print("test")
    time.sleep(0.000001)
    #GPIO Trigger has been set to high here
    GPIO.output(GPIO_Rear_Left_Trigger, True)

    #Set sensor to sleep in 0.01 seconds. 
    #Reset Sensor back to off.
    time.sleep(0.01)
    GPIO.output(GPIO_Rear_Left_Trigger, False)

    #Set the time variables for distance
    startTime = time.time()
    endTime= time.time()

    #need to save the start and end time. That will count as one cycle
    #Save the initial start time
    while GPIO.input(GPIO_Rear_Left_Trigger_Output) == 0:
        startTime = time.time()
    
    #End time will be when the signal comes back. 
    while GPIO.input(GPIO_Rear_Left_Trigger_Output) == 1:
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
    return rear_left_distance
  
    GPIO.cleanup()
    #print(GPIO.output(GPIO_LeftShoulder_Trigger, True))
    
#distance function for the front right ultrasonic sensor
def front_left_distance():
    #output function for the front trigger will set to true.
    #As long as the script is running the trigger will fire.
    #Bare minumum code so far to try and see if trigger works.
    #print("test")
    time.sleep(0.000001)
    #GPIO Trigger has been set to high here
    GPIO.output(GPIO_Front_Right_Trigger, True)

    #Set sensor to sleep in 0.01 seconds. 
    #Reset Sensor back to off.
    time.sleep(0.01)
    GPIO.output(GPIO_Front_Right_Trigger, False)

    #Set the time variables for distance
    startTime = time.time()
    endTime= time.time()

    #need to save the start and end time. That will count as one cycle
    #Save the initial start time
    while GPIO.input(GPIO_Front_Right_Trigger_Output) == 0:
        startTime = time.time()
    
    #End time will be when the signal comes back. 
    while GPIO.input(GPIO_Front_Right_Trigger_Output) == 1:
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
    return front_right_distance
  
    GPIO.cleanup()
    #print(GPIO.output(GPIO_LeftShoulder_Trigger, True))
    
#distance function for the rear right ultrasonic sensor
def rear_left_distance():
    #output function for the front trigger will set to true.
    #As long as the script is running the trigger will fire.
    #Bare minumum code so far to try and see if trigger works.
    #print("test")
    time.sleep(0.000001)
    #GPIO Trigger has been set to high here
    GPIO.output(GPIO_Rear_Right_Trigger, True)

    #Set sensor to sleep in 0.01 seconds. 
    #Reset Sensor back to off.
    time.sleep(0.01)
    GPIO.output(GPIO_Rear_Right_Trigger, False)

    #Set the time variables for distance
    startTime = time.time()
    endTime= time.time()

    #need to save the start and end time. That will count as one cycle
    #Save the initial start time
    while GPIO.input(GPIO_Rear_Right_Trigger_Output) == 0:
        startTime = time.time()
    
    #End time will be when the signal comes back. 
    while GPIO.input(GPIO_Rear_Right_Trigger_Output) == 1:
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
    return rear_right_distance
  
    GPIO.cleanup()
    #print(GPIO.output(GPIO_LeftShoulder_Trigger, True))


#This code will constantly fire, printing out the measurement from the sensor
while 1 == 1:
    fldist = front_left_distance()
    print("Your distance in cm is" + " " + str(fldist))
    time.sleep(0.5)
    if fldist >= 71 and fldist <= 200:
       vibrate.front_left_minPulse()
       print("Your distance in cm is" + " " + str(fldist))

    elif fldist >= 30 and fldist <= 70:
       vibrate.front_left_quarterPulse()
       print("Your distance in cm is" + " " + str(fldist))

    elif fldist <= 29:
       vibrate.front_left_steadyPulse()
       print("Your distance in cm is" + " " + str(fldist))

    elif fldist > 200:
       print("out of bounds")
       vibrate.stopPulsing()
        
    rldist = rear_left_distance()
    print("Your distance in cm is" + " " + str(rldist))
    time.sleep(0.5)
    if rldist >= 71 and rldist <= 200:
       vibrate.rear_left_minPulse()
       print("Your distance in cm is" + " " + str(rldist))

    elif rldist >= 30 and rldist <= 70:
       vibrate.rear_left_quarterPulse()
       print("Your distance in cm is" + " " + str(rldist))

    elif rldist <= 29:
       vibrate.rear_left_steadyPulse()
       print("Your distance in cm is" + " " + str(rldist))

    elif rldist > 200:
       print("out of bounds")
       vibrate.stopPulsing()
        
    frdist = front_right_distance()
    print("Your distance in cm is" + " " + str(frdist))
    time.sleep(0.5)
    if frdist >= 71 and frdist <= 200:
       vibrate.front_right_minPulse()
       print("Your distance in cm is" + " " + str(frdist))

    elif fldist >= 30 and fldist <= 70:
       vibrate.front_right_quarterPulse()
       print("Your distance in cm is" + " " + str(frdist))

    elif frdist <= 29:
       vibrate.front_right_steadyPulse()
       print("Your distance in cm is" + " " + str(frdist))

    elif frdist > 200:
       print("out of bounds")
       vibrate.stopPulsing()
        
    rldist = rear_left_distance()
    print("Your distance in cm is" + " " + str(rldist))
    time.sleep(0.5)
    if rldist >= 71 and rldist <= 200:
       vibrate.rear_left_minPulse()
       print("Your distance in cm is" + " " + str(rldist))

    elif rldist >= 30 and rldist <= 70:
       vibrate.rear_left_quarterPulse()
       print("Your distance in cm is" + " " + str(rldist))

    elif rldist <= 29:
       vibrate.rear_left_steadyPulse()
       print("Your distance in cm is" + " " + str(rldist))

    elif rldist > 200:
       print("out of bounds")
       vibrate.stopPulsing()

#    else:
#       vibrate.stopPulsing()
   #print("YOOo this time is measured in" % dist)
    #time.sleep(1)
#    if KeyboardInterrupt:
#	print("User stopped measurement, thanks for using")
    #used to stop by ctrl-c
    #except KeyboardInterrupt:
     #   print("Measurement stopped by User")
     #   GPIO.cleanup()
