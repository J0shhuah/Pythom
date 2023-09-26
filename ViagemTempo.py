from datetime import date
from colorama import Fore, init
from random import randint
import time
diaAtual = date.today().day
mesAtual = date.today().month
anoAtual = date.today().year

while True :
    print('')
    print(f'\033[1;37mDATA ATUAL\033[m: \033[31m{diaAtual}/{mesAtual}/{anoAtual}\033[m\n')
    iniciar = input('Deseja iniciar a viajem no tempo? \033[1;37m[S]\033[m ou \033[1;37m[N]\033[m: ')
    if iniciar == 'S'.replace('S','s'):
        aFut = randint(50,2000) + anoAtual
        mFut = randint(1,12) 
        dFut = randint (1,30) 
    print('')

    viagem = ['*\033[34m*\033[m* \033[34mLIGANDO OS MOTORES 🚀 \033[m*\033[34m*\033[m*', 
              '*\033[34m*\033[m* \033[34mATIVANDO AS TURBINAS 🔥\033[m *\033[34m*\033[m*',
              '*\033[34m*\033[m* \033[34mATIVANDO O RESFRIAMENTO AUTOMÁTICO 🧊\033[m *\033[34m*\033[m*',
              '*\033[34m*\033[m* \033[34mATIVANDO O ACELERADOR DE PARTÍCULAS 🥼\033[m *\033[34m*\033[m*',
              '5',
              '4',
              '3',
              '2',
              '1',
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
    print('\n\n\n\n\n\n\n\n\n\n')
    print('\033[1;37m#\033[m'*45)
    print('')
    
    print('~\033[34m~\033[m~ \033[36mBem vindo ao futuro, viajante!!\033[m ~\033[34m~\033[m~')
    time.sleep(1)
    print('')
    print(f'🌟 O ano é \033[31m{dFut}/{mFut}/{aFut}\033[m 🌟')
    time.sleep(3)
    print('')
    eventos = ["\033[1;37m ~~ Neste ano foi descoberto vida em outro planeta. ~~\033[m",
               "\033[1;37m ~~ Neste século uma pesquisa sobre células tronco marcou a história ~~\033[m",
               "\033[1;37m ~~ Essa década foi marcada por uma terrível doença. ~~ \033[m",
               "\033[1;37m ~~ Neste dia houve uma chuva de meteoros histórica. ~~ \033[m",
               "\033[1;37m ~~ Esse século foi marcado pela descoberta da cura do câncer. ~~ \033[m",
               "\033[1;37m ~~ Hoje é o dia internacional do cachorro quente. ~~ \033[m",
                "\033[1;37m ~~ Neste ano foram criados exoesqueletos funcionais aos humanos. ~~ \033[m",
                "\033[1;37m ~~ Hoje foram descobertos fósseis em marte. ~~ \033[m",
                "\033[1;37m ~~ Esse ano foi marcado por um furacão terrível. ~~ \033[m",
                "\033[1;37m ~~ Nesta década as crises climáticas chegaram ao seu ápice. ~~ \033[m",
                "\033[1;37m ~~ Nesse século foi feito um acordo de paz entre todos os países. ~~ \033[m"
                ]
    
    i = (randint(1,4) - 1)
    print(eventos[i])
    print('\n')
    break   