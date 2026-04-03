import random
import math
import datetime

# sempre coloque os imports no início do código

# gera um número aleatório entre 1000 e 2000
numero_aleatorio = random.randint(1000, 2000)
print(numero_aleatorio)

# sorteio de alunos
alunos = ["Israel", "Adenilson", "João", "Jonathan", "Carlos"]

# choice é um método da biblioteca random que sorteia um elemento de uma lista
aluno_sorteado = random.choice(alunos)
aluno_sorteado2 = random.choice(alunos)
print("Os alunos sorteados foram:", aluno_sorteado, "e", aluno_sorteado2)

# biblioteca math

numero = 16

# sqrt é um método da biblioteca math que calcula a raiz quadrada de um número
raiz  = math.sqrt(numero)
print(raiz)

# trabalhando com datas

# datetime é uma biblioteca que trabalha com datas e horas
agora = datetime.datetime.now()
print(agora)

# exercicio: solicitar ao usuario um numero de 1 ate 5, e gerar um número aleatório usando a biblioteca random. 
# e verificar se o usuario digitou o mesmo valor que o sorteado

numero_usuario = int(input("Digite um número de 1 a 5: "))
numero_sorteado = random.randint(1, 5)

if numero_usuario == numero_sorteado:
    print("Parabéns! Você acertou o número sorteado:", numero_sorteado)
else:
    print("Você errou, o número sorteado foi:", numero_sorteado)