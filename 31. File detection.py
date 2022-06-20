""" Curso Bro Code https://www.youtube.com/watch?v=XKHEtdqhLK8 """

# Para detectar si un archivo o ubicacion o carpeta existe, debemos importar el módulo os

import os

path = "D:\Data analyst\Excel\Projects\Excel Project Dataset - Bike Sales.xlsx" # una vez importado el modulo, creamos una variable con la ubicacion o path

if os.path.exists(path): # creamos una condicion que sea if os.path.exists(v) y dentro colocamos la variable
    print("Esta ubicacion si existe") # Imprimimos un mensaje si es verdadero
    if os.path.isfile(path): # para saber si la ubicacion es un archivo, escribimos if os.path.isfile(v)
        print("Es un archivo")
    elif os.path.isdir(path): #Para saber si la ubicación es un directorio o carpeta, if os.path.isdir(v)
        print("Es una carpeta")
else: #usamos else si no es verdadero
    print("Esta ubicacion no existe") #e imprimimos un mensaje