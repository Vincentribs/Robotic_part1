from machine import ADC, Pin, PWM
import time

#Variables 

adc = ADC(Pin(26))
adc1 = ADC(Pin(27))

pwm0 = PWM(Pin(0))
pwm0.freq(1000)
SW= Pin(2, Pin.IN, Pin.PULL_UP)

#Boucle principale du code

while True:

    print(SW.value())
    val_x = adc.read_u16() #Lecture valeur x 
    val_y = adc1.read_u16() #lecture valeur y
    print(val_x)
    print(val_y)
    pwm.duty_u16(val_y)
    time.sleep_ms(1000)
    
    