'''
Observador do futuro 

Autors: Guilherme de Moura, Joshua Rodrigues, João Pedro Neves
Version 1.0
'''

import datetime
from random import randint
import time

# Variáveis aqui :

hoje = datetime.datetime.now()
ano_atual = datetime.datetime.now().year

iniciar = "" 

# Interface do programa :
    # while iniciar != "s" or iniciar != "n" :
while True :
    print("\n\033[0;36m✦ ✧ ✦ ✧ ✦ ✧ ✦ ✧ ✦ ✧ ✦\033[m\n\n"
        "A data atual é:\n")
    print((hoje.strftime("%d/%m/%Y")))


    
    iniciar = input("\n\033[1;37mDeseja começar a viagem no tempo agora? [S] ou [N]\033[m\n").lower().strip()[0]

    if iniciar == "s" :

        a = randint(50, 1000)
        a = a + ano_atual
        m = randint(1,12)
        d = randint(1,30)

        futuro = datetime.date(a, m , d)
                
        carregamento = [
                        "\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n",
                        "\033[1;37m◇◇◇◇◇◇◇◇◇◇◇◇◇◇◇◇◇◇◇◇◇◇◇◇◇◇◇◇◇◇◇◇◇◇◇◇◇◇◇◇\033[m\n\n"
                        "\033[1;34m[/******] Energizando os motores...\033[m\n",
                        "\033[1;34m[//*****] Ativando a potência máxima...\033[m\n",
                        "\033[1;34m[///****] Soltando o freio de mão...\033[m\n",
                        "\033[1;34m[////***] Procurando rotas...\033[m\n",
                        "\033[1;34m[/////**] Viajando no vórtex temporal...\033[m\n",
                        "\033[1;34m[//////**] Saindo do vórtex...\033[m\n",
                        "\033[1;34m[///////*] Aterrizando a máquina...\033[m\n",
                        "\033[1;34m[////////] Puxando o freio de mão...\033[m\n",
                        "\n\033[1;37m◇◇◇◇◇◇◇◇◇◇◇◇◇◇◇◇◇◇◇◇◇◇◇◇◇◇◇◇◇◇◇◇◇◇◇◇◇◇◇◇\033[m\n\n"
                        ]
                
        eventos = [
                    "Neste ano foi descoberto vida em outro planeta.",
                    "Neste século uma pesquisa sobre células tronco marcou a história",
                    "Essa década foi marcada por uma terrível doença.",
                    "Neste dia houve uma chuva de meteoros histórica.",
                    "Esse século foi marcado pela descoberta da cura do câncer.",
                    "Hoje é o dia internacional do cachorro quente.",
                    "Neste ano foram criados exoesqueletos funcionais aos humanos.",
                    "Hoje foram descobertos fósseis em marte.",
                    "Esse ano foi marcado por um furacão terrível.",
                    "Nesta década as crises climáticas chegaram ao seu ápice.",
                    "Nesse século foi feito um acordo de paz entre todos os países."
                    ]

        i = (randint(1,11) - 1)

        for t in (carregamento) :
                print(t)
                time.sleep(1)
                    
        print("\033[1;36mBem vindo ao futuro viajante!\033[m\n\nO ano é :")
        print(futuro.strftime("%d/%m/%Y"))

        print(eventos[i])

        iniciar = input("\n\033[1;37mDeseja viajar novamente? [S] ou [N]\033[m\n").lower().strip()[0]
            
    if iniciar == "n" :
        print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\033[1;37m◇◇◇◇◇◇◇◇◇◇◇◇◇◇◇◇◇◇◇◇◇◇◇◇◇◇◇◇◇◇◇◇◇◇◇◇◇◇◇◇\033[m\n\n"
        "\033[1;31mVocê saiu da máquina do tempo e viveu sua vida normalmente.\033[m\n\n")
        break



