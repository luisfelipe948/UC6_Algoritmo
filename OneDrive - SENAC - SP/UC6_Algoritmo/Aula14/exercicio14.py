import pandas as pd
import os

EXCEL_FILE = "base_BANCO_TABAJARA.xlsx"

# Função para garantir que o arquivo Excel exista
def inicializar_arquivo():
    if not os.path.exists(EXCEL_FILE):
        pd.DataFrame(columns=[
            "nome_cliente", "tipo_conta", "numero_conta",
            "cpf", "agencia", "extrato_bancario", "deposito", "saque"
        ]).to_excel(EXCEL_FILE, index=False)

# Função para carregar o DataFrame
def carregar_dados():
    clientes_banco = pd.read_excel(EXCEL_FILE)
    clientes_banco["cpf"] = clientes_banco["cpf"].astype(str)  # Garantir CPF como string
    return clientes_banco

# Função para salvar o DataFrame
def salvar_dados(clientes_banco):
    clientes_banco.to_excel(EXCEL_FILE, index=False)

# Função para criar uma conta
def criar_conta():
    clientes_banco = carregar_dados()
    nome_cliente = input("Digite o nome do cliente: ")
    cpf = input("Digite o CPF: ")
    tipo_conta = input("Tipo de conta (Corrente, Poupança, Salario): ")

    if tipo_conta not in ["Corrente", "Poupança", "Salario"]:
        print("Tipo de conta inválido.")
        return

    if cpf in clientes_banco["cpf"].values:
        print("CPF já cadastrado.")
        return

    numero_conta = int(clientes_banco["numero_conta"].max()) + 1 if not clientes_banco.empty else 0
    agencia = int(clientes_banco["agencia"].max()) + 1 if not clientes_banco.empty else 400

    if numero_conta > 100 or agencia > 700:
        print("Limite de contas ou agências atingido.")
        return

    novo_cliente = {
        "nome_cliente": nome_cliente, "tipo_conta": tipo_conta,
        "numero_conta": numero_conta, "cpf": cpf, "agencia": agencia,
        "extrato_bancario": 0, "deposito": 0, "saque": 0
    }

    clientes_banco = pd.concat([clientes_banco, pd.DataFrame([novo_cliente])], ignore_index=True)
    salvar_dados(clientes_banco)

    print(f"\nConta criada com sucesso! Nome: {nome_cliente}, CPF: {cpf}, "
          f"Tipo: {tipo_conta}, Conta: {numero_conta}, Agência: {agencia}")

# Função para acessar uma conta
def acessar_conta():
    clientes_banco = carregar_dados()
    cpf = input("Digite o CPF: ")
    try:
        numero_conta = int(input("Digite o número da conta: "))
    except ValueError:
        print("Número de conta inválido.")
        return

    cliente = clientes_banco[(clientes_banco["cpf"] == cpf) & (clientes_banco["numero_conta"] == numero_conta)]
    if not cliente.empty:
        print(f"\nBem-vindo {cliente.iloc[0]['nome_cliente']} ao banco Tabajara!")
    else:
        print("\nUsuário não encontrado, tente novamente ou realize o cadastro.")

# Função para exibir o menu
def menu():
    while True:
        print("\n--- Banco Tabajara ---")
        print("1 - Criar conta\n2 - Acessar conta\n3 - Sair")
        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            criar_conta()
        elif opcao == "2":
            acessar_conta()
        elif opcao == "3":
            print("Saindo do sistema...")
            break
        else:
            print("Opção inválida.")

# Execução principal
if __name__ == "__main__":
    inicializar_arquivo()
    menu()
