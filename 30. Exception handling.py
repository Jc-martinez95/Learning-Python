""" Curso Bro Code https://www.youtube.com/watch?v=XKHEtdqhLK8 """

# Exception = eventos ocurridos durante la ejecucion del código que interrumpen el flow del programa y hacen que se detenga

# Primero voy a crear una division de un numero entre cero para que me de error.
# Lo haré además haciendo que el usuario use input para dar los numeros
# Y para evitar que crashee el programa tenemos que indentar el codigo dentro de las clause try:
# y fuera del mismo colocar la clause except Exception ..esto evitara cualquier error asi:
"""
try:
    codigo dañino o problemático que sabemos quizá va a crashear el programa

except Exception:
    print("Lo que sea como mensaje por si hay un error")
"""
try:
    numerador = int(input("Que numero quieres dividir?" ))
    denominador = int(input("entre cuanto lo quieres dividir? "))
    result = numerador / denominador
except ZeroDivisionError as f:
    print(f)
    print("Error, no es posible dividir entre cero")
except ValueError as g:
    print(g)
    print("Error. debes de insertar solo números")
except Exception as e:
    print(e)
    print("Upps hubo un error")
else:
    print(result)
finally:
    print("La división se realizó con éxito")

# Esta no es una buena práctica, ya que solo damos un mensaje para cualquier tipo de error
# Lo ideal es mostrar distintos mensajes para cualquier tipo de error, así sabremos y el usuario sabra porque fue el error

# Un ejemplo al dividir entre cero es: except ZeroDivisionError

try:
    numerador = int(input("Escribe un numero a dividir "))
    denominador = int(input("Entre que numero lo quieres dividir? "))
    resultado = numerador / denominador
except ValueError as e:
    print(e)
    print("Solo puedes insertar números")
except ZeroDivisionError as e:
    print(e)
    print("No es posible dividir entre cero")
except Exception as e:
    print(e)
    print("Hubo un error desconocido")
else:
    print(float(resultado))
finally:
    print("La operación se realizó con éxito")



