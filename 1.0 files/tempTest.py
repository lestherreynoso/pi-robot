'''Temp Sensor Test'''

import temperatureSensor as ts 

try:
	while True:
		print ts.tempC(), ts.tempF()
except KeyboardInterrupt:
	print 'Okay i will stop now, sadness.'
