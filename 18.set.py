# Curso Bro code https://www.youtube.com/watch?v=XKHEtdqhLK8
# set = los sets son una class, una lista que está desordenada y no indexada. y no hay valores duplicados

mandado = {"carne", "leche", "huevo"}

for y in mandado:
    print(y, end=" ")

mandado.add("tortillas")
print("")
for x in mandado:
    print(x, end=" ")
print("")

print("El cliente no quiere el huevo: ")
mandado.remove("huevo")
for z in mandado:
    print(z)

print("")
ingredientes ={"azucar", "sal", "pimienta"}
for a in ingredientes:
    print(a)
ingredientes.add("ajo")
print("")
for b in ingredientes:
    print(b)
print("")

ingredientes.remove("sal")
for c in ingredientes:
    print(c)


ingredientes.update(mandado)#con .update añado otro set a la variable. v1.update(v2) añado v2 a la v1
print(ingredientes)
print("")
ingredientes2 = {"tomate","cebolla","chile", "sal", "azucar"}
comida = mandado.union(ingredientes2) # con .union tambien puedo unir dos sets. pero tengo que crear otra variable..
# .... y dentro de ella tengo que usar la subfuncion. v3 = v1.union(v2)
for d in comida:
    print(d)
print("")
print("abajo muestro lo que los ingredientes tienen que ingredientes 2 no tienen")
print(ingredientes.difference(ingredientes2))
print("")
print("abajo muestro lo que los ingredientes e ingredientes 2 tienen en comun")
print(ingredientes2.intersection(ingredientes))
ingredientes.clear()
print(ingredientes)
