notas = [10, 8, 5, 10, 4, 7, 2, "Jamal"]

notas.append("Senac") # insere o valor entre parênteses no final da lista
print(notas)

print("\n")

notas.insert(0, False) # insere o valor entre parênteses na posição indicada
notas.remove("Jamal") # remove a informação entre parênteses
print(notas)
print("\n")

novos_numeros = [390, "Adenilson", 19, "Anna", 45, "Iara", 390]

# notas.extend(novos_numeros) # junta as listas, adicionando os elementos da que está entre parênteses à primeira lista

# novos_numeros.pop(3) # se não for indicado o índice, remove o último elemento da lista
# print(novos_numeros)

# print(novos_numeros.clear()) # limpa a lista, deixando-a vazia

# index
print(novos_numeros.index(390)) # retorna o índice do elemento entre parênteses
numeros = [12, 45, 67, 12, 89, 12]
numeros.sort() # ordena a lista em ordem crescente
print(numeros)

nomes = ["Maria", "Ana", "João", "Carlos"]
nomes = ["Maria", "Ana", "João", "Carlos"]  