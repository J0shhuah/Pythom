from datetime import date
from colorama import Fore, init
from random import randint
import time
diaAtual = date.today().day
mesAtual = date.today().month
anoAtual = date.today().year

while True :
    print('')
    print(f'DATA ATUAL: {diaAtual}/{mesAtual}/{anoAtual}\n')
    iniciar = input('Deseja iniciar a viajem no tempo? [S] ou [N]: ')
    if iniciar == 'S'.replace('S','s'):
        aFut = randint(50,2000) + anoAtual
        mFut = randint(1,12) 
        dFut = randint (1,30) 
    print('')

    viagem = ['*\033[34m*\033[m* \033[34mLIGANDO OS MOTORES 🚀 \033[m*\033[34m*\033[m*', 
              '*\033[34m*\033[m* \033[34mATIVANDO AS TURBINAS 🔥\033[m *\033[34m*\033[m*',
              '*\033[34m*\033[m* \033[34mATIVANDO O RESFRIAMENTO AUTOMÁTICO 🧊\033[m *\033[34m*\033[m*',
              '*\033[34m*\033[m* \033[34mATIVANDO O ACELERADOR DE PARTÍCULAS 🥼\033[m *\033[34m*\033[m*',
              '',
              '*\033[33m*\033[m*\033[31mBOOM\033[m*\033[33m*\033[m*']
    
            
    for t in (viagem):
        print(t)
        time.sleep(1)
    print('')
    print('🔥'*20)
    print('🔥'*20)
    print('🔥'*20)
    print('🔥'*20)
    print('🔥'*20)
    print('🔥'*20)
    print('🔥'*20)
    print('🔥'*20)
    print('🔥'*20)
    print('🔥'*20)
    print('🔥'*20)
    print('🔥'*20)
    print('🔥'*20)
    print('🔥'*20)
    print('🔥'*20)
    print('🔥'*20)
    print('🔥'*20)
    print('🔥'*20)
    print('🔥'*20)
    print('🔥'*20)
    print('🔥'*20)
    print('🔷'*20)
    print('🔷'*20)
    print('🔷'*20)
    print('🔷'*20)
    print('🔷'*20)
    print('🔷'*20)
    print('🔷'*20)
    print('🔷'*20)
    print('🔷'*20)
    print('🔷'*20)
    print('🔷'*20)
    print('')
    print('\033[1;37m#\033[m'*45)
    
    print(f'🌟 O ano é \033[31m{dFut}/{mFut}/{aFut}\033[m 🌟')

    eventos = ["Neste ano foi descoberto vida em outro planeta.",
               "Neste século uma pesquisa sobre células tronco marcou a história",
               "Essa década foi marcada por uma terrível doença.",
               "Neste dia houve uma chuva de meteoros histórica.",]
    i = (randint(1,4) - 1)
    print(eventos[i])
   