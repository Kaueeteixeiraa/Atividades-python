class Livro:
    def init(self, titulo, autor):
        self.titulo = titulo
        self.autor = autor

class Biblioteca:
    def init(self):
        self.livros = []

    def adicionar_livro(self, livro):
        self.livros.append(livro)

    def listar_livros(self):
        for livro in self.livros:
            print(f"{livro.titulo} por {livro.autor}")

livro1 = Livro("A Arte da Guerra", "Sun Tzu")
livro2 = Livro("Dom Quixote", "Miguel de Cervantes")
livro3 = Livro("O Pequeno Principe", "Antoine de Saint-Exupery")

biblioteca = Biblioteca()
biblioteca.adicionar_livro(livro1)
biblioteca.adicionar_livro(livro2)
biblioteca.adicionar_livro(livro3)

biblioteca.listar_livros() 