from hcsr04 import HCSR04 
from machine import Pin 
import time
import utime

sensor = HCSR04(trigger_pin=16, echo_pin=0) # On utilise içi une fonction dans le module hcsr04.
G = Pin(28, Pin.OUT)
R = Pin(27, Pin.OUT)
J = Pin(22, Pin.OUT)

while True:  # Boucle principale du code 
    
    distance = sensor.distance_cm() 
    print('Distance:', distance, 'cm')
    time.sleep_ms(50)
    
    # déifinition des conditions d'activation des leds. 
    
    if distance < 50:
        G.value(1)
    else :
        G.value(0)
    
    if distance < 30:
        R.value(1)
    else :
        R.value(0)
        
    if distance < 15:
        J.value(1)
    else :
        J.value(0)
    
    
        
    
    
        
    
        
        
        
    
    

