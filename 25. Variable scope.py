# Curso Bro code https://www.youtube.com/watch?v=XKHEtdqhLK8

# scope = es la region donde una variable es reconocida.
#         Una variable está solo disponible dentro de la region donde es creada.
#         Pero pueden ser creadas una version local y global de la variable.

def display_name():
    name = "Martinez" #☜esta variable esta en un scope local, ya que solo está disponible dentro de esta funcion def
    print(name) #☜es un localy variable scope
#si yo quiero mostrar esta funcion lo hago acá abajo
print("acá abajo se muestra el resultado de una función que dentro de la misma tiene una variable name y es locaL")
display_name()
print("")
print("a continuacion se muestra el valor de una variable clase str que es global ☟" )
# ☟si yo quiero imprimir la variable locally available scope dentro de la funcion, pero fuera de ella, me dará error print(name)☟


name = "Juan" # esta es una version globally scoped, ya que afecta todo el codigo, excepto en funciones.
print(name)

#Recuerda que el orden del scope de las variables es LEGB.
# L = Local
# E = Enclosing
# G = Global
# B = Built-in