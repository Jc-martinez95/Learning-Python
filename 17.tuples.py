#Curso Bro code https://www.youtube.com/watch?v=XKHEtdqhLK8

#   tuple = son como listas que están ordenados y no se pueden cambiar
#   usados para agrupar data similar

student = ("juan", 27, 183.5, "juan")#para crear tuplets tenemos que usar un parentesis dentro del valor de una variable ()
# con los tuples o parentesis, asigno varios valores a una misma variable, combinando distintas clases,str,int,float
print(student)
# con la subfuncion .count, puedo contar cuantas veces aparece un cierto valor dentro del tuplet.
# recuerda que tiene que ir despues del nombre de la variable, y usar parentesis con el dato que  quiero que busque y
# cuente. además de print para mostrarlo.
print(student.count("juan"))
#con .index puedo buscar el espacio del indice donde se encuentra el valor especifico que ando buscando.
print(student.index(27))
#si quiero mostrar en la consola todos los valores de la variable, tengo que crear una lista for loop
for i in student:
    print(i)
#ahora voy a usar una condicion, si mi nombre está en la lista tuplet, entonces que muestre lo siguiente
 #esta condicion tiene que ser if ""(lo que sea que esté buscando) in student (o variable):
for j in student:
    print(j)
print("")
#ahora quiero crear una condicion, si el numero 27 está en la variable
if 27 in student:           # print()
    print("juan si está en la lista")
