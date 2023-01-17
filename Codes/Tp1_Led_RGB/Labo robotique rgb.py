from machine import Pin
import time
#test sa mère

R = Pin(19, Pin.OUT)
B = Pin(16, Pin.OUT)
G = Pin(17, Pin.OUT)

Bt1 = Pin(16, Pin.IN)
Bt2 = Pin(17, Pin.IN)

increment = 0 #Incrémentation qui varie de 0 à 2. Cela permettra d'obtenir 3 états (allumage de chaque led)."


def val_Bt(): #"Fonction qui vient vérfier la valeur des boutons."
    
    val_Bt1 = Bt1.value()
    val_Bt2 = Bt2.value()
    
    if val_Bt1:
        time.sleep(500)  #"Modification du temps d'arrêt du bouton pour pas que ça aille trop vite."
    
    return val_Bt1, val_Bt2

def led_on(increment):  #"Fonction qui commande l'allumage des leds "
    if increment == 0:
        R.value(1)      #"led rouge on"
        G.value(0)
        B.value(0)
        
    if increment == 1:
        R.value(0)      #"led verte on"
        G.value(1)
        B.value(0)
    
    if increment == 2:
        R.value(0)      #"led Bleue on"
        G.value(0)
        B.value(1)
        
    increment += 1
    if increment > 2:    #"Reset de l'incrementation"
        increment = 0
    
    return increment
        
def led_off():     #"fonction qui s'occupe d'éteindre les leds"
    R.value(0) 
    G.value(0)
    B.value(0) 
    return
    
while True:            # "Boucle principale du programme"
    time.sleep_ms(50)
    
    Btv1 = val_Bt()[0]    #"on vient chercher les valeur des deux boutons"
    Btv2 = val_Bt()[1]
    if Btv1 == True:     # "appel à la fonction d'allumage"
        led_on(increment)
        
    if Btv2 == True:
        led_off()        #"appel à la fonction de mise en off des leds"
        increment = 0
    

