lista = ["P", "y", "h", "o", "n"]

lista[2:]    # ["t", "h", "o", "n"]
print(lista)

lista[:2]    # ["P", "y"]
print(lista)

lista[1:3]   # ["y", "t"]
print(lista)

lista[0:3:2] # ["P", "t"]
print(lista)

lista[::]    # ["P", "y", "t", "h", "o", "n"]
print(lista)

lista[::-1]	 # ["n", "o", "h", "t", "y", "P"]
print(lista)


carros = ["gol", "celta", "palio"]

for carro in carros:
	print(carro)