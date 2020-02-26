import RPi.GPIO as GPIO
import time
import distFL
import distFR
import vib

while 1 == 1:
        dFR = distFR.distanceFR()
#        print("Distance(FR): " + str(dFR) + "cm")
	time.sleep(0.5)
        if dFR >= 71 and dFR <= 200:
                vib.secPulseFR()
#               print("Your FR distance in cm is" + " " + str(dFR))
        elif dFR >= 30 and dFR <= 70:
                vib.quarterPulseFR()
#                print("Your FR distance in cm is" + " " + str(dFR))
        elif dFR <= 29:
                vib.PulseFR()
#                print("Your FR distance in cm is" + " " + str(dFR))
        elif dFR > 200:
                vib.StopPulsingFR()
#                print("Out of bounds! Safe!!")

