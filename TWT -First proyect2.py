# Tutorial primer proyecto en Python https://www.youtube.com/watch?v=7R-CfL21zIY
import time
vida = 10
print("Hola mundo")
def load(a):
    loading = [".", ".", "."]
    for i in loading:
        print(i)
        time.sleep(a)
print("bienvenidos a mi primer juego interactivo")
load(1)
name = input("Cuál es tu nombre?").title()

while len(name) == 0:
    name = input("Tienes que escribir tu nombre. ¿Cuál es tu nombre? ")

print("Hola", name, "Este es una juego donde debes tomar desiciones")

age = int(input("¿Cuantos años tienes?"))
if age >= 18:
    print("Puedes continuar")
    print("Muy bien", name, "comencemos")
    load(1)
    print("Despiertas en una habitación de un hotel")
    print("No recuerdas como llegaste hasta ahí, pero te pones a investigar) ")
    load(0.5)

    choice1 = input("Tienes dos opciones, tratas de salir de la habitacion o investigas la habitacion, qué haces? (salir/investigar" ).lower()
    if choice1 == "salir":
        print("La puerta no abre, por lo que solo queda investigar la habitacion")
        print("te das cuenta que hay un olor fétido en el baño, y al mismo tiempo llama la atención una maleta en la cama de la habitacion")
        choice1_1 = input("¿Qué haces, ir al baño o ver que hay en la maleta? (baño/maleta)" )
        load(0.5)

        if choice1_1 == "baño" or "ir":
            print("te encontraste con un cadaver, pero vez que tiene unas llaves en su mano")
            print("Con esas llaves puedes salir, felicidades!!")
        elif choice1_1 == "maleta" or "ver":
            print("vez que en la maleta hay una bomba y explota, moriste")

    elif choice1 == "investigar":
        print("Vas a la cama y notas una maleta y la ventana abierta")
        load(1)
        choice1_2 = input("Que deseas hacer, abrir la maleta o asomarte por la ventana? (maleta/ventana) ")
        if choice1_2 == "maleta" or "abrir":
            print("vez que en la maleta hay una bomba y explota, moriste :(")
        elif choice1_2 == "ventana" or "asomarme":
            print("Pudiste salir de la habitacion, felicidades!!")
























else:
    print("Tienes que ser mayor de edad para jugar")