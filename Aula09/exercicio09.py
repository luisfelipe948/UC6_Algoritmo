
# codigo errado

def notas(valor1, valor2, valor3, valor4, valor5):
    valor1 = float(input("Digite a primeira nota: "))
    valor2 = float(input("Digite a segunda nota: "))
    valor3 = float(input("Digite a terceira nota: "))
    valor4 = float(input("Digite a quarta nota: "))
    valor5 = float(input("Digite a quinta nota: "))
    return valor1, valor2, valor3, valor4, valor5


def media(valor1, valor2, valor3, valor4, valor5):
    resultado = (valor1 + valor2 + valor3 + valor4 + valor5) / 5
    if resultado >= 7:
        print(f"Sua média foi de {resultado}, você está aprovado")
    elif resultado >= 5:
        print(f"Sua média foi de {resultado}, você está de recuperação")
    else:
        print(f"Sua média foi de {resultado}, você está reprovado")

# -----------------------------------------------------------------------------------------

# a função notas será usada para receber dados do usuário e retornar as notas,
#  enquanto a função media será responsável por calcular a média e exibir o resultado.
def notas():
    nota1 = float(input("Digite a primeira nota: "))
    nota2 = float(input("Digite a segunda nota: "))
    nota3 = float(input("Digite a terceira nota: "))
    nota4 = float(input("Digite a quarta nota: "))
    nota5 = float(input("Digite a quinta nota: "))

    return nota1, nota2, nota3, nota4, nota5


def media():
    nota1, nota2, nota3, nota4, nota5 = notas() # chama a função notas para obter as notas do usuário e armazena os valores retornados em variáveis

    resultado = (nota1 + nota2 + nota3 + nota4 + nota5) / 5
    if resultado >= 7:
        print(f"Sua média foi de {resultado}, você está aprovado")
    elif resultado >= 5:
        print(f"Sua média foi de {resultado}, você está de recuperação")
    else:
        print(f"Sua média foi de {resultado}, você está reprovado")

media() # chama a função media, que por sua vez chama a função notas para obter as notas do usuário e calcular a média.