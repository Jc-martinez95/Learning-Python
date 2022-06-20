#Curso Bro code https://www.youtube.com/watch?v=XKHEtdqhLK8
    #2D lists = una lista de otra lista, o tambien llamados listas multidimensionales

#primero creamos varias listas.
comida = ["huevo", "frijoles", "arroz", "carne"]
bebida = ["agua", "jugo", "leche", "café"]
utensilios = ["tenedor", "cuchara", "servilleta"]
#ahora añadimos todas las listas en una sola lista
cocina = comida, bebida, utensilios #aqui añado las variables o las listas completas, separados con coma
print(cocina)#si solo imprimo la variable food, me aparecerá con todo y brackets
#con brackets dentro de la variable a imprimir,  ya especifico que elemento dentro de la lista quiero mostrar.
# el primer bracket es el numero de lista
#y el segundo bracket es el elemento dentro de esa lista (OJO no poner comas y tener los brackets separados)
print(cocina[1][1])
#solo por el afán de practiccar, cree abajo un indice
for i in cocina:
    print(i)
