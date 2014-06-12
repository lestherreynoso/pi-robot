'''Motion Sensor Test'''

import motionSensor as mS
import RPi.GPIO as GPIO
import time

pinnumber = 24

mS.PIRSetup(pinnumber)

try:
	while True:

		
		if mS.PIRReading():
			now = time.time()
			while mS.PIRReading():
				then = time.time()
			diff = now - then
			print diff, "second long high pulse"

		
except KeyboardInterrupt:

	print "OKAY OKAY im done now"
	GPIO.cleanup()
