import pandas as pd
import os

EXCEL_FILE = "base_BANCO_TABAJARA.xlsx"

def inicializar_arquivo():
    """
    Garante que o arquivo Excel exista.
    Caso não exista, cria um DataFrame vazio com as colunas necessárias.
    """
    if not os.path.exists(EXCEL_FILE):
        pd.DataFrame(columns=[
            "nome_cliente", "tipo_conta", "numero_conta",
            "cpf", "agencia", "extrato_bancario", "deposito", "saque"
        ]).to_excel(EXCEL_FILE, index=False)


def carregar_dados():
    """
    Lê o arquivo Excel e retorna um DataFrame atualizado,
    garantindo que a coluna 'cpf' seja tratada como string
    para evitar problemas de formatação.
    """
    clientes_banco = pd.read_excel(EXCEL_FILE)

    # Garantir CPF como string (evita perda de zeros à esquerda)
    clientes_banco["cpf"] = clientes_banco["cpf"].astype(str)

    return clientes_banco


def salvar_dados(clientes_banco):
    """
    Salva o DataFrame atualizado no arquivo Excel.
    """
    clientes_banco.to_excel(EXCEL_FILE, index=False)


def criar_conta():
    """
    Cria uma nova conta bancária com validações básicas:
    - Tipo de conta válido
    - CPF não duplicado
    - Limite de contas/agências
    """
    clientes_banco = carregar_dados()

    nome_cliente = input("Digite o nome do cliente: ")
    cpf = input("Digite o CPF: ")
    tipo_conta = input("Tipo de conta (Corrente, Poupança, Salario): ")

    # Verificar se o tipo de conta é válido (Corrente, Poupança ou Salario)
    if tipo_conta not in ["Corrente", "Poupança", "Salario"]:
        print("Tipo de conta inválido.")
        return  # Retorna ao menu sem criar conta

    # Verifica se o CPF já está cadastrado
    if cpf in clientes_banco["cpf"].values:
        print("CPF já cadastrado.")
        return

    # Gerar número de conta sequencial (começa do 0 se vazio)
    numero_conta = int(clientes_banco["numero_conta"].max()) + 1 if not clientes_banco.empty else 0

    # Gerar número de agência sequencial (começa do 400 se vazio)
    agencia = int(clientes_banco["agencia"].max()) + 1 if not clientes_banco.empty else 400

    # Limite de contas ou agências
    if numero_conta > 100 or agencia > 700:
        print("Limite de contas ou agências atingido.")
        return

    novo_cliente = {
        "nome_cliente": nome_cliente,
        "tipo_conta": tipo_conta,
        "numero_conta": numero_conta,
        "cpf": cpf,
        "agencia": agencia,
        "extrato_bancario": 0,
        "deposito": 0,
        "saque": 0
    }

    # Adiciona novo cliente ao DataFrame
    clientes_banco = pd.concat([clientes_banco, pd.DataFrame([novo_cliente])], ignore_index=True)

    # Salva os dados atualizados no Excel
    salvar_dados(clientes_banco)

    print(f"\nConta criada com sucesso! Nome: {nome_cliente}, CPF: {cpf}, "
          f"Tipo: {tipo_conta}, Conta: {numero_conta}, Agência: {agencia}")


def acessar_conta():
    """
    Permite acessar uma conta existente através do CPF e número da conta.
    """
    clientes_banco = carregar_dados()

    cpf = input("Digite o CPF: ")

    try:
        numero_conta = int(input("Digite o número da conta: "))
    except ValueError:
        print("Número de conta inválido.")
        return

    # Busca cliente pelo CPF e número da conta
    cliente = clientes_banco[
        (clientes_banco["cpf"] == cpf) &
        (clientes_banco["numero_conta"] == numero_conta)
    ]

    if not cliente.empty:
        print(f"\nBem-vindo {cliente.iloc[0]['nome_cliente']} ao banco Tabajara!")
    else:
        print("\nUsuário não encontrado, tente novamente ou realize o cadastro.")


def menu():
    """
    Exibe o menu principal do sistema e controla a navegação do usuário.
    """
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

# if 
if __name__ == "__main__":
    # Inicializa o arquivo e inicia o sistema
    inicializar_arquivo()
    menu()

