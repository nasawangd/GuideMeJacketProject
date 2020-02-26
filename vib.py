import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BOARD)

# Setting up the front left vibrator
vibratorFL = 12
GPIO.setup(vibratorFL, GPIO.OUT)

# Now for the definitions:
# Steady Pulsing for FL vibrator
def PulseFL():
	GPIO.output(12, GPIO.HIGH)
# Stop Pulsing for FL vibrator
def StopPulsingFL():
	GPIO.output(12, GPIO.LOW)
# Quarter Second intervals for FL vibrator
def quarterPulseFL():
	time.sleep(0.25)
	PulseFL()
	time.sleep(0.25)
	StopPulsingFL()
# 1 second interval pulse for FL vibrator
def secPulseFL():
	time.sleep(1)
	PulseFL()
	time.sleep(1)
	StopPulsingFL()

# Setting up the front right vibrator
vibratorFR = 32
GPIO.setup(vibratorFR, GPIO.OUT)

# Now for the definitions:
# Steady Pulsing for FR vibrator
def PulseFR():
	GPIO.output(32, GPIO.HIGH)
# Stop Pulsing for FR vibrator
def StopPulsingFR():
	GPIO.output(32, GPIO.LOW)

# Quarter Second vibrations for FR motor:
def quarterPulseFR():
	time.sleep(0.25)
	PulseFR()
	time.sleep(0.25)
	StopPulsingFR()
# 1 Second interval pulse for FR motor:
def secPulseFR():
	time.sleep(1)
	PulseFR()
	time.sleep(1)
	StopPulsingFR()

#-------------------------------------

vibratorRear = 36
GPIO.setup(vibratorRear, GPIO.OUT)

# Steady Pulsing for R vibrator
def PulseR():
	GPIO.output(36, GPIO.HIGH)
# Stop Pulsing for R vibrator
def StopPulsingR():
	GPIO.output(36, GPIO.LOW)

# Quarter Second vibrations for R motor:
def quarterPulseR():
	time.sleep(0.25)
	PulseR()
	time.sleep(0.25)
	StopPulsingR()
# 1 Second interval pulse for R motor:
def secPulseR():
	time.sleep(1)
	PulseR()
	time.sleep(1)
	StopPulsingR()
