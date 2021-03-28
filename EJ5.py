frase = input("Ingrese una frase")
string = input("Ingrese la palabra a buscar")
frase = frase.lower().split(" ")
string = string.lower()
cant = 0
for elem in frase:
    if elem in string:
        cant += 1

print(f"El string {string} se encuentra {cant} veces en la frase {frase}")    