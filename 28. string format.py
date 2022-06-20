""" Curso bro code: https://www.youtube.com/watch?v=XKHEtdqhLK8

 str.format() = método opcional que da a los usuarios más control cuando se muestra el output de strings

"""
#aqui muestro un usual uso de strings, una pequeña frase con dos variables
a = "Juan"
b = "Brazil"
print("A", a, "le gusta viajar a", b)

print("")
#ahora voy a hacer algo similar con el str.format()
print("A {} le gusta viajar a {}".format("Juan","Brazil"))
# a la hora de imprimir debo de colocar curly braces {{ sobre los espacios donde quiero dar formato(poner un valor dado despues) dentro del string
 # y al final del string (aun dentro del parentesis coloco .format("str", "str")
# o mejor aun puede ser ("str {}..{}".format(v1, v2)
print("A {} le gusta viajar a {}".format(a,b))
"""OJO recuerda que el orden aqui si importa, y se insertaran sobre los curly braces en el orden que los pongas dentro del string format"""

#Pero que pasa si no quiero respetar el orden... entonces debo hacer lo siguiente
#debo de colocar dentro de los {} el numero de indice u orden donde estan colocados las variables o strings dentro del format. 0 es la 1° posicion, 1 la 2°, etc
 #positional argument
lugar = "México"
persona = "Paco"
profesion = "Médico"
print("{1} es de {2} y se dedica a {0}".format(profesion, persona, lugar))
print("")

#ya usamos positional arguments, ahora vamos a usar keyword argument. osea dentro del format colocamos keywords (key='value')
# y dentro de los {} debo escribir el key para que en el output me arroje en value o valor
print("A {persona} no le gusta comer {comida} durante el {temporada}".format(comida="camarones",temporada="invierno", persona="Maria"))
print("")

""" Incluso hay otra forma de usar string format, que es la siguiente"""

# Debemos crear una variable cuyo valor sea un string y además tenga {}.
pasa = "Mi pasatiempo favorito es {} con mi amigo {} y mi mascota {perro}"
#luego debemos de imprimir esa variable y darle formato.. print(v.format(arg1, arg2, kwarg1))
print(pasa.format("Jose","jugar futbol", perro="Azura"))
print("")
#Tambien puedo añadir espacio en el format field {} antes o despues de que se coloque el valor o string.

 #solo tengo que insertar {:4} para poner 4 espacios antes del dato
 # o {:2} para poner 2 espacios vacios despues de la palabra
#Incluso podemos alinear el string dentro del format field, como si de word se tratase, alinear a la izquierda, a la derecha, centrado, etc..
#eso se logra colocando < para alinear a la izquierda. > para alinear a la derecha. y ^ para centrarlo
name = "Wendy"
#recuerda colocar la alineacion asi {:<8}
print("Hola, les presento a {:<10}".format(name))
print("Hola, no les presento a {:>10}".format(name))
print("Hola, demos un fuerte aplauso a {:^12}".format(name))
# Y si quiero colocar un positional argument o keyword argument en específico y al mismo tiempo alinearlo?
#tienes que colocar simplemente el arg o kwarg antes de los dos puntos, así {0:<6} o {capital:>4}

print("La capital de {1:} es {0:,}, y tiene {capital} habitantes".format(30000,"Uruguay",capital="Montevideo"))
#OJO, el orden en el str.format() es arg y despues kwarg.
""" OJO, al parecer los espacios que asignemos en la alineacion deben ser mayores a el numero de caracteres o palabras
del valor del arg o kwarg que estemos colocando. si la palabra hola tiene 4 letras, nosotros debemos colocar más de 4, osease <>^5
para que surta efecto
"""
print("")
print("")

#Ahora vamos a dar formato a numeros. en este caso quiero que me muestre solo los dos primeros dígitos despues del punto de un numero.
# pi = 3.14159 #primero creo una variable
#en el format field {} hay que colocar punto ., luego la cantidad de digitos a tomar y luego una f despues de los dos puntos
# asi: {:.3f} toma 3 digitos despues del punto. y además redondea
pi = 3.14159
print("El número de Pi es {:.4f}".format(pi))
#con coma dentro del format field {:,} muestro una coma para convertir 10000 a 10,000 por ejemplo
num = 400000
print("Tenemos {:,} dólares en el banco".format(num))
# con {:.b} muestro el numero en su version binaria
print("la version binaria de {} es {:b}".format(num,num))


# {:o} para mostrar el numero en su version octal
print("La versión octal de {1:^20} es {0:o}".format(num,num))

# {:x} para mostrar la version hexadecimal en minuscula o {:X} para hexadecimal en mayúscula
print("La version hexadecimal de {:,} es {:X}".format(234292,num))
# {:e} para mostrar la version de notacion cientifica o {:E}
print("la versión cientifica de {} es {:e}".format(num+pi, pi))
