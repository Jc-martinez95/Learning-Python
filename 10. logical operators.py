#Curso Bro code https://www.youtube.com/watch?v=XKHEtdqhLK8
# Logical (and, or, not)  = sirve para checar si dos o mas condicionales son verdad

temp = int(input("¿Cual es la temperatura afuera? "))

if temp >=0 and temp <=30: #con el operador logico "and" ambas condiciones se deben cumplir para que sea verdad
    print("la temperatura está agradable el día de hoy!")
    print("sal afuera")
elif temp < 0 or temp > 30: #con el operador logico "or" con que cualquiera de las dos condiciones se cumplan, sera verdadera
    print("la temperatura no es agradable")
    print("quédate en casa el día de hoy")

# Aqui abajo voy a repetir el proceso, pero incluyendo el operador logico not despues del if, esto invierte la condicion.
# con "not" si la condicion normalmente es verdadera se convierte en falsa y viceversa.
temp_2 = int(input("Cual es la temperatura afuera?" ))

if not (temp_2 >=0 and temp_2 <=30): #con el operador logico "and" ambas condiciones se deben cumplir para que sea verdad
    print("la temperatura está agradable el día de hoy!")
    print("sal afuera")
elif not (temp_2 < 0 or temp_2 > 30): #con el operador logico "or" con que cualquiera de las dos condiciones se cumplan, sera verdadera
    print("la temperatura no es agradable")
    print("quédate en casa el día de hoy")

a = 55
b = 40
c = 15

if a < b and a < c:
    print("a es menor a b y c")
elif a > b and a < c:
    print("a es mayor a b pero menor a c")
elif a < b and a > c:
    print("a es menor a b pero mayor a c")
else:
    print("a es mayor a b y c")