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
    nome = str(input("Digite seu nome: "))
    idade = int(input("Digite a idade: "))
    altura = float(input("Digite a altura: "))
    
    dados = {
        "nome": [nome],
        "idade": [idade],
        "altura": [altura]
    }
    
    leitura_excel = pd.read_excel("Aula12\portal_alunos.xlsx")
    nova_linha = len(leitura_excel)
    
    leitura_excel.loc[nova_linha, nome] = dados ["nome"]
    leitura_excel.loc[nova_linha, idade] = dados ["idade"]
    leitura_excel.loc[nova_linha, altura] = dados ["altura"]
    
    leitura_excel.to_excel("Aula12\portal_alunos.xlsx", index=False)
    print("Dados adicionados com sucesso!")


elif opcao == 3:
    print("Opção 3 selecionada.")
    leitura_apagado = int(input("Digite o número da linha que deseja apagar: "))

    leitura_excel = pd.read_excel("Aula12\portal_alunos.xlsx")
    leitura_excel.to_excel("Aula12\portal_alunos.xlsx", index=False)