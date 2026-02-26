# dicionario em python

aluno = {
    "nome_aluno": "Pedro",
    "idade": 19,
    "nota": 8,
    "curso": "Técnico em informática para internet.",
    # array
    "Array": [30, True, "Texto"],
    #posicoes  0    1       2

# dicionario dentro de outro:

    "endereco": {
        "cidade": "SP",
        "estado": "SP",
        "numero": 224
    }
}

print(aluno["nome_aluno"])

# acessar o segundo dicionario, mas com um campo especifico
print(aluno["endereco"]["estado"])

# acessando campo dentro de um array
print(aluno["Array"][1])

# alterar dados do dicionario
aluno["idade"] = 20
print(aluno["idade"])

# alterar dados dentro de um array, dentro do dicionario
aluno["Array"][2] = 9
print(aluno["Array"][2])


# alterar dados de um dicionario que esta dentro de outro
aluno["endereco"]["cidade"] = "São Paulo"
print(aluno["endereco"]["cidade"])

# adicionar um novo campo
aluno["periodo"] = "Noturno"
print(aluno["periodo"])

print("\n")

# removendo um campo do dicionario
# del aluno["idade"], aluno ["endereco"] # usamos virgula para deletar mais de um campo.
# print(aluno)

# percorrer um dicionario usando laco de repeticao para retornar as chaves
for chave in aluno:
    print(chave)

print("\n")

# percorrer um dicionario usando laco de repeticao para retornar os valores

for valor in aluno.values(): # values retorna apenas os valores dentro do dicionario aluno
    print(valor)

print("\n")

# percorrer um dicionario e retornar chave e valores

for chave, valor in aluno.items(): # items retorna as chaves e os valores dentro do dicionario aluno, usando a virgula para separar chave e valor
    print(chave, ":", valor)