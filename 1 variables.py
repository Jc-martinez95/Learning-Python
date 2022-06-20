#CURSO BRO CODE https://www.youtube.com/watch?v=XKHEtdqhLK8
# Tipos de DATA (Variables)
#Variables tipo str(caracter), int(numero entero), float(numero decimal) y bool (True o False)
#NUM.1 print es una funcion que sirve para imprimir texto y mostrarlo en el output

print("Hola")

# NUM.2 variables.

name = "Juan" #str
age = 27 #int
height = 183.5 #float
#name es una variable tipo STRING "str". "Juan" es el valor de la variable.
#String o str es solo un conjunto de caracteres.
#para mostrar una variable como texto en output tenemos que:
print(str(age))
#Asegurate de no poner la variable con comillas. En cambio puedes combinar texto en comillas y variables con el signo de + así:
print("hola " + name)
#para saber que tipo de clase es un cierto texto de codigo podemos usar print(type(name))
print(type(height))

primer_nombre = "Juan "
segundo_nombre = "Martinez "
#aca arriba tengo dos variables, mi nombre y mi segundo nombre. luego abajo quiero combinarlos en una variable que se llama full_name
#recuerda el uso del signo + y las comillas para crear espacio al combinar variables
full_name = primer_nombre + segundo_nombre
#aqui lquiero mostrar en la consola un texto "Hola" y mi nombre competo
print("Hola " + full_name)
#aquí obtuve el mismo resultado pero con más código
print(primer_nombre + segundo_nombre)
# NUM.3 INTENGER (int) significa un numero entero y aqui se muestra en azul. OJO (no usar comillas)

edad = 27
edad_2 = 27.5
#recuerda no concatenar o unir dos tipos distintos de clases. str no puede unirse con int
#por ejemplo print("yo tengo "+age) ESTO ES ERROR

 #aqui si puedo unir str con int porque especifico que quiero que age se muestre como un str
print("tengo " + str(edad_2) + " años")

#NUM.4  FLOAT (float) (floating point number) es un numero decimal
altura = 183.5
 #este valor es un float (un numero con decimales)
print(type(altura))
print("mido " + str(altura) + " cm de altura")


#NUM5. BOOLEAN (bool) (verdadero o falso) en naranja
 #recuerda usar la primera letra en mayúscula para que la distinga de una variable
 #no uses comillas y recuerda la mayúscula
humano = True
perro = False
print(humano)
print(perro)
print("Eres un perro?= " + str(perro))
print("Eres un humano?= " + str(humano))
#NUM. 5 Multiple assigment = nos permite asignar multiples variables al mismo tiempo en una sola linea de codigo
nombre = "Daniel"
edad = 25
altura = 180.5
inteligencia = False

#arriba tengo los datos en tres lineas de codigo, si quiero definir distintas variables y clases en una sola linea uso comas
nombre, edad, altura, inteligencia = "Daniel", 25, 180.5, False
print("Hola, me llamo " + nombre)
print("Tengo " + str(edad) + " años, y mido " + str(altura) + " de altura")
print("Soy inteligente?= " + str(inteligencia))
#tambien puedo agruparlos usando el signo de igual para cada variable y al final poner el valor para todos(solo usar si se repiter un valor
juan = maria = pepe = luis = 40

print(maria)
print(pepe + maria)