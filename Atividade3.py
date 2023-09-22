class SistemaOperacional:
    def init(self, nome, versao):
        self.nome = nome
        self.versao = versao

class Computador:
    def init(self, sistema):
        self.sistema = sistema

sistema = SistemaOperacional("Windows", "10")
meu_computador = Computador(sistema)

print(f"Meu computador esta rodando o sistema {meu_computador.sistema.nome} {meu_computador.sistema.versao}")