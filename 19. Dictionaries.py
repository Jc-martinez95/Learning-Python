# Curso Bro code https://www.youtube.com/watch?v=XKHEtdqhLK8
# dictionary = una coleccion cambiable, y desordenada de datos en pares (palabra:definicion)
#               esta funcion es rápida porque usamos hashing ('') nos permite acceder rápidamente a un valor.

# primero creamos una variable que será la base de datos de nuestro diccionario
dic = {'Haus':'Casa','Frau':'Mujer', 'Mann':'Hombre',
        'Wasser':'Agua', 'Bier':'Cerverza'} # tenemos que crear un set con {, y los datos colocarlos así-> 'palabra':'definicion'
             #recuerda separar cada par con comas

print(type(dic))#aqui se que la variable es clase dict osea diccionario
print(dic['Haus'])#para buscar una capital por ejemplo, tengo que print(v['palabra']) para que me de la definicion. osea buscar una lista
 # OJO recuerda usar hashings. si no se encuentra el dato en el diccionario, el programa dará error
# pero hay otra forma mejor de encontrar un dato con la subfuncion .get despues de la variable
print(dic.get('Bier')) #print(v.get('palabra')) y dará la definición, No hay, por eso mostrara None en la consola

print(dic.keys())#con la subfuncion v.keys muestro solo los keys y no los values, osea solo la palabra o país, y no la definicion
 # Recuerda no colocar nada dentro de los segundos parentesís
print("")
print(dic.values())#con subfuncion .values solo imprimo los valores o values y no la palabra o capitales.

print("")
#con subfunción .items muestro todo el diccionario, keys y values.
print(dic.items()) #OJO recuerda usar parentesis luego de la subfuncion .items()

#hay otra forma si quiero mostrar todos los pares mas ordenados, y es con una for loop lista.
for keys, values in dic.items(): #tiene que ser for key, value in v.items()
    print(keys,values)#y luego solo pido que imprima tanto la lista de key como de value, separado con coma

# También puedes añadir nuevos valores al diccionario, con la subfuncion .update
# tenemos que crear un set con {, y los datos colocarlos así-> 'palabra':'definicion'
dic.update({'Geld':'Dinero', 'Blau':'Azul', 'Schule':'Escuela'})             #recuerda separar cada par con comas
 # tiene que ser v.update({'key':'value'})
print(dic)#aqui se ve el resultado
# E incluso podemos modificar los valores dentro del diccionario
dic.update({'Haus':'Hogar'}) # tiene que ser v.update({'key:value'})
print(dic)
# para remover un par de valores usamos la subfuncion .pop
dic.pop('Geld') # tiene que ser v.pop('key')

print(dic)
del dic['Frau'] #con el statement del podemos eliminar tambien un par de elementos. del dict['key']
print(dic)
print("diccionario 2")

#puedo crear un nuevo diccionario que contenga una copia de otro diccionario
dict2 = dict(dic) #este es un metodo dict2 = dict(dict1)
print(dict2.items())
print("")
print("diccionario 3")
dict3 = dict(dict2.items())# esta es otra forma de copiar un diccionario dentro de otro dict2 = dict(dict1.items())
print(dict3)

print("")

print("diccionario 4") # y otra forma de añadir un diccionario dentro de otro es con la subfuncion .update(dict1)
dict4 = {}
dict4.update(dict3)
print(dict4)

print("")

print("borrar diccionario")
#con subfuncion .clear eliminamos el diccionario por completo.
dic.clear()# OJO recuerda no poner nada dentro del paréntesis
print(dic)

print("")


x = [
    'a',
    'b',
    {
        'foo': 1,
        'bar':
        {
            'x' : 10,
            'y' : 20,
            'z' : 30
        },
        'baz': 3
    },
    'c',
    'd'
]
print(x[2]['bar'].get('z'))


