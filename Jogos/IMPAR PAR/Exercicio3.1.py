import random

ImparPar = (input('Escolha IMPAR ou PAR: '))
numero = int(input('Digite um número: '))
numeroAleatorio = random.randint(1,10)
print('Máquina:',numeroAleatorio)


Soma = numeroAleatorio+numero
print(f'Soma: {Soma}')
if Soma%2 == 0:
    print('O número é PAR!')
else:
    print('O número é IMPAR!')

par = True
