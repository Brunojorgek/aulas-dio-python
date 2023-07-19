MAIOR_IDADE = 18
IDADE_ESPECIAL = 17

idade = int(input("Informe sua idade: "))



if idade >= MAIOR_IDADE:
    print("Pode tirar a habilitação")
elif idade < MAIOR_IDADE:
    print("Não pode tirar a habilitação")



if idade >= MAIOR_IDADE:
    print("Pode tirar a habilitação")
else:
    print("Não pode tirar a habilitação")



if idade >= MAIOR_IDADE:
    print("Pode tirar a habilitação")
elif idade == IDADE_ESPECIAL:
    print("Pode começar fazendo aulas teóricas")
else:
    print("Não pode tirar a habilitação")