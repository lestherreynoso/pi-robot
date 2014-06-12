'''Motor Test'''

import motorControl as MC
import time 
import RPi.GPIO as GPIO

#pin assignments
LL = 0  #not currently working
LH = 16
RL = 0	#not currently working
RH = 12

MC.motorPins(LL, LH, RL, RH)
print 'Starting test..'
time.sleep(2)

MC.motorSetup()

print 'Testing both wheels forward'
#both wheels forward
MC.forward()
time.sleep(10)
MC.off()
print 'Testing Complete.. exiting in 2 seconds.'
time.sleep(2)
GPIO.cleanup()
