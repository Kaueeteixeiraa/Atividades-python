import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QDialog, QVBoxLayout, QLabel, QLineEdit, QPushButton

class InputJanela(QDialog):
    def init(self, parent=None):
        super().init(parent)
        self.setWindowTitle("Inserir Nome e Mensagem")
        self.setGeometry(100, 100, 300, 150)

        layout = QVBoxLayout()

        self.nome_edit = QLineEdit(self)
        self.nome_edit.setPlaceholderText("Seu Nome")
        layout.addWidget(self.nome_edit)

        self.mensagem_edit = QLineEdit(self)
        self.mensagem_edit.setPlaceholderText("Sua Mensagem")
        layout.addWidget(self.mensagem_edit)

        enviar_button = QPushButton("Enviar", self)
        enviar_button.clicked.connect(self.enviar)
        layout.addWidget(enviar_button)

        self.setLayout(layout)

    def enviar(self):
        nome = self.nome_edit.text()
        mensagem = self.mensagem_edit.text()
        self.parent().atualizar_mensagem(nome, mensagem)
        self.close()

class MainJanela(QMainWindow):
    def init(self):
        super().init()
        self.setWindowTitle("Janela Principal")
        self.setGeometry(100, 100, 400, 200)

        self.label_mensagem = QLabel("Mensagem aqui", self)
        self.label_mensagem.setGeometry(20, 20, 360, 100)

        abrir_button = QPushButton("Abrir Janela de Entrada", self)
        abrir_button.setGeometry(140, 130, 120, 30)
        abrir_button.clicked.connect(self.abrir_janela_entrada)

    def abrir_janela_entrada(self):
        input_janela = InputJanela(self)
        inputjanela.exec()

    def atualizar_mensagem(self, nome, mensagem):
        nova_mensagem = f"Nome: {nome}\nMensagem: {mensagem}"
        self.label_mensagem.setText(nova_mensagem)

if name == 'main':
    app = QApplication(sys.argv)
    main_janela = MainJanela()
    mainjanela.show()
    sys.exit(app.exec())