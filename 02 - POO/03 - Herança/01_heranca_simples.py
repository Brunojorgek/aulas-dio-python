class Veiculo:
    def __init__(self, cor, placa, numero_rodas):
        self.cor = cor
        self.placa = placa
        self.numero_rodas = numero_rodas

    def ligar_motor(self):
        print("Ligando o motor... ")

    def __str__(self):
        return f"{self.__class__.__name__}: {' , '.join([f'{chave} = {valor}' for chave, valor in self.__dict__.items()])}"

class Motocicleta(Veiculo):
    pass

class Carro(Veiculo):
    pass

class Caminhao(Veiculo):
    def __init__(self, cor, placa, numero_rodas, carregado):
            super().__init__(cor, placa, numero_rodas)
            self.carregado = carregado
    def esta_carregado(self):
        print(f"{'sim' if self.carregado else 'não'} estou carregado")

moto = Motocicleta("preta", "ABC123", 2)
print(moto)

carro = Carro("branco", "xyz-3254", 4)
print(carro)

caminhao = Caminhao("vermelho", "wsa-8567", 8, False)
print(caminhao)