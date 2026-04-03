print("Exercício 1.")

numero1 = int(input("Digite o primeiro número: "))
numero2 = int(input("Digite o segundo número: "))

maior_menor = f"O maior número é o n1: {numero1} e o menor é o n2: {numero2}" if numero1 > numero2 else f"O maior número é o n2: {numero2} e o menor é o n1: {numero1}"
print(maior_menor)

print("\n")

print("Exercício 2")

mes = int(input("Digite o número: "))

if mes == 1:
    print("O mês 1 é janeiro") 
elif mes == 2:
    print("O mês 2 é fevereiro")
elif mes == 3:
    print("O mês 3 é março")
elif mes == 4:
    print("O mês 4 é abril")
elif mes == 5:
    print("O mês 5 é maio")
elif mes == 6:
    print("O mês 6 é julho")
elif mes == 7:
    print("O mês 7 é junho")
elif mes == 8:
    print("O mês 8 é agosto")
elif mes == 9:
    print("O mês 9 é setembro")
elif mes == 10:
    print("O mês 10 é outubro")
elif mes == 11:
    print("O mês 11 é novembro")
elif mes == 12:
    print("O mês 12 é dezembro")
else:
    print("Digite um número entre 1 a 12")


print("\n")

print("Exercício 3")

num1 = int(input("Digite o número: "))

par_impar = f"O número {num1} é par" if num1 % 2 == 0 else f"O número {num1} é impar."
print(par_impar)

