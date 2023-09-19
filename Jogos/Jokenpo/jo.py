from random import randint
from time import sleep
from colorama import Fore, init

escolhaPlayer = int(input('''
PEDRA [1] 
PAPEL [2]
TESOURA [3]
Faça a sua escolha: '''))
if(escolhaPlayer >3):
    print('Escolha um número válido \033[0;31mBOBÃO\033[m')
else:
    if(escolhaPlayer == 1):
        print('Você escolheu \033[0;34mPEDRA\033[m')
    elif(escolhaPlayer == 2):
        print('Você escolheu \033[0;34mPAPEL\033[m')
    elif(escolhaPlayer == 3):
        print ('Você escolheu \033[0;34mTESOURA\033[m')


    escolhaComputador = randint(1,3)
    if(escolhaComputador == 1):
        print('O computador escolheu: \033[0;34mPEDRA\033[m')
    if(escolhaComputador == 2):
        print('O computador escolheu: \033[0;34mPAPEL\033[m')
    if(escolhaComputador == 3):
        print('O computador escolheu: \033[0;34mTESOURA\033[m')

    if(escolhaPlayer == 1 and escolhaComputador == 2 or
    escolhaPlayer == 2 and escolhaComputador == 3):
        print(Fore.RED+'VOCÊ PERDEU!🤡')
    elif(escolhaPlayer == escolhaComputador):
        print('\033[0;33mEMPATE\033[m 🥶')

    else:
        print(Fore.GREEN+'VOCÊ GANHOU!🤑')
    
