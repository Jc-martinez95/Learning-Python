#Curso Bro code https://www.youtube.com/watch?v=XKHEtdqhLK8
# if statement = bloque de codigo que se ejecuta si la condición se cumple

age = int(input("¿Cuantos años tienes?: ")) #como quiero que el usuario escriba un numero, tengo que convertir la variable a clase int
if age == 100: #aqui pongo la condicion de si la edad es igual a 100 (OJO usar doble signo de igual, sino python creera que quiero asignar un valor a la variable)
    print("Eres un anciano!!")
elif age >= 18: #aqui estoy poniendo una condicion, si la variable age es igual o mayor a 18 (para cerrar la condicion hay que colocar dos puntos)
    print("Ya eres un adulto!") #aqui escribo lo que quiero que se muestre si la condicion se cumple.
elif age <= 0: #con elif podemos añadir otra condición (va despues del primer if)
    print("Wtf aún no has nacido!!!")
else: #esto es para mostrar algo si la condicion no se cumple (OJO usar dos puntos luego de else)
    print("Aún eres un menor de edad")