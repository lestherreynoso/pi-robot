import time
import RPi.GPIO as GPIO

brakes = 0
headlights = 0
GPIO.setmode(GPIO.BOARD)

def ledSetup(b, h):
	global brakes
	global headlights
	brakes = b
	headlights = h

	GPIO.setup(brakes, GPIO.OUT)
	GPIO.setup(headlights, GPIO.OUT)

def brakesON():
	GPIO.output(brakes, 1)

def headlightsON():
	GPIO.output(headlights, 1)

def brakesOFF():
	GPIO.output(brakes, 0)
def headlightsOFF():
	GPIO.output(headlights, 0)