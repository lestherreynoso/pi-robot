# '''RES Controller'''
# import motion
# import wheels
# import light
# import leds
# import distance
# import servo
# import time
# import RPi.GPIO as GPIO
# '''SETUP ALL THE PINS'''
# #ultrasonic
# trig = 11
# echo = 13
# #photoresistor
# pr = 7
# #gear motors
# left1 = 8
# left2 = 10
# right1 = 3
# right2 = 5
# #motion sensor
# motioning = 15
# #LEDs
# brakes = 18
# headlights = 16
# serv = 12

# distance.uSensorSetup(trig, echo)
# servo.pinSetup(serv)
# light.photoresistorSetup(pr)
# wheels.motorPins(left1, left2, right1, right2)
# motion.PIRSetup(motioning)
# leds.ledSetup(brakes, headlights)

#########################################################################

#########################################################################


def main():
	print "Welcome to the RES 2.0 Controller"
	response = raw_input("To test each component indivually type 'test': ")
	if response == "test":
		testing()
	else:
		print "you did not enter test"

def testing():
	components = {
	"brakes" 	:brakes,
	"headlights":headlights,
	"wheels" 	:wheels,
	"distance" 	:distance,
	"motion" 	:motion
}
	print "What would you like to test?"
	print "(brakes, headlights, wheels, distance, motion)"
	component = input("enter one of the above: ")
	components[component]()


def brakes():
	print "You are testing the brake lights"
def headlights():
	print "You are testing the headlights"
def wheels():
	print "You are testing the wheels"
def distance():
	print "You are testing distance getting"
def motion():
	print "You are testing the motion detection"


main()








# print "forward"
# ss.forward()
# time.sleep(1)
# print "left"
# ss.left()
# time.sleep(1)
# print "right"
# ss.right()
# time.sleep(5)
# print "forward again"
# ss.forward()
# time.sleep(2)

"""
'''turn light on'''
def lightON():
	lM.rgbActivate(lM.WHITE)
'''turn light off'''
def lightOFF():
	lM.rgbDeactivate(lM.WHITE)
'''flash green'''
def flashGreen():
	for i in range(5):
		lM.rgbActivate(lM.GREEN)
		time.sleep(.1)
		lM.rgbDeactivate(lM.GREEN)
		time.sleep(.1)
'''brake lights on'''
def brakeLightsON():
	lM.ledActivate(rearr)
	lM.ledActivate(rearl)
'''brake lights off'''
def brakeLightsOFF():
	lM.ledDeactivate(rearr)
	lM.ledDeactivate(rearl)"""
###########################################################################
#TESTING PURPOSES#
###########################################################################

for i in range(5):
	'''
	lM.redON()
	time.sleep(1)
	lM.redOFF()
	lM.blueON()
	time.sleep(1)
	lM.blueOFF()
	lM.greenON()
	time.sleep(1)
	lM.greenOFF()
	lM.whiteON()
	time.sleep(1)
	lM.whiteOFF()
	lM.brakesON()
	time.sleep(1)
	lM.brakesOFF'''
'''
print 'testing motors'
mC.reverse()
time.sleep(2)
mC.off()
''''''
print 'testing brake lights'
for i in range(5):	
	brakeLightsON()
	time.sleep(.2)
	brakeLightsOFF()
	time.sleep(.2)

print 'testing the color white'
for i in range(5):	
	lightON()
	time.sleep(.2)
	lightOFF()
	time.sleep(.2)

print 'testing the color green'
for i in range(5):	
	flashGreen()

print 'testing the ultrasonic sensor'
for i in range(5):
	print  round(getDistance(), 2), 'cm'
	time.sleep(0.2)
print 'testing light'


print 'testing the temperature'
for i in range(5):
	print 'Fahrenheit: ', tS.tempF(), ' Celcius: ', tS.tempC()

for i in range(5):
	if pM.lightLevel() == 'Low':
		print 'low'
		lightON()
	else:
		if pM.lightLevel() =='High':
			print 'high'
			lightOFF()
	time.sleep(2)


'''

ss.p.stop()
GPIO.cleanup()

######################################################################
#
######################################################################
