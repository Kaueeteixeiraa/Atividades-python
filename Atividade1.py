
def saudacao():
    print("Ola! Bem-vindo ao meu programa.")

def calcular_area_retangulo(largura, altura):
    print(f"A area do retangulo e {largura * altura} unidades quadradas.")

def eh_par(numero):
    return numero % 2 == 0

saudacao()
calcular_area_retangulo(5, 8)

numero = 7
if eh_par(numero):
    print(f"{numero} e um numero par.")
else:
    print(f"{numero} e um numero impar.")