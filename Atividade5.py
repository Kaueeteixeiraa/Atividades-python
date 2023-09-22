class Motor:
    def init(self, tipo, potencia):
        self.tipo = tipo
        self.potencia = potencia

class Carro:
    def init(self, motor):
        self.motor = motor

motor_gasolina = Motor("Gasolina", 150)
meu_carro = Carro(motor_gasolina)

print(f"Tipo de motor do carro: {meu_carro.motor.tipo}")
print(f"Potencia do motor do carro: {meu_carro.motor.potencia} cavalos")