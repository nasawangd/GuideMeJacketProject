import RPi.GPIO as GPIO
import time
import distFL
import distFR
import distR
import vib

while 1 == 1:
	dR = distR.distanceR()
	print("Distance(R): " + str(dR) + "cm")
	time.sleep(0.5)
	if dR >= 71 and dR <= 200:
		vib.secPulseR()
		print("Your R distance in cm is" + " " + str(dR))
	elif dR >= 30 and dR <= 70:
		vib.quarterPulseR()
		print("Your R distance in cm is" + " " + str(dR))
	elif dR <= 29:
		vib.PulseR()
		print("Your R distance in cm is" + " " + str(dR))
	elif dR > 200:
		vib.StopPulsingR()
		print("Out of bounds! Safe!!")

