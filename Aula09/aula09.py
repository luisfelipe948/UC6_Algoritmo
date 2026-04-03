def soma(valor1, valor2):  # a função soma recebe dois parâmetros, valor1 e valor2, e retorna a soma desses valores
    return valor1 + valor2

print(soma(1457, 10))


salario_funcionario = 1600
beneficio = 200

novo_salario = soma(salario_funcionario, beneficio)
print(novo_salario)

# ---------------------------------------------------------------

idade_usuario = int(input("Digite sua idade: "))

if idade_usuario >= 18:
    var1 = float(input("Digite o primeiro valor: "))
    var2 = float(input("Digite o segundo valor: "))
    resultado = soma(var1, var2)
    print("O resultado da soma é: ", resultado)
else:
    print("Você não tem idade suficiente para realizar a operação.")

# -------------------------------------------------------------------

lista = [20, 1, 6, 10, 45]
palavra = "Senac"
print(len(lista)) # retorna o número de elementos da lista

print(len(palavra)) # retorna o número de caracteres da string

print(sum(lista)) # retorna a soma dos elementos da lista

print(max(lista)) # retorna o maior valor da lista

print(min(lista)) # retorna o menor valor da lista

print(sorted(lista)) # retorna a lista ordenada em ordem crescente

print(sorted(lista, reverse=True)) # retorna a lista ordenada em ordem decrescente

tipo = 10
print(type(tipo)) # retorna o tipo da variável lista

print(float(tipo)) # converte a variável tipo para float