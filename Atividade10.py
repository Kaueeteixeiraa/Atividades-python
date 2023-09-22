class Publicacao:
    def init(self, titulo, ano_publicacao):
        self.titulo = titulo
        self.ano_publicacao = ano_publicacao

    def descricao(self):
        return f"Titulo: {self.titulo}, Ano de Publicacao: {self.ano_publicacao}"


class Livro(Publicacao):
    def init(self, titulo, ano_publicacao, autor, numero_paginas):
        super().init(titulo, ano_publicacao)
        self.autor = autor
        self.numero_paginas = numero_paginas

    def descricao(self):
        return f"{super().descricao()}, Autor: {self.autor}, Numero de Paginas: {self.numero_paginas}"


class Revista(Publicacao):
    def init(self, titulo, ano_publicacao, editora, edicao):
        super().init(titulo, ano_publicacao)
        self.editora = editora
        self.edicao = edicao

    def descricao(self):
        return f"{super().descricao()}, Editora: {self.editora}, Edicao: {self.edicao}"

livro1 = Livro("Aprendendo Python", 2020, "John Smith", 400)
revista1 = Revista("Python Monthly", 2022, "Editora ABC", "Edicao de Janeiro")

print(livro1.descricao())
print(revista1.descricao()) 