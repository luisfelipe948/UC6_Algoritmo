import pandas as pd


print("     Bem-Vindo ao Portal de Alunos")
print("\n")
print("     Digite uma opção no menu")
print("         1 > Criar")
print("         2 > Adicionar")
print("         3 > Apagar")
opcao = int(input("R: "))

if opcao == 1:
    print("Opção 1 selececionada.")
    nome = str(input("Digite seu nome: "))
    idade = int(input("Digite a idade: "))
    altura = float(input("Digite a altura: "))

    dados = {
        "nome": [nome],
        "idade": [idade],
        "altura": [altura]
}
    
    excel = pd.DataFrame(dados)                                 # criando um DataFrame a partir do dicionário
    excel.to_excel("Aula12\portal_alunos.xlsx", index=False)    # exportando o DataFrame para um arquivo Excel

elif opcao == 2:
    print("Opção 2 selecionada.")
    print()