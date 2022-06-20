# Curso Bro code https://www.youtube.com/watch?v=XKHEtdqhLK8
# nested function calls = funciones dentro de otras funciones
#                         las funciones más dentro integradas se resuelven primero
#                         el valor retornado es usado como un argumento para la siguiente función externa

# num = input("insert
#Aca abajo primero se actua la funcion input, luego float, después abs, luego round y al final print
print(round(abs(float(input("inserta un número entero positivo: ")))))#5 funciones en una sola linea de código
