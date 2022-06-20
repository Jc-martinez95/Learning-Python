# Curso Bro code https://www.youtube.com/watch?v=XKHEtdqhLK8
# return statement = Funciones para mandar  valores u objetos de Python de la funcion def, al al caller o invocador.
#                    Estos valores/objetos son conocidos como el valor de retorno de la funcion

# A continuacion voy a definir una variable def, de dos statements
 #def v(st1,st2):
def multiply(a,b):   # luego creo otra variable dentro, que se llame result y sea la multiplicacion de los dos statements
    result = a * b# result = # v2 = st1 * st2
     # Al final uso la funcion return para retornar al programa principal el resultado del codigo anterior
    return result# return v2 OJO no usar parentesis
# Esto hace que ahora cada vez que se invoque a la funcion, esa "invocacion" pasa a valer por si misma lo que la funcion
# ...def y al finalk return nos arrojó
print(multiply(8,6))
 # Quiere decir que esta invocacion de la funcion ahora vale 48.
#y ahora puedo usar esta invocacion con sus argumentos como si fuera una variable.
res = multiply(8,6)
# lo que falta por hacer es imprimir algo con esa variable cuyo resultado de la funcion retorno en si.
print(res + 2)#esto ya vale 48 por si mismo
print(multiply(5,2))

#incluso puedo usar esa variable retornada como valor de otra variable
print("el valor de la funcion def multiplicado por 2 es de " + str(res * 2))
# y lo puedo concatenar con otras clases
