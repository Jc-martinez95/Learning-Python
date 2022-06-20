#Curso Bro code https://www.youtube.com/watch?v=XKHEtdqhLK8
# loop control statements = cambia la ejecución de un loop de su secuencia normal
    # break = se usa para terminar el loop en su totalidad
    # continue = salta la siguiente iteración del loop
    # pass = no hace nada u omite cierta iteracion.

#mientras sea verdad lo de abajo se seguirá loopeando. recuerda escribir True con mayúscula la primera letra

while True: #primero debes colocar el while True
    name = input("como te llamas?") #despues la variable y su input
    if name != "": #escribo una condicion. != significa no es igual a...
         break#con break si la condicion anterior es verdadera, se termina el loop

# Ahora quiero indexar solo los numeros del siguente telefono

cel = "123-456-789"
#para quitar los guiones y que me muestre el numero hago lo siguiente
for i in cel: #creo un indice para el numero de telefono
     if i == "-":#dentro del indice hago una condicion, si el indice es igual a un guion, entonces continua
        continue#con continua, skipeo y salto a lo demás
     print(i, end="")#aqui pido que muestre el indice, y con end="" le pido que lo muestre en una sola linea de codigo..
    #si yo pusiera algo dentro de end="" como end="g", pondría letras G entre cada numero


#Ahora quiero eliminar un dato del indice o skipearlo por completo, para eso uso pass
for j in range(1,21):#quiero mostrar un rango del 1 al 20 (No olvidar los dos puntos) y recuerda que el segundo numero es exclusivo
      if j == 13:#si en el indice aparece el numero 13, entonces...
         pass#Pásalo, omitelo
      else:
        print(j)
            #para todo lo demás, imprime el indice con else

