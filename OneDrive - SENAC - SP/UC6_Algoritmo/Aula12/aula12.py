import pandas as pd

nome = str(input("Digite seu nome: "))
idade = int(input("Digite a idade: "))
altura = float(input("Digite a altura: "))

# criando um dicionário com os dados do usuário
dados = {
    "nome": [nome],
    "idade": [idade], # os colchetes são usados para criar uma lista, pois o DataFrame espera uma estrutura de dados em forma de lista ou array
    "altura": [altura]
}

# excel = pd.DataFrame(dados) # criando um DataFrame a partir do dicionário

# excel.to_excel("Aula12\cadastro_usuario.xlsx", index=False) # exportando o DataFrame para um arquivo Excel


# ler o excel

leitura_excel = pd.read_excel("Aula12\cadastro_usuario.xlsx")

# lendo o arquivo Excel e armazenando em um DataFrame
# nova_linha = len(leitura_excel) # obtendo o número de linhas do DataFrame para determinar a posição da nova linha


# leitura_excel.loc[nova_linha, "nome"] = dados["nome"]
# leitura_excel.loc[nova_linha, "idade"] = dados["idade"]
# leitura_excel.loc[nova_linha, "altura"] = dados["altura"]


# print(leitura_excel["nome"])

# apagar linhas de uma planilha
# leitura_excel = leitura_excel.drop(0) 


leitura_excel.loc[0, "nome"] = dados["nome"]
leitura_excel.loc[0, "idade"] = dados["idade"]
leitura_excel.loc[0, "altura"] = dados["altura"]

# save
leitura_excel.to_excel("Aula12\cadastro_usuario.xlsx", index=False) # exportando o DataFrame atualizado para o arquivo Excel