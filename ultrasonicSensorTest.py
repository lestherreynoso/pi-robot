'''Ultrasonic Sensor test'''

import ultrasonicSensor as uS, RPi.GPIO as io, time

t = 15
e = 7
uS.uSensorSetup(t, e)

try:
	while True:
		print uS.distance()
		time.sleep(1)

except KeyboardInterrupt:
	print 'no more distance for you'
	io.cleanup()
