# Curso Bro code https://www.youtube.com/watch?v=XKHEtdqhLK8
# index operator [] = dan acceso a elementos de una secuencia (str, list, tuples, int, etc)

# A continuacion voy a cambiar la primera letra de un str de minusculas a mayusculas
name = "juan Martinez" #primero creamos una variable de cualquier clase
# luego creamos una condición, dentro de esta condicion debemos colocar la variable asi:
if name[0].islower():  # if (v[posicion en int donde se encuentra el dato en la secuencia].islower())
     name = name.capitalize()# despues escribir v = v.capitalize()
print(name)     # y por ultimo imprimimos la variable aparte

print("")
# Ahora quiero crear un substring de la primer parte de mi nombre o variable
# debo crear una nueva variable, debe ser v1.2 = v1[0:1]
apellido = name[5:]
# donde dentro de los brackets en el primer campo coloco donde quiero comenzar, y el segundo campo donde quiero terminar

 #por ultimo imprimo
print(apellido.capitalize())
# Si quiero imprimir mi apellido, solo busco el espacio donde quiero comenzar y terminar
# se puede dejar vacio el campo si queremos terminar hasta el final [1:]
first =name[0:4]
print(first)
# [1:] comienza a idexar del caracter 1 hasta el final
# [:5] comienza a indexar del caracter 0 hasta el 5
if name.istitle():
     name = name.lower()
print(first, apellido)

#crea una variable e imprime la ultima letra

