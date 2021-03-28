frase = input("Ingrese una frase o palabra")
frase = frase.lower()
frase = [char for char in frase]
set_frase = set(frase)

if (len(set_frase) == len(frase)):
    print("La palabra es un heterograma")
else:
    print("La palabra no es un heterograma")    