class Plano:
    def __init__(self, saldo_inicial):
        self._saldo = saldo_inicial

    def verificar_saldo(self):
        return self._saldo

    def custo_chamada(self, duracao):
        return duracao * 0.10

    def deduzir_saldo(self, valor):
        self._saldo -= valor

class UsuarioTelefone:
    def __init__(self, nome, numero, plano):
        self._nome = nome
        self._numero = numero
        self._plano = plano

    def fazer_chamada(self, destinatario, duracao):
        custo = self._plano.custo_chamada(duracao)
        if self._plano.verificar_saldo() >= custo:
            self._plano.deduzir_saldo(custo)
            return f"Chamada para {destinatario} realizada com sucesso. Saldo: ${self._plano.verificar_saldo():.2f}"
        else:
            return "Saldo insuficiente para fazer a chamada."

class UsuarioPrePago(UsuarioTelefone):
    def __init__(self, nome, numero, saldo_inicial):
        super().__init__(nome, numero, Plano(saldo_inicial)) # Aqui estava o erro de sintaxe


# Recebendo as informações do usuário:
nome = input()
numero = input()
saldo_inicial = float(input())

# Objeto de UsuarioPrePago com os dados fornecidos:
usuario_pre_pago = UsuarioPrePago(nome, numero, saldo_inicial)
destinatario = input()
duracao = int(input())

# Chama o método fazer_chamada do objeto usuario_pre_pago e imprime o resultado:
print(usuario_pre_pago.fazer_chamada(destinatario, duracao))
