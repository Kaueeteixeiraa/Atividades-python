class Documento:
    def init(self, titulo, conteudo):
        self.titulo = titulo
        self.conteudo = conteudo

    def exibir(self):
        return f"Titulo: {self.titulo}, Conteudo: {self.conteudo}"

class Email(Documento):
    def init(self, titulo, conteudo, remetente, destinatario):
        super().init(titulo, conteudo)
        self.remetente = remetente
        self.destinatario = destinatario

    def exibir(self):
        return f"{super().exibir()}, Remetente: {self.remetente}, Destinatario: {self.destinatario}"

class Relatorio(Documento):
    def init(self, titulo, conteudo, data):
        super().init(titulo, conteudo)
        self.data = data

    def exibir(self):
        return f"{super().exibir()}, Data: {self.data}"

email = Email("Reuniao de Projeto", "Conteudo da reuniao...", "kaue@example.com", "kayan@example.com")
relatorio = Relatorio("Relatorio Mensal", "Dados de vendas...", "20/09/2023")

print(email.exibir())
print(relatorio.exibir()) 