#Curso Bro code https://www.youtube.com/watch?v=XKHEtdqhLK8
# for loop = es una declaracion que se ejecutara una limitada cantidad de veces-

            #while loop = sin limites
            #for loop = con limites

#el primer campo me indica de donde comienzo, el segundo donde termino, y el tercero los pasos o de cuanto en cuanto contar
for a in range(0,10,1):
    print(a)#range me indica un rango de numeros
print("")#aqui estoy diciendo que la variable i se repetira en un rango de 10 (osea contará 10 veces)
    # como la variable i no tiene valor asignado, python lo asigna como del 0 al 9 ya que es exclusivo



#aqui le digo que haga lo mismo pero sumando uno, así me muestra un loop del 1 al 10
for b in range(1,11,1):
    print(b, end="")
print("")
#aqui el primer numero es inclusivo (osea si se incluye); y el segundo, exclusivo
for c in range(50,100,1):     #solo imprimira del 50 al 99
    print(c)
#a continuacion haré lo mismo, pero colocando un tercer campo que son los numeros de pasos a contar.
for d in range(50,100+1,10): #aqui mostrará del 50 al 100, ya que agregamos 1, y de 10 en 10
    print(d)
print("")#en el tercer campo coloco el numero de pasos o cada cuanto contar, en este caso de dos en dos

#A continuacion voy a sortear y hacer un loop para que me muestre cada una de las letras de mi apellido
for e in "Martinez":#recuerda poner los dos puntos al final
    print(e)
#Acá abajo voy a crear un programa de cuenta regresiva

#primero importo el módulo de tiempo, import time lo cual me dará acceso a funciones relacionadas al tiempo
import time
for f in range(10,0,-1): #aqui hago un for loop en rango de 10 al cero, y el -1 significa que haré la cuenta al reves
    print(f)
    time.sleep(1) #aqui digo cuantos segundos voy a avanzar en cada paso del loop, osea cada segundo
print("Despierta!!")
print("")
#ahora de 90 a 100 de dos en dos, cada dos segundos
for g in range(90,101,2):
    print(g)
    time.sleep(2)
print("feliz año nuevo!!")