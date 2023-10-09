# 1. Crie uma lista chamada 'nomes' com pelo menos 5 nomes de pessoas.
nomes = ["Alice", "Bob", "Carol", "David", "Eva"]

# 2. Crie uma sublista chamada 'sublista_nomes' que contenha os nomes da posição 1 à 3 da lista 'nomes'.
sublista_nomes = nomes[1:4]

# 3. Imprima a sublista 'sublista_nomes'.
print("Sublista de nomes:", sublista_nomes)

# 4. Crie um loop for para iterar sobre a lista 'nomes' e imprima cada nome em uma linha.
print("Nomes na lista:")
for nome in nomes:
    print(nome)

# 5. Verifique se "Eva" está na lista 'nomes' e imprima o resultado.
nome_a_procurar = "Eva"
if nome_a_procurar in nomes:
    print(nome_a_procurar, "está na lista.")
else:
    print(nome_a_procurar, "não está na lista.")

# 6. Conte quantos nomes na lista 'nomes' começam com a letra "A" e imprima o resultado.
letra_a_contagem = sum(1 for nome in nomes if nome.startswith("A"))
print("Número de nomes que começam com 'A':", letra_a_contagem)