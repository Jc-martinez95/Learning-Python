#nested loops = Es un loop o loops dentro de otros loops
    #El "inner loop" terminará todas sus iteraciones antes de que termine el "outer loop"

        #quiero crear una forma echa de simbolos, primero defino las variables.
filas = int(input("Cuantas filas? ")) #filas
columnas = int(input("cuantas columnas? ")) #columnas
simbolo = input("Inserta un símbolo para usar") #aqui no es int porque voy a insertar un simbolo

#Tengo que crear un indice para la variable fila y columna
for i in range(filas):#(outer for loop) primero creo un loop para las filas con la cantidad que especifique el usuario, recuerda usar la funcion range
    for j in range(columnas): #(inner for loop) luego creo un loop con distinta variable para las columnas con la cantidad que especifique el usuario
      print(simbolo, end="")   #Aqui imprimimos el simbolo en el inner for loop y colocamos la coma y end=" para cerrar el loop y que se muestr en un solo rango
    print()#aqui imprimimos el outer loop , pero no escribimos nada dentro del parentesis