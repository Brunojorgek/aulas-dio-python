texto = input("Informe um texto: ")
VOGAIS = "AEIOU"

#Exemplo usando o iterável
for letra in texto:
    if letra.upper() in VOGAIS:
            print(letra, end = "")
print()

#Exemplo usando Built in
for i in range(0, 100, 2):
    print(i, end = " ")