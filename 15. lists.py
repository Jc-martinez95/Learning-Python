#Curso Bro code https://www.youtube.com/watch?v=XKHEtdqhLK8
    # list = se usa para guardar varios items en una sola variable.

#Para crear una lista, hay que tener una variable y dentro de ella, encerrar los str en brackets[ y separados con comas
comida = ["pizza", "Hot-dog", "Hamburguesa",]
print(comida)#si solo imprimo la variable, me mostrará los datos tal y como los escribí, incluyendo los brackets.
#Aquí cambié el valor del primer elemento de la lista, osea pizza por sushi usando v[0 = "nuevo valor
comida[1] = "sushi"
#Para mostrar un elemento en concreto tenemos que poner en brackets dentro de la variable a imprimir, el numero de elemento en el indice.
print(comida[1])
#con la subfuncion .append puedo agregar otro elemento a la lista
comida.append("Tacos")
print(comida)
 #con la subfunción .remove puedo eliminar un elemento de la lista
comida.remove("pizza")
print(comida)
 #con la subfunmcion .pop() elimino el ultimo elemento de la lista
comida.pop()
print(comida)
 #podemos insertar un valor en una lista con .insert, en el primer campo elegimos el espacio donde queremos insertar, y enel segundo campo insertamos el valor en str
comida.insert(0, "Gorditas")#no reemplaza
print(comida)
 #Con .sort puedo barajear la lista y mostrarla después en random
comida.sort()
print(comida)

 #para mostrar la lista completa, debo colocar un for loop
for i in comida:
    print(i)

 #con .clear elimino todo el contenido de una lista
#por lo tanto no se imprimirá la lista
comida.clear()
print(comida)