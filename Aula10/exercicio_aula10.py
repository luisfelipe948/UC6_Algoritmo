nome = input("Digite seu nome: ")
idade = int(input("Digite sua idade: "))

with open("Aula10/exercicio10.txt", "w") as arquivo:
    arquivo.write(f"Nome: {nome}\n")
    arquivo.write(f"Idade: {idade}\n")

print("\n")

with open("Aula10/exercicio10.txt", "r") as leitura_arquivo:
    recebe_leitura = leitura_arquivo.read()
    print(recebe_leitura)