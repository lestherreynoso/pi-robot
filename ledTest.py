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
