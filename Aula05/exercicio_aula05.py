
while True:
     numero = input("Digite um número inteiro: ").strip()
     if numero.isdigit():
         numero_valido = int(numero)
         break
     else: 
         print("Digite um número válido")
        
for i in range (1, 11):
     resultado = i * numero_valido
     print(f"{numero_valido} x {i} = {resultado}")



# while True:
#     numero = input("Digite um número inteiro: ").strip()
#     if numero.isdigit():
#         numero_valido = int(numero)
#         break
#     else: 
#         print("Digite um número válido.")


# while True:
#     multiplicador = input("Digite até qual número ele deve ser multiplicado: ").strip()

#     if multiplicador.isdigit():
#         multiplicador_valido = int(multiplicador)
#         break
#     else:
#         print("Digite um número valido.")

# for multiplicador_valido in range (1, multiplicador_valido +1 ):
#     resultado = multiplicador_valido * numero_valido        
#     print(f"{numero_valido} x {multiplicador_valido} = {resultado}")