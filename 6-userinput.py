#Curso Bro code https://www.youtube.com/watch?v=XKHEtdqhLK8
#Vamos a crear inputs que un usuario puede dar con la funcion input
name = input("¿Cúal es tu nombre? ") #La variable name equivale a input ya que es el usuario quien define la variable al escribir
#Fijate que aqui abajo  tengo que convertir la variable tipo str "" a int, ya que quiero que el usuario nos proporcione un numero
#si no hiciera lo anterior, daria error, como esto age = input("cuantos años tienes?)
age = int(input("Cuantos años tienes?"))#Fijate que el input que el usuario debe darnos debe ser un int (numero entero), sino da error al correr el codigo
print("Tú te llamas " + name)
print(" y tienes " + str(age) + " de edad")
height = float(input(" Y cuanto mides?"))
print("y efectivamente mides " + str(height) + " cm de altura")