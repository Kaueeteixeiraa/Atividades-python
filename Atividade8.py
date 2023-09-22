class Produto:
    def init(self, nome, preco):
        self.nome = nome
        self.preco = preco

    def desconto(self, percentual):
        desconto_valor = (percentual / 100) * self.preco
        preco_com_desconto = self.preco - desconto_valor
        return preco_com_desconto

class Livro(Produto):
    def init(self, nome, preco, autor):
        super().init(nome, preco)
        self.autor = autor

    def desconto(self, percentual):
        desconto_geral = super().desconto(percentual)
        desconto_adicional = 0.1 * super().desconto(0)
        return desconto_geral - desconto_adicional

class Jogo(Produto):
    def init(self, nome, preco, plataforma):
        super().init(nome, preco)
        self.plataforma = plataforma

produto1 = Produto("Produto Generico", 100)
print(f"Preco com desconto geral: R${produto1.desconto(20)}")

livro1 = Livro("Livro de Exemplo", 50, "Autor Exemplo")
print(f"Preco do livro com desconto: R${livro1.desconto(20)}")

jogo1 = Jogo("Jogo de Exemplo", 60, "PS5")
print(f"Preco do jogo com desconto: R${jogo1.desconto(15)}") 