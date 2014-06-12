import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BOARD)
servo = 0
p = 0 
def pinSetup(s):
	global servo
	global p
	servo = s
	GPIO.setup(servo, GPIO.OUT)
	p = GPIO.PWM(servo, 50)
	p.start(7.5)

def forward():
	p.ChangeDutyCycle(7.5)	#1.5ms pulse to 90deg neutral
def right():
	p.ChangeDutyCycle(12.5)	#2.5ms pulse to 180deg
def left():
	p.ChangeDutyCycle(2.5)	#0.5ms pulse to 0deg
def forwardRight():
	p.ChangeDutyCycle(10)	#2ms pulse to 135deg 
def forwardLeft():
	p.ChangeDutyCycle(5)	#1ms pulse to 45deg

