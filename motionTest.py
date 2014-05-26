'''Motion Sensor Test'''

import motionSensor as mS
import RPi.GPIO as GPIO
import time

pinnumber = 3

mS.PIRSetup(pinnumber)

try:
	while True:
		print GPIO.input(3)
		'''
		if mS.PIRReading():
			now = time.time()
			while mS.PIRReading():
				then = time.time()
			diff = now - then
			print diff, "second long high pulse"
		else:
			print GPIO.input(3)
		'''
except KeyboardInterrupt:

	print "OKAY OKAY im done now"
	GPIO.cleanup()
