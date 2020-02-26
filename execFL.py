import RPi.GPIO as GPIO
import time
import distFL
import distFR
import vib

while 1 == 1:
	dFL = distFL.distanceFL()
#	print("Distance(FL): " + str(dFL) + "cm")
	time.sleep(0.5)
	if dFL >= 71 and dFL <= 200:
		vib.secPulseFL()
#		print("Your FL distance in cm is" + " " + str(dFL))
	elif dFL >= 30 and dFL <= 70:
		vib.quarterPulseFL()
#		print("Your FL distance in cm is" + " " + str(dFL))
	elif dFL <= 29:
		vib.PulseFL()
#		print("Your FL distance in cm is" + " " + str(dFL))
	elif dFL > 200:
		vib.StopPulsingFL()
#		print("Out of bounds! Safe!!")

