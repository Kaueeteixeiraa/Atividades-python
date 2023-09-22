class Veiculo:
    def init(self, cor, preco):
        self.cor = cor
        self.preco = preco

    def detalhes(self):
        return f"Cor: {self.cor}, Preco: R${self.preco:.2f}"


class Carro(Veiculo):
    def init(self, cor, preco, numero_portas):
        super().init(cor, preco)
        self.numero_portas = numero_portas

    def detalhes(self):
        return f"{super().detalhes()}, Numero de Portas: {self.numero_portas}"


class Bicicleta(Veiculo):
    def init(self, cor, preco, tipo):
        super().init(cor, preco)
        self.tipo = tipo

    def detalhes(self):
        return f"{super().detalhes()}, Tipo: {self.tipo}"

carro = Carro("Vermelho", 25000, 4)
bicicleta = Bicicleta("Azul", 800, "Montanha")

print(carro.detalhes()) 
print(bicicleta.detalhes()) 