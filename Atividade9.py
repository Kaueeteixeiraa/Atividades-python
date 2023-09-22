class ContaBancaria:
    def init(self, titular, saldo=0):
        self.titular = titular
        self.saldo = saldo

    def depositar(self, valor):
        self.saldo += valor

    def sacar(self, valor):
        if valor <= self.saldo:
            self.saldo -= valor
            return True
        else:
            return False

class ContaPoupanca(ContaBancaria):
    def sacar(self, valor):
        taxa = 2
        if super().sacar(valor + taxa):
            return True
        else:
            return False

class ContaCorrente(ContaBancaria):
    def init(self, titular, saldo=0, limite=0):
        super().init(titular, saldo)
        self.limite = limite

    def sacar(self, valor):
        if valor <= self.saldo + self.limite:
            if valor <= self.saldo:
                self.saldo -= valor
            else:
                self.limite -= (valor - self.saldo)
                self.saldo = 0
            return True
        else:
            return False

conta1 = ContaPoupanca("Kaue", 100)
conta2 = ContaCorrente("Kayan", 500, 1000)

conta1.depositar(200)
print(f"Saldo da conta poupanca: {conta1.saldo}")
conta1.sacar(50)
print(f"Saldo da conta poupanca apos saque: {conta1.saldo}")

conta2.depositar(300)
print(f"Saldo da conta corrente: {conta2.saldo}")
conta2.sacar(800)
print(f"Saldo da conta corrente apos saque: {conta2.saldo}")
print(f"Limite da conta corrente apos saque: {conta2.limite}") 
