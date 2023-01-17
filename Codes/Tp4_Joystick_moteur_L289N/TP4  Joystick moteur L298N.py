from machine import Pin, UART, PWM, ADC
import time

ENA = PWM(Pin(0)) # La modulation par impulsions (PWM) permet de moduler la vitesse en fonction de la valeur val_y.
ENA.freq(2000)
IN1 = Pin(1, Pin.OUT)
IN2 = Pin(2, Pin.OUT)

Vrx = ADC(Pin(26)) # Valeur analogique -> ADC 
Vry = ADC(Pin(27))

# Fonction qui convertit la valeur de la résistance de notre joystick en pourcentage. (Elle n'est utilisée que pour voir la différence de vitesse en pourcentage).

def scale_value (value,in_min,in_max,out_min,out_max):
    scaled_value = (value - in_min) * (out_max - out_min) / (in_max - in_min) + out_min 
    return scaled_value

while True:
    
    # Lecture et mise en variables des valeurs x et y du joystick. 
    
    val_y = Vrx.read_u16()  
    val_x = Vry.read_u16()
    
    print(val_y)
    time.sleep_ms(200) 

    if val_y <= 45000:
        ENA.duty_u16((-val_y)+65000) # Permet de moduler la vitesse du moteur (Forward).

        IN1.value(1)
        IN2.value(0)

        print(int(scale_value(y_value,0,45000,0,100))) # La vitesse est affichée en pourcentage à l'aide de "scale_value" (Forward).

    elif val_y >= 55000:
        ENA.duty_u16(val_y) # Permet de moduler la vitesse du moteur (marche arrière). 
        IN1.value(0)
        IN2.value(1)
        
        print(int(scale_value(y_value,50000,65535,0,100))) # La vitesse est affichée en pourcentage en utilisant "scale_value" (Backward).
        
    else:
        IN1.value(0)
        IN2.value(0)

