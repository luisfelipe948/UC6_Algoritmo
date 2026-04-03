import pandas as pd
import os

EXCEL_FILE = "Aula14/base_BANCO_TABAJARA.xlsx"

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
    
    # Garantir que extrato_bancario seja float para aceitar valores com decimal
    clientes_banco["extrato_bancario"] = clientes_banco["extrato_bancario"].astype(float)

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
        "extrato_bancario": 1000,
        "deposito": 0,
        "saque": 0
    }

    # Adiciona novo cliente ao DataFrame
    clientes_banco = pd.concat([clientes_banco, pd.DataFrame([novo_cliente])], ignore_index=True)

    # Salva os dados atualizados no Excel
    salvar_dados(clientes_banco)

    print(f"\nConta criada com sucesso! Nome: {nome_cliente}, CPF: {cpf}, "
          f"Tipo: {tipo_conta}, Conta: {numero_conta}, Agência: {agencia}")
    

def saque(cliente, clientes_banco):
    """
    Realiza um saque, com as seguintes regras: 
        Saques na conta Corrente: 5% de taxa 
        Saques na conta Poupança: 0% de taxa 
        Saques na conta Salário: 2% de taxa

    """

    tipo_conta = cliente.iloc[0]["tipo_conta"]
    saldo_atual = cliente.iloc[0]["extrato_bancario"]
    indice_cliente = cliente.index[0]

    taxas = {
        "Corrente": 0.05,
        "Poupança": 0,
        "Salario": 0.02
    }

    taxa = taxas[tipo_conta]

    valor_saque = float(input("Digite o valor do saque: "))

    # Validar se o valor é maior que o disponível em conta
    if valor_saque > saldo_atual:
        print("\nValor maior que o disponivel em conta")
        return

    # Calcular o desconto da taxa
    valor_desconto = valor_saque * taxa

    # Novo saldo = saldo atual - saque - taxa
    novo_saldo = saldo_atual - valor_saque - valor_desconto

    # Atualizar saldo da conta
    clientes_banco.loc[indice_cliente, "extrato_bancario"] = novo_saldo

    # Salvar dados atualizados
    salvar_dados(clientes_banco)

    # Exibir comprovante
    print("="*30)
    print("Saque realizado com sucesso!")
    print(f"Saque: {valor_saque:.2f}")
    print(f"Valor em conta: {saldo_atual:.2f}")
    print(f"Taxa para saque: {taxa*100:.0f}%") 
    print(f"Valor total do saque: {valor_saque + valor_desconto:.2f}")
    print(f"Saldo após saque: {novo_saldo:.2f}")
    print("="*30 + "\n")

def deposito(cliente, clientes_banco):
    """
    Realiza um depósito, com as seguintes regras: 
        Depósitos na conta Corrente: 0% de taxa 
        Depósitos na conta Poupança: 0% de taxa 
        Depósitos na conta Salário: 0% de taxa

    """

    tipo_conta = cliente.iloc[0]["tipo_conta"]
    saldo_atual = cliente.iloc[0]["extrato_bancario"]
    indice_cliente = cliente.index[0]

    valor_deposito = float(input("Digite o valor do depósito: "))

    # Validar se o valor é positivo
    if valor_deposito <= 0:
        print("\nValor de depósito deve ser positivo.")
        return

    # Novo saldo = saldo atual + depósito
    novo_saldo = saldo_atual + valor_deposito

    # Atualizar saldo da conta
    clientes_banco.loc[indice_cliente, "extrato_bancario"] = novo_saldo

    # Salvar dados atualizados
    salvar_dados(clientes_banco)

    # Exibir comprovante
    print("="*30)
    print("Depósito realizado com sucesso!")
    print(f"Depósito: {valor_deposito:.2f}")
    print(f"Valor em conta: {saldo_atual:.2f}")
    print(f"Saldo após depósito: {novo_saldo:.2f}")
    print("="*30 + "\n")

def acessar_conta():
    """
    Permite acessar uma conta existente através do CPF e número da conta.
    """
    cpf = input("Digite o CPF: ")

    try:
        numero_conta = int(input("Digite o número da conta: "))
    except ValueError:
        print("Número de conta inválido.")
        return

    clientes_banco = carregar_dados()

    # Busca cliente pelo CPF e número da conta
    cliente = clientes_banco[
        (clientes_banco["cpf"] == cpf) &
        (clientes_banco["numero_conta"] == numero_conta)
    ]

    if not cliente.empty:
        print(f"\nBem-vindo {cliente.iloc[0]['nome_cliente']} ao banco Tabajara!")
        while True:
            # Recarrega os dados a cada iteração para manter os saldos atualizados
            clientes_banco = carregar_dados()
            cliente = clientes_banco[
                (clientes_banco["cpf"] == cpf) &
                (clientes_banco["numero_conta"] == numero_conta)
            ]
            
            print("\n--- Menu da Conta ---")
            print("1 - Saque\n2 - Depósito\n3 - Saldo\n4 - Sair")

            # Solicita a opção do usuário
            opcao = input("Escolha uma opção: ")

            if opcao == "1":
                saque(cliente, clientes_banco)
            elif opcao == "2":
                deposito(cliente, clientes_banco)
            elif opcao == "3":
                print(f"Saldo atual: {cliente.iloc[0]['extrato_bancario']:.2f}")
            elif opcao == "4":
                print("Saindo da conta...")
                break
            else:
                print("Opção inválida.")

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
