'''Exercício JO-KEN-PO o Jogador escolherá pedra 
papel ou tesoura e o computador também através de
um número aleatório de 1 a 3 
@author alunos de python data 18/09/2023
version 1.0
'''
from random import randint
from time import sleep
from colorama import Fore, init
init(autoreset=True)
print('#'*50)
print('''Bem vindo ao JO-KEN-PO😀''')

acumularPonto = 0

escolhaPlayer = int(input('''
Digite [1] - Pedra 
Digite [2] - Papel
Digite [3] - Tesoura
Faça a escolha: '''))
print(f'Sua escolha foi {escolhaPlayer}')
if (escolhaPlayer == 1): 
    print(f'A sua escolha foi PEDRA')
elif (escolhaPlayer == 2):
    print(f'A sua escolha foi PAPEL')
elif(escolhaPlayer == 3):
    print(f'A sua escolha foi TESOURA')
else:
    print('Digite a opção entre 1 e 3 e reinicie o jogo')

sleep(1)
print('JO')
sleep(1)
print(Fore.RED +'KEN')
sleep(1)
print('PO')
sleep(1)

escolhaComputador = randint(1,3)
print(escolhaComputador)

if (escolhaComputador == 1): 
    print(f'O computador escolheu PEDRA')
elif (escolhaComputador == 2):
    print(f'O computador escolheu PAPEL')
else:
    print(f'O computador escolheu TESOURA')
if(escolhaPlayer == escolhaComputador):
    print(f'Empate')

elif((escolhaPlayer == 1 and escolhaComputador == 3) or 
     (escolhaPlayer == 2 and escolhaComputador == 1) or
     (escolhaPlayer == 3 and escolhaComputador == 2)):
    print('Você ganhou')
else:
    print('Você perdeu')

print(f'Sua pontuação é {acumularPonto}')




escolhaPlayer = int(input('''
Digite [1] - Pedra 
Digite [2] - Papel
Digite [3] - Tesoura
Faça a escolha: '''))
print(f'Sua escolha foi {escolhaPlayer}')
if (escolhaPlayer == 1): 
    print(f'A sua escolha foi PEDRA')
elif (escolhaPlayer == 2):
    print(f'A sua escolha foi PAPEL')
elif(escolhaPlayer == 3):
    print(f'A sua escolha foi TESOURA')
else:
    print('Digite a opção entre 1 e 3 e reinicie o jogo')

sleep(1)
print('JO')
sleep(1)
print(Fore.RED +'KEN')
sleep(1)
print('PO')
sleep(1)

escolhaComputador = randint(1,3)
print(escolhaComputador)

if (escolhaComputador == 1): 
    print(f'O computador escolheu PEDRA')
elif (escolhaComputador == 2):
    print(f'O computador escolheu PAPEL')
else:
    print(f'O computador escolheu TESOURA')
if(escolhaPlayer == escolhaComputador):
    print(f'Empate')

elif((escolhaPlayer == 1 and escolhaComputador == 3) or 
     (escolhaPlayer == 2 and escolhaComputador == 1) or
     (escolhaPlayer == 3 and escolhaComputador == 2)):
    print('Você ganhou')
else:
    print('Você perdeu')
    
acumularPonto = acumularPonto + 1
print(f'Sua pontuação é {acumularPonto}')



escolhaPlayer = int(input('''
Digite [1] - Pedra 
Digite [2] - Papel
Digite [3] - Tesoura
Faça a escolha: '''))
print(f'Sua escolha foi {escolhaPlayer}')
if (escolhaPlayer == 1): 
    print(f'A sua escolha foi PEDRA')
elif (escolhaPlayer == 2):
    print(f'A sua escolha foi PAPEL')
elif(escolhaPlayer == 3):
    print(f'A sua escolha foi TESOURA')
else:
    print('Digite a opção entre 1 e 3 e reinicie o jogo')

sleep(1)
print('JO')
sleep(1)
print(Fore.RED +'KEN')
sleep(1)
print('PO')
sleep(1)

escolhaComputador = randint(1,3)
print(escolhaComputador)

if (escolhaComputador == 1): 
    print(f'O computador escolheu PEDRA')
elif (escolhaComputador == 2):
    print(f'O computador escolheu PAPEL')
else:
    print(f'O computador escolheu TESOURA')
if(escolhaPlayer == escolhaComputador):
    print(f'Empate')

elif((escolhaPlayer == 1 and escolhaComputador == 3) or 
     (escolhaPlayer == 2 and escolhaComputador == 1) or
     (escolhaPlayer == 3 and escolhaComputador == 2)):
    print('Você ganhou')
else:
    print('Você perdeu')
    
print(f'Sua pontuação é total é {acumularPonto}')
