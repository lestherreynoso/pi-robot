import RPi.GPIO as io
import time

io.setmode(io.BOARD)
io.setup(7, io.OUT)
p = io.PWM(7, 50)
p.start(0)
try:
	while True:
		for i in range(100):
			p.ChangeDutyCycle(i)
			time.sleep(0.02)
		for i in range (100):
			p.ChangeDutyCycle(100-i)
			time.sleep(0.02)
except KeyboardInterrupt:
	p.stop()
	io.cleanup()
	print 'were good'
