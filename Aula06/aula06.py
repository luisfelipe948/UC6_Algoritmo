texto1 = "Senac"

print(texto1[0])
print(texto1[1])
print(texto1[2])
print(texto1[3])
print(texto1[4])

# função len()

print("\n")

texto2 = "MUSICA TRISTE NÃO TOCA EM FESTA EU SEI QUE NO FUNDO VOCE DETESTA AAH, I LIKE DO WAY YOU KISS ME I CAN TELL MISS ME I CAN TELL THIS THIS THIS, MUITO PRAZER ESSE SOU EU, O MAIOR OTARIO DA CIDADE, EXAGERADO JOGADO AOS SEUS PES, EU SOU MESMO EXAGERADO, NAS SOMBRAS, VOCE É MEU CASTIGO MAS EU SEMPRE INSISTO ME ASSOMBRA, UM TOQUE VAZIO TENTANDO ALCANÇAR, O QUE EU MAIS QUERO É TE AMAR NA PRAIA (AAAAAA) DIZ EU TE AMO BEM NA SUA CARA (AAAAAAAAAAAAAA)"

print(len(texto2))

print("\n")

# função mai/min

texto3 = "ola safadinhos"
print(texto3.upper())

print("\n")

texto4 = "AI BOLSONARO"
print(texto4.lower())

print(texto4.capitalize())

print(texto4.title())


texto5 = "Python"

print(texto5[0:5])

# replace

texto6 = "Hoje é aula da Heloisa"
texto_replace = texto6.replace("da Heloisa", "do Zé Milton")
print(texto_replace)

# espaço em branco

texto7 = "    adkjakjdasdasdasdasdas   "
print(texto7.strip()) # remove os espaços em branco dos dois lados
print(texto7.lstrip()) # remove da esquerda
print(texto7.rstrip()) # remove da direita
