# Curso Bro code https://www.youtube.com/watch?v=XKHEtdqhLK8

# keyword arguments = son argumentos precedidos por un identificador cuando los pasamos a una funcion..
#                 ...el orden de los argumentos no importa, contrario a los argumentos normales (alineados a statements)
#                 ...Python sabe el nombre de los argumentos que nuestra función recibe..

# Aquí abajo creo una funcion def normal con 3 statements y 3 argumentos posicionales
def hola(first,middle,last):
    print("hola " + first + middle + last)

hola("Juan ", "Carlos ", "Martinez") #aquí el orden de los argumentos si altera los statements y el resultado

#ahora voy a crear otra funcion def pero voy a añadir keywords a los arguments para identificarlos luego en el statement
def hola2(first,middle,last):
    print("hola " + first + middle + last + ", este es una funcion def con keyword arguments")
# A la hora de invocar la función, tengo que asignar cada argumento a su respectivo statement
#v1(statement2="arg2",statement3="arg3",statement1="arg1")
hola2(middle="Carlos ",last="Martinez",first="Juan ")# Al invocar, no importa el orden de los argumentos, mientras los definamos