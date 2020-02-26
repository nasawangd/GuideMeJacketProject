from threading import Thread
#import threading
import RPi.GPIO as GPIO
import time
import distFL
import distFR
import vib

# Home code for all sensors and motors

class FLPollingClass(Thread):
	def __init__(self):
		Thread.__init__(self)
		self.daemon = True
		self.start()
	def run(self):
		while 1 == 1:
			dFL = distFL.distanceFL()
			print("Distance(FL): " + str(dFL) + "cm")

			if dFL >= 71 and dFL <= 200:
				vib.secPulse()
				print("Your FL distance in cm is" + " " + str(dFL))
			elif dFL >= 30 and dFL <= 70:
				vib.quarterPulseFL()
				print("Your FL distance in cm is" + " " + str(dFL))
			elif dFL <= 29:
				vib.PulseFL()
				print("Your FL distance in cm is" + " " + str(dFL))
			elif dFL > 200:
				vib.StopPulsingFL()
				print("Out of bounds! Safe!!")

class FRPollingClass(Thread):
	def __init__(self):
		Thread.__init__(self)
		self.daemon = True
		self.start()
	def run(self):
		while 1 == 1:
			dFR = distFR.distanceFR()
			print("Distance(FR): " + str(dFR) + "cm")

			if dFR >= 71 and dFR <= 200:
				vib.secPulseFR()
				print("Your FR distance in cm is" + " " + str(dFR))
			elif dFR >= 30 and dFR <= 70:
				vib.quarterPulseFR()
				print("Your FR distance in cm is" + " " + str(dFR))
			elif dFR <= 29:
				vib.PulseFR()
				print("Your FR distance in cm is" + " " + str(dFR))
			elif dFR > 200:
				vib.StopPulsingFR()
				print("Out of bounds! SAFE!!!"

FLPollingClass()
FRPollingClass()
while True:
	pass
