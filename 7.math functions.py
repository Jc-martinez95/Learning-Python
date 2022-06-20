#Curso Bro code https://www.youtube.com/watch?v=XKHEtdqhLK8
import math

año = 2020.5
a = 5.565656565756
b = 5.565656756565
c = 5.565657565656

print(round(año)) #la funcion round sirve para redondear un numero decimal (float) al numero entero (int) más cercano
print(math.ceil(año))#la subfuncion math.ceil sirve para redondear hacia arriba
print(math.floor(año)) #la subfuncion math.floor redondea hacia abajo
print(abs(año)) #la funcion abs nos da el numero absoluto del valor de la variable sin importar que el numero sea negativo
print(pow(año, 4)) #la funcion power (pow) eleva el valor de la variable a una potencia, (primero escribimos la base, y luego la potencia, separado con coma)
print(math.sqrt(año))#con la subfuncion math.sqrt puedo sacar la raiz cuadrada del valor numerico de una variable (no funciona con numeros negativos)


print(max(a, b, c))#con funcion max podemos encontrar el valor numerico mas alto de entre distintas variables
print(min(a,b,c))#con funcion min podemos encontrar el valor numerico más bajo de entre distintas variables
print(11/2)

x=2
y=2.5
print(x*y)