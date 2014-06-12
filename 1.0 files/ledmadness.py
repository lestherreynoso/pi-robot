import time
import RPi.GPIO as gpio

ledEnable = 1
ledDisable = 0
rgbEnable = 1
rgbDisable = 0

#LED PIN CONFIGURATION
ledred = 7
ledblue = 12 
ledgreen = 11
ledyellow = 16
rgbred =  18  #15
rgbgreen = 13 #18
rgbblue = 15 #13

#GROUP THE LED PINS
LED = [ledred, ledblue, ledgreen, ledyellow]
RGB = [rgbred, rgbgreen, rgbblue]

#RGB COLORS
RED = [rgbred]
GREEN = [rgbgreen]
BLUE = [rgbblue]
CYAN = [rgbblue, rgbgreen]
MAGENTA = [rgbblue, rgbred]
YELLOW = [rgbgreen, rgbred]
WHITE = [rgbred, rgbblue, rgbgreen]



def ledSetup():
    #SETS UP THE BOARD FOR WIRING
    gpio.setmode(gpio.BOARD)
   #print 'enabling..'
    #SETS UP EACH LED PIN FOR OUTPUT
    for i in LED:
        gpio.setup(i, gpio.OUT)
      #  print i 
    for i in RGB:
        gpio.setup(i, gpio.OUT)
       # print i 

def ledActivate(led):
    #TURNS ON THE LED COLOR OF CHOICE
    gpio.output(led, ledEnable)

def rgbActivate(color):
    #ACTIVATES THE COLOR  FOR THE RGB
    for i in color:
        gpio.output(i, rgbEnable)

def ledDeactivate(led):
    gpio.output(led, ledDisable)

def rgbDeactivate(color):
    for i in color:
        gpio.output(i, rgbDisable)

def ledClear():
   # print 'clearing..'
    for j in LED:
        gpio.output(j, ledDisable)
       # print j 
    for j in RGB:
        gpio.output(j, rgbDisable)
       # print j

def main():
    ledSetup()      #SET UP ALL THE PINS
    ledClear()      #SET THEM ALL TO LOW
    
    ledActivate(ledred)     #TURN ON RED LED
    time.sleep(1)          #WAIT HALF A SECOND
    ledDeactivate(ledred)
    
    ledActivate(ledblue)
    time.sleep(1)
    ledDeactivate(ledblue)
    
    ledActivate(ledyellow)
    time.sleep(1)
    ledDeactivate(ledyellow)
    
    ledActivate(ledgreen)
    time.sleep(1)
    ledDeactivate(ledgreen)
    
    time.sleep(1)

    ledActivate(ledred)
    ledActivate(ledblue)
    ledActivate(ledgreen)
    ledActivate(ledyellow)
    time.sleep(1)
    ledDeactivate(ledred)
    ledDeactivate(ledblue)
    ledDeactivate(ledgreen)
    ledDeactivate(ledyellow)
    


    for i in range(0, 1):
        
        rgbActivate(RED) #blue
        time.sleep(1)
        rgbDeactivate(RED)
        time.sleep(1)
        
        rgbActivate(BLUE) #green
        time.sleep(1)
        rgbDeactivate(BLUE)
        time.sleep(1)
        
        rgbActivate(GREEN) #red
        time.sleep(1)
        rgbDeactivate(GREEN)
        time.sleep(1)

        rgbActivate(YELLOW) #YELLOW
        time.sleep(1)
        rgbDeactivate(YELLOW)
        time.sleep(1)

        rgbActivate(MAGENTA) #MAGENTA   
        time.sleep(1)
        rgbDeactivate(MAGENTA)
        time.sleep(1)

        rgbActivate(CYAN) #CYAN
        time.sleep(1)
        rgbDeactivate(CYAN)
        time.sleep(1)
       
        rgbActivate(WHITE) #WHITE
        time.sleep(1)
        rgbDeactivate(WHITE)
        time.sleep(1)

    ledClear()
    gpio.cleanup()

main()    
