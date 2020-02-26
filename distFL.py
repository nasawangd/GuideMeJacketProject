import RPi.GPIO as GPIO
import time
#import vibrate

# Suppress warnings on used/unused GPIO pins
GPIO.setwarnings(False)

# Set mode to board numbering
GPIO.setmode(GPIO.BOARD)

# The following pins are to be assigned for the FRONT LEFT ultrasonic
# sensor
GPIO_FRONT_LEFT_TRIGGER = 5
GPIO_FRONT_LEFT_OUTPUT = 7
GPIO.setup(GPIO_FRONT_LEFT_TRIGGER, GPIO.OUT)
GPIO.setup(GPIO_FRONT_LEFT_OUTPUT, GPIO.IN)
print("Front left sensor ready!")

# The distance function...

def distanceFL():

	# Poll sensor every.... miniscule second lol
	time.sleep(0.000001)

	# Enable the pin for a single microsecond.
	GPIO.output(GPIO_FRONT_LEFT_TRIGGER, True)

	time.sleep(0.01)

	GPIO.output(GPIO_FRONT_LEFT_TRIGGER, False)

	# Calculate the start and end time for the above pin because...
	startTime = time.time()
	endTime = time.time()

	# ... the next two while loops do just that
	while GPIO.input(GPIO_FRONT_LEFT_OUTPUT) == 0:
		startTime = time.time()

	while GPIO.input(GPIO_FRONT_LEFT_OUTPUT) == 1:
		endTime = time.time()

	# The difference between the start time and the end time, followed by a simple calculation
	# that grabs that difference, multiplies it by the speed of sound, divided by two
	TimeCycle = endTime - startTime

	distance = (TimeCycle * 34300)/2

	return distance

	GPIO.cleanup()

# And finally the while_loop that shows the distance of each sensor.
#while 1 == 1:
#	dist = distanceFL()
#	print("Distance: " + str(dist) + "cm")
#	time.sleep(1.5)
