def mensagem(nome):
    print("Executando mensagem")
    return f"oi {nome}"
def mensagem_longa(nome):
    print("Executando mensagem longa")
    return f"Olá tudo bem {nome}?"
def executar(funcao):
    print("executando executar")
    return funcao("Bruno")

print(executar(mensagem_longa))