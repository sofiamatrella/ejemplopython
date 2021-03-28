cadena = input("Ingresa un texto")
caracter = input("Ingrese una letra")
if len(caracter) > 1:
    print("Ingresaste más de una letra")
    exit(1)
c = cadena.split(" ")
for elem in c:
    if (elem.startswith(caracter)):
        print (elem)