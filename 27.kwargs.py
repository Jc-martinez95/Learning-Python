"""Curso bro code: https://www.youtube.com/watch?v=XKHEtdqhLK8

**kwargs = es un parametro o statement que juntara todos los argumentos para una funcion, en un diccionario
            muy util para que una funcion acepte una variada cantidad de key:value key=value o argumentos keyword

"""
# Aquí tengo un ejemplo de una funcion normal con keyword arguments, argumentos que su orden está definido manualmente en la invocacion
def hello(name,age,height):
    print("hola", name, "tienes", age, "años, y mides", height)

hello("juan", 32, 200.5)

# Hasta aqui todo bien, pero que tal si quiero añadir otro keyword argument sin añadir su respectivo statement en la funcion?

""" def hello(first_name, last_name)
    print("Hola", first_name, middle_name, last_name)
hello(last_name="Martinez",first_name="Juan", middle_name="Carlos")"""
#acá arriba habrá un error.

# Para eso uso el parametro **kwargs (importa más los dos asteriscos)
def edades(**kwargs): #defino una funcion y el argumento seran dos asteriscos **, esto lo convierte en un diccionario
   print(kwargs['maria']) # imprimo algo y si quiero imprimir algo del diccionario, tengo que añadirlo y en bracktes escribir el key dentro de '
   print(kwargs['jose'])  # No importa que no usemos todos los keywords arguments
edades(juan=27, maria=19, jose=45, luisa=33)


# Ahora quiero imprimir cada valor del diccionario
def diccio(**keyw): #Primero defino el diccionario con **
    print("las capitales de paises europeos son", end=" ")#imprimo un mensaje y añado end=" " para que lo siguiente aparezca en la misma linea de codigo
    for key, value in keyw.items():#creo una lista for loop del diccionario para key y value. asi: for key, value in dic.items()
        print(value, end=", ") # luego imprimo lo que quiera mostrar, en este caso solo los valores
diccio(Inglaterra='Londres', Irlanda='Dublin', España='Madrid', Grecia='Atenas') #Y por último invoco la funcion con los keyword arguments que quiera utilizar


print("")
print("")
# voy a crear una funcion def con *args de diferente clase, str,int, float.
def mix (*args,):
    print(args)#se comporta como un tuple, lista de datos no modificable de diferentes clases
mix(1, 2, 3.5, "hola")


# Y ahora voy a crear otra funcion mezclando *args con **kwargs
def mix2(*args, **kwargs): #debo de colocar ambos statements en la funcion, aqui el orden ahora si importa
     print(args, kwargs)
     print(kwargs)
     print(args[1], kwargs['peso'])# la hora de imprimir no importa el orden. y recuerda no usar coma, ya que no podemos concatenar args con kwargs
mix2(1,2,"hola", peso=85)# Pero el orden importa porque en el invocador tengo primero args tipo tuple y despues argumentos tipo dic
"""     mix(1, 2.3, "hola", italia="roma")
    funcion(*args---------, **kwargs-----)
aqui está el orden de los argumentos, que debe coincidir con la posicion u orden de los statements
"""
print("")
# Práctica:
def lista(*args, **kwargs): #al parecer en la definicion de la funcion, va primero los *args y después los **kwargs
    args = list(args)#modifico los argumentos *args a lista para modificarlos
    print(args[2])#una vez modificado, imprimo ciertos elementos
    print(kwargs['lupita'])# imprimo elementos pero del diccionario **kwargs
    print(kwargs.get('mario'))#otra forma
    print(args[0], args[1], end=" ")
    for key, value in kwargs.items():#ahora cree una lista for loop in del diccionario
        print(key, value, end=" ")# e imprimi los datos
lista("Hola", "estas son las medidas", 4, 1, lupita=180.5, mario=176.4) #los argumentos a usar

print("")
#ahorsa una practica con url
def my_random_django_view(request, **kwargs):
    print(request, kwargs)
    print(kwargs['id'])
"""path('my-product/:id')"""
my_random_django_view("request", id='some_id')

print("")
print("")

def foo(required, *args, **kwargs):
    print(required)
    if args:
        print(args)
    if kwargs:
        print(kwargs)

foo("hello", 1, 2, 3, "adios", bier="cerveza", sanft="jugo")


#Aquí voy a crear una lista ya existente a argumentos para usar en una funcion def
def arg_one(*args): #defino la funcion con *args
    for stuff in args: #creo un for loop
        print(stuff) #la imprimo

my_list = ["Honda", "BMW", "Toyota", "Ford", "Chevy"] #aqui está la lista original
print(my_list)
arg_one(*my_list) #IMPORTANTE, aqui invoco a la funcion, pero como argumento indico que la lista la transforme en argumentos, así arg_one(*my_list)

print("")
def arg_3(one, two, *args):
    print(one)
    print(two)
    for i in args:
        print(i)
arg_3("argumento 1", "argumento 2", "lista", "de", 4, "argumentos")

#Ahora voy a crear argumentos de un diccionario ya existente:
def kwarg_1(**kwargs): #defino la funcion con **
    for key, value in kwargs.items(): #creo un indice for lopp de keys y values in dic.items()
        print(key, value) #imprimo
diccionario = {'Handy':'Celular', 'Tisch':'Mesa', 'Löffel':'Cuchara'}# Aquí está el diccionario
kwarg_1(**diccionario) #y aqui lo convierto a key word arguments **kwargs dentro de la invocacion de la funcion