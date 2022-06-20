#Curso Bro code https://www.youtube.com/watch?v=XKHEtdqhLK8
# while loop = es una declaracion que se ejecutará siempre y cuando la condicion sea verdadera.

name = "" #aqui establezco la variable name (que aun no es nada)

while len(name) == 0: #mientras la variable name tenga una longitud de 0 caracteres. entonces...
     name=input("Cual es tu nombre?")#Vuelve a mostrar el input
#si no escribes nada se aparecera el mismo input, loopeandose hasta que escribas algo
print("Mucho gusto "+name) #una vez salgas del loop, mostrará este mensaje

# a continuacion voy a hacer lo mismo que arriba, pero con otra fórmula.
name2 = None #recuerda que None tiene que comenzar con mayúscula para distinguirlo de un valor de variable
while not name2: #recuerda usar 2 puntos y dos signos de igual.
    name2 = input("Cómo te llamas otra vez?")
print("Aaah ok", name2, "ya me acordé")


while 1==2: #aqui pongo, mientras 1 sea igual a 1, imprime lo debajo
    name = print("Ayuda, estoy en un loop!!")