menu = """

[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair

=> """

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 0
deposito = 0

while True:

    opcao = input(menu)

    if opcao == "d":
        deposito = float(input("Digite o valor a ser depositado: "))
        if deposito <= 0:
            print("Valor de depósito inválido: ")
        else:
            saldo = saldo + deposito
            extrato += f"Depósito: {deposito}, Novo saldo: {saldo}\n"
            print(f"Valor depositado: {deposito}, novo saldo: {saldo}")

    elif opcao == "s":
        saque = float(input("Digite o valor a ser sacado: "))
        if saque <= 0:
            print("Valor de saque inválido: ")
        elif saque > saldo:
            print("Saldo insuficiente: ")
        else:
            saldo = saldo - saque
            numero_saques += 1
            extrato += f"Saque: {saque}, Novo saldo: {saldo}\n"
            print(f"Valor sacado: {saque}, novo saldo: {saldo}")
        if numero_saques == 3:
            print("Número limite de saques atingido.")

    elif opcao == "e":
        print(f"Extrato:\n{extrato}")

    elif opcao == "q":
        print("Encerrando o programa.")
        break

    else:
        print("Opção inválida.")
    
