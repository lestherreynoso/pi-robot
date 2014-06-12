import RPi.GPIO as GPIO , time

#must be called prior to any other function to assign the pin value

PR = 0
GPIO.setmode(GPIO.BOARD)

count = 0 

def photoresistorSetup(lightSensor):
    global PR 
    PR = lightSensor
	
def reading():
    value = 0
    GPIO.setup(PR, GPIO.OUT)
    GPIO.output(PR, GPIO.LOW)
    time.sleep(.1)
    GPIO.setup(PR, GPIO.IN)
    while (GPIO.input(PR) == GPIO.LOW):
        value += 1

    return value


