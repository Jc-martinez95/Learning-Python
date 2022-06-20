"""https://www.youtube.com/watch?v=XKHEtdqhLK8
    *args = es un parámetro que junta todos los argumentos en un tuple ()
    es muy util para que una función pueda aceptar una variada cantidad de argumentos
"""
# una funcion def return normal sería así:
def add(a,b,c):
    sum = a + b + c
    return sum

print(add(2,3,1))
#pero si añado un tercer argumento, el programa dara error, ya que solo tengo dos statements en la funcion
"""def add(num1,num2):
    sum = num1 + num2
    return sum
print(add(5,4,89))"""
# ahora si quiero añadir 3,4, 5 o cualquier cantidad de argumentos en el futuro, uso el parametro *args como statement (importa más el asterisco)
def add_2(*args):
     sum = 0#si hago una suma, debo de colocar una v local = 0
#y como los arguments se convirtieron en clase tuple, puedo iterarlos o indexarlos, osea tratar como una lista for lopp
     for i in args:#para eso creo un for loop del statement *args
        sum += i   # dentro del for loop escribo que v += i (esto quiere decir que la variable equivale a la suma de los elementos dentro de la lista i)
     return sum#y por ultimo retorno la variable, en este caso sum
print(add_2(2,3,7,6,9))# ahora solo resta imprimir la funcion con los argumentos o tuples de la lista que queramos usar sin importar la cantidad
 #se sumaron los elementos de este tuple

""" incluso podemos llamar al argumento *args de otra manera, lo que importa es usar el asterisco"""


# ahora si quiero cambiar algun valor ya dentro de la función, tengo que convertir el argumento * a lista [[
#eso se logra de la siguiente manera
 # primero defino la funcion con su *arg
def add_3(*args):
     sum = 0# creo una variable que valga cero para despues arrojar una suma
     args = list(args)#importante aqui, modifico el argumento y lo convierto en una lista asi args = list(args)
     args[0] = 1#ahora si, indexo al numero de elemento que quiero cambiar.. arg[] = 5 .. aquí un ejemplo
     args[1] = 3
     args.insert(2, -4)
     for i in args:#ahora si creo un for loop lista
         sum += i# modifico la variable sum a que sume los elementos de la lista for loop
     return sum# retorno la variable, en este caso sum

print(add_3(1,1))

""" normalmente no podemos simplemente modificar los argumentos una vez dentro de la funcion, ya que son tuples, y los tuples no se pueden modificar
def add_4(*cosas):
    sum = 0
    cosas[0] = 0 # esto daría error, no puedo acceder al elemento 0, ya que un tuple NO es una lista
    for i in cosas:
        sum += i
    return sum
_"""

print("")
print("")
print("")
print("")










# una funcion def return normal sería así:
def add(a,b,c):
    sum = a + b - c
    return sum
print(add(1, 4, 3))

#pero si añado un tercer argumento, el programa dara error, ya que solo tengo dos statements en la funcion
"""def add(num1,num2):
    sum = num1 + num2
    return sum
print(add(5,4,89))"""
# ahora si quiero añadir 3,4, 5 o cualquier cantidad de argumentos en el futuro, uso el parametro *args como statement (importa más el asterisco)
def add2(*numeros):
    sum = 0#si hago una suma, debo de colocar una v local = 0
    for i in numeros:#y como los arguments se convirtieron en clase tuple, puedo iterarlos o indexarlos, osea tratar como una lista for lopp
         #para eso creo un for loop del statement *args
        sum += i # dentro del for loop escribo que v += i (esto quiere decir que la variable equivale a la suma de los elementos dentro de la lista i)
    return sum#y por ultimo retorno la variable, en este caso sum
print(add2(1,4,6,2))# ahora solo resta imprimir la funcion con los argumentos o tuples de la lista que queramos usar sin importar la cantidad
 #se sumaron los elementos de este tuple

""" incluso podemos llamar al argumento *args de otra manera, lo que importa es usar el asterisco"""


# ahora si quiero cambiar algun valor ya dentro de la función, tengo que convertir el argumento * a lista [[
#eso se logra de la siguiente manera
 # primero defino la funcion con su *arg
def add3(*lista):
     sum = 0# creo una variable que valga cero para despues arrojar una suma
     lista = list(lista)#importante aqui, modifico el argumento y lo convierto en una lista asi args = list(args)
     lista[0] = 2#ahora si, indexo al numero de elemento que quiero cambiar.. arg[] = 5 .. aquí un ejemplo
     lista[1] = 2
     for i in lista:#ahora si creo un for loop lista
         sum+= i# modifico la variable sum a que sume los elementos de la lista for loop
     return sum# retorno la variable, en este caso sum
print(add3(1,1,1))

# una funcion def return normal sería así:





#pero si añado un tercer argumento, el programa dara error, ya que solo tengo dos statements en la funcion
"""def add(num1,num2):
    sum = num1 + num2
    return sum
print(add(5,4,89))"""
# ahora si quiero añadir 3,4, 5 o cualquier cantidad de argumentos en el futuro, uso el parametro *args como statement (importa más el asterisco)

     #si hago una suma, debo de colocar una v local = 0
#y como los arguments se convirtieron en clase tuple, puedo iterarlos o indexarlos, osea tratar como una lista for lopp
     #para eso creo un for loop del statement *args
           # dentro del for loop escribo que v += i (esto quiere decir que la variable equivale a la suma de los elementos dentro de la lista i)
     #y por ultimo retorno la variable, en este caso sum
# ahora solo resta imprimir la funcion con los argumentos o tuples de la lista que queramos usar sin importar la cantidad
 #se sumaron los elementos de este tuple

""" incluso podemos llamar al argumento *args de otra manera, lo que importa es usar el asterisco"""


# ahora si quiero cambiar algun valor ya dentro de la función, tengo que convertir el argumento * a lista [[
#eso se logra de la siguiente manera
 # primero defino la funcion con su *arg

     # creo una variable que valga cero para despues arrojar una suma
     #importante aqui, modifico el argumento y lo convierto en una lista asi args = list(args)
     #ahora si, indexo al numero de elemento que quiero cambiar.. arg[] = 5 .. aquí un ejemplo


     #ahora si creo un for loop lista
         # modifico la variable sum a que sume los elementos de la lista for loop
     # retorno la variable, en este caso sum

