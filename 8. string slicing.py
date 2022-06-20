#Curso Bro code https://www.youtube.com/watch?v=XKHEtdqhLK8
# slicing es crear un substring al extraer elementos de otro string

# se puede hacer esto con indexing[] o con slice() (el slice es más complejo)
# al hacer slicing existen tres campos o argumentos que debemos de llenar, estos son:
# [start:stop:step] que depende de cuando y como queremos cortar o slice el substring
name = "Daniel martinez"
first_letter = name[0] #aqui indexé, quiere decir que le pedí a python que me mostrará el caracter 0, osea la primera letra
first_name = name[0:6] #aqui le pedi el primer campo que comience la indexación del valor 0 al 7. el primer nombre.
last_name = name[7:16] #aqui le pedi al primer campo que comience la indexacion del valor 7 al 16. el apellido.
# OJO: si hago esto [:7] el codigo asume que quiero comenzar del valor 0 hasta el valor 7
# OJO: si hago esto [7:] el codigo asume que quiero comenzar del valor 7 hasta el final
# OJO: en el campo stop, el valor es exclusivo, osease que el valor 0 no es nada, el valor 1 ES EL PRIMER CARACTER, por lo que hay que sumar 1 a los valores de los caracteres originales
print(first_letter)
print(first_name)
print(last_name)

#ahora voy a indexar usando el tercer campo step. step sirve para brincar de caracter al indexar y mostrar resultados
funky_name = name[0:6:2] #por defecto step es igual a 1 por lo que mostrará todos los caracteres
print(funky_name)

funky_name = first_name[0:6:2] #aqui solo mostrará cada segundo caractér del nombre
print(funky_name)
raro_name = name[::3] #aqui el programa asume que quiero empezar del primer caracter hasta el ultimo, y brincando cada 3 caracteres
print(raro_name)

reversed_name = name[::-1] #aqui indexé al reves, lo cual me muestra el nombre al reves
print(reversed_name)

#ahora quiero usar la funcion slice para indexar la siguiente url
website1 = "https://google.com" #quiero comenzar la indexacion en el espacio 7 y terminarlo en el espacio -4 (tiene que ser negativo ya que asi funciona la funcion slice, de manera negativa se cuenta de derecha a izquierda
website2 = "https://youtube.com"
slice1 = slice(8,-4) #el primer campo cuenta de izquierda a derecha y el segundo campo de derecha a izquierda (por eso negativo)
print(website1[slice1]) #para mostrarlo tengo que colocar [slice] dentro de la funcion de print, despues de la variable
print(website2[slice1])
slice2 = slice(0,-10)
print(website1[slice2])