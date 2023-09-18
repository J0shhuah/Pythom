soma = 0
for i in range(1,5):
    nota = float(input(f'Digitge a nota {i}: ').replace(',', ('.')))
    soma += nota 
print(f'A soma {soma}')