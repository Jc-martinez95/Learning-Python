""" Curso Bro Code https://www.youtube.com/watch?v=XKHEtdqhLK8
"""
# Random numbers = vamos a crear pseudo random numeros

# Primero importamos el módulo random

import random

print(random.randint(10,50)) #Para mostrar numeros int al azar hay que usar la subfuncion random.randint(1,20) y especificar el rango
print(random.random()) #con random.random() mostramos un numero float con decimales al azar


#si quiero mostrar al azar elementos o str de una lista, tengo que usar la subfuncion random.choice()
# y colocar la lista o variable que contiene los elementos de la lista. en este caso usaré piedra, papel o tijeras

juego = ["Piedra","Papel","Tijera"]
print(random.choice(juego))
#Tambien puedo barajear o reborujar datos de una lista con subfuncion random.shuffle(v).
#primero creo una lista
baraja = ["A",1,2,3,4,5,6,7,8,9,10,"J","Q","K"]
random.shuffle(baraja)#luego uso la subfuncion
print(baraja)#imprimo

#si quiero mostrar los datos fuera de los brackets, tengo que crear un for loop
for i in baraja:
    print(i, end=", ")