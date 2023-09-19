numero = int(input('Digite o número: '))
if numero>1:
    for i in range(2, numero):
        if (numero %i) == 0:
            print('Não é primo')
            break
        else:
            print('É primo')

