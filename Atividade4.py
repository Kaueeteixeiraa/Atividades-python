class Autor:
    def init(self, nome, data_nascimento):
        self.nome = nome
        self.data_nascimento = data_nascimento

class Livro:
    def init(self, titulo, autor):
        self.titulo = titulo
        self.autor = autor

autor1 = Autor("Joao da Silva", "15/05/1980")
livro1 = Livro("Aventuras no Mundo Perdido", autor1)

print(f"Autor: {livro1.autor.nome}")
print(f"Data de Nascimento do Autor: {livro1.autor.data_nascimento}")
print(f"Titulo do Livro: {livro1.titulo}")