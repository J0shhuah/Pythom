soma = 0
for i in range (1,5):
    nota = float(input(f'Digite a nota {i}: ').replace(',','.'))
    soma += nota
print(f'A soma é {soma}')
print(f'A média é {soma/4}')