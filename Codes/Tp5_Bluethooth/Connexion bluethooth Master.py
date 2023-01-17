from machine import UART, Pin
import time
import json

uart1 = UART(0, baudrate = 38400, tx= Pin(0), rx=Pin(1)) # içi on définit la connection du module 
str2 = "lo"

while (True): # boucle principale du programme.
    
    uart1.write('Salut')    # Envoie du mot 'Hello' 
    print(uart1.read(5))    
    if uart1.any() > 0:     # lorsque la pin UARt 1 reçois une valeur autre que "0" c'est qu'il à reçu une information
        strBT = str(uart1.readline(),"utf-8") #lecture de l'information
        print(strBT)
        strSplit = strBT.split(";") # permet de séparer les mots au niveau des ";"
        print(strSplit[0])
        for x in range(len(strSplit)): 
            print(strSplit[x]) # Affichage l'information
    time.sleep(1)