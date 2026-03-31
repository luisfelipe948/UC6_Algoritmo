import requests
# API
url = "https://rickandmortyapi.com/api/character/"

# Menu

print("Escolha uma opção:")
print("1. Consultar por ID")
print("2. Consultar por Nome")
print("3. Ver Lista de Personagens")
opcao = int(input("Digite o número da opção desejada: "))

print("----------------------------------")

if opcao == 1:
    id = int(input("Digite um número inteiro: "))
    link_API = f"https://rickandmortyapi.com/api/character/{id}"
    resposta = requests.get(link_API)
    novo_json = resposta.json()
    print("Nome: ", novo_json["name"])
    print("Status: ", novo_json["status"])
    print("Especie: ", novo_json["species"])
    print("----------------------------------")



elif opcao == 2:
    nome = input("Digite o nome do personagem: ")
    link_API_nome = f"https://rickandmortyapi.com/api/character/?name={nome}"
    resposta_nome = requests.get(link_API_nome)
    json_nome = resposta_nome.json()
    if "results" in json_nome:
        personagem_nome = json_nome["results"][0]
        print("Nome: ", personagem_nome["name"])
        print("Status: ", personagem_nome["status"])
        print("Especie: ", personagem_nome["species"])
    else:
        print("Personagem não encontrado.")
    print("----------------------------------")


elif opcao == 3:
    resposta_lista = requests.get(url)
    json_lista = resposta_lista.json()
    personagens_lista = json_lista["results"]
    print("Lista de personagens:")
    for personagem in personagens_lista:
        print(personagem["name"])
else:
    print("Opção inválida.")
