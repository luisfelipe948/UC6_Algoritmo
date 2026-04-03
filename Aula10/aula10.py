#open("nota.txt", "w" ) # Cria o arquivo nota.txt, caso ele não exista, e apaga o conteúdo caso ele já exista

# abrir um arquivo e digitar infomações 
with open("Aula10/nota.txt", "w") as nota_aluno:
    nota_aluno.write("Ola mundo")


# ler o conteúdo do arquivo
with open("Aula10/nota.txt", "r") as leitura_arquivo:
    recebe_leitura = leitura_arquivo.read()
    print(recebe_leitura)

# adicionar um texto no final do seu arquivo
with open("Aula10/nota.txt", "a") as adiciona_texto:
    adiciona_texto.write("\n Adicionando mais uma linha")