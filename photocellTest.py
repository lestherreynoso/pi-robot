'''Photocell Test'''

import photocellManagement as pM, time
import RPi.GPIO as GPIO

pinnum = 5
pM.photoresistorSetup(pinnum)


try:
	#for i in range(50):
	while True:
		print pM.photoresistorReading()
		
		#print pM.average()
		#print pM.lightLevel()
	GPIO.cleanup()

except KeyboardInterrupt:
	print 'I just love being interrupted!!!'
	GPIO.cleanup()
