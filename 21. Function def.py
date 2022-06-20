# Curso Bro code https://www.youtube.com/watch?v=XKHEtdqhLK8
# functions = Es un bloque de código que solo se ejecuta cuando es llamado. Son útiles para no repetir bloques de código

# A continuacion voy a definir una funcion, se llamará hello()
def hello(): #los pasos son usar def y despues el nombre de la funcion + tuples = def hello():
    print("Hello") #dentro de la función tengo que definir lo que quiero que realize cuando se le invoque
hello() # Aquí estoy invocando esa funcion, la funcion hello() por lo que imprimirá su bloque de código dentro de ella


print("")
# Puedo hacer 2 mas operaciones dentro de la funcion def
def greetings():
    print("Saludos")
    print("Cómo están?")
greetings()
# y tambien puedo asignar un valor temporal a la variable de la funcion así
def goodbye(name): #aquí añado una variable temporal dentro del parentesis de la funcion def
     print("adios " + name)# uso esa variable dentro de la funcion para mostrarlo en la consola
     print("que te vaya bien" + name)
goodbye("Juan")
 #Aquí definí la variable temporal
# OJO: el numero de valores debe corresponder al número de variables que se añaden en la funcion def.
# por ejemplo def goodbye(name):
#               print(name)
# goodbye("Juan", "Carlos")
# lo de arriba me dará error, ya que asigné dos valores que voy a añadir a la variable temporal
# pero la funcion solo tiene una variable temporal y no dos.
# en conclusion, si se quieren añadir dos valores, hay que usar dos variables en def goodbye()
# a los valores que se asignan temporalmente son llamados ARGUMENTS
# y a las variables temporales que corresponden a cada uno de esos valores se llaman PARAMETERS
# OJO: recuerda añadir comas para separar Arguments y Parameters.

def saludos(nombre, edad, altura, apellido): #aquí cree 4 variables temporales o parameters
    print("Hola " + nombre + " " + apellido + " cómo estás?")    #acá las uso como quiera
    print("así que tienes " + str(edad) + " años y mides " + str(altura) + " cm")

# y acá abajo además de invocar la función, cree 4 valores o argumentos, uno para cada variable o parameter.
# OJO: si no coinciden el numero de arguments con los de parameters, dará error el sistema
saludos("Juan", 27, 184.3, "Martinez")
