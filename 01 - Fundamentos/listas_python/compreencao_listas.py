#Filtro versão 1
numeros = [1, 30, 21, 2, 9, 65, 34]
pares = []

for numero in numeros:
	if numero % 2 == 0:
		pares.append(numero)

print(numeros)
print(pares)

#Filto verssão 2
numeros = [1, 30, 21, 2, 9, 65, 34]
pares = [numero for numero in numeros if numero %2 == 0]
print(numeros)
print(pares)

#Modificando valores versão 1
numeros = [1, 30, 21, 2, 9, 65, 34]
quadrado = []
for numero in numeros:
	quadrado.append(numero ** 2)
print(numeros)
print(quadrado)

#Modificando valores versão 2
numeros = [1, 30, 21, 2, 9, 65, 34]
quadrado = [numero**2 for numero in numeros]
print(numeros)
print(quadrado)