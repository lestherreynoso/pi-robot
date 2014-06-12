''' Temperature Sensor'''

import time
import os

os.system('modprobe w1-gpio')
os.system('modprobe w1-therm')

filedir = '/sys/bus/w1/devices/28-000005b5b540/w1_slave'

def tempReading():
	file = open(filedir, 'r')
	filelines = file.readlines()
	file.close()
#loop would get skipped if all is working fine
'''
	while filelines[0].strip()[-3] != 'YES': #while the temperature sensor didnt get a reading
		time.sleep(0.5)			#sleep for half a second
		tempReading()			#then try to get a reading again.
'''
#we assume we got a reading at this point
	equalsign = filelines[1].find('t=')
'''
#look for the position number of the two characters
#before the value in the second line of the lines 
#variable which we created from the file
'''	
#check would get skipped if all is working fine
	if equalsign == -1:
#if for some reason we get a yes in the previous line but there is no value for the temperature
#sleep for a bit then try again
		time.sleep(0.5)
		tempReading()
	tempstring = filelines[1][equalsign+2:]
	return tempstring
'''
	celcius = float(tempstring) / 1000  
	farenheit = celcius * (9.0/5.0) + 32	
'''
def tempF():
	return tempC() * (9.0/5.0) +32

def tempC():
	tempstring = tempReading()
	return float(tempstring) / 1000

try:
	while True:
		print tempC(), tempF()
except KeyboardInterrupt:
	print 'Okay i will stop now, sadness.'

