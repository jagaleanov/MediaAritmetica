# Escribir un programa que solicite cinco números, los 
# almacene en una lista y luego calcule la media aritmética 
# de esos números

lista = []
suma = 0

for x in range(5):
    lista = lista + [int(input("ingrese un numero: "))]

for y in range(5):
    suma = suma + lista[y]

print("La media aritmetica es ",(suma / 5)," ")