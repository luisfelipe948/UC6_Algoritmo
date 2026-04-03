print("Exercício 1:\n")

dados = {
 "nome": "",
 "idade": "",
 "cidade": "",
}

nome = input("Digite seu nome: ")
idade = input("Digite sua idade: ")
cidade = input("Digite sua cidade: ")

print("\n")

dados["nome"] = nome
dados["idade"] = idade
dados["cidade"] = cidade

for chave, valor in dados.items(): 
    print(chave, ":", valor)

print("\n")

print("Exercício 2:\n")

notas = {
    "nota1": "",
    "nota2": "",
    "nota3": "",
    "nota4": "",
    "nota5": "",
}

nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite a segunda nota: "))
nota3 = float(input("Digite a terceira nota: "))
nota4 = float(input("Digite a quarta nota: "))
nota5 = float(input("Digite a quinta nota: "))

print("\n")

notas["nota1"] = nota1
notas["nota2"] = nota2
notas["nota3"] = nota3
notas["nota4"] = nota4
notas["nota5"] = nota5

media = (notas["nota1"] + notas["nota2"] + notas["nota3"] + notas["nota4"] + notas["nota5"]) / 5

print("A média das notas é:", f"{media:.2f}")