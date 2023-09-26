'''
Produção de poções mágicas

Autors: Guilherme de Moura, Joshua Rodrigues, João Pedro Neves
Version 1.3
'''

from random import randint
import time

# Strings do inventário :

ingredientes = [
    '[1] Losna.', 
    '[2] Raízes de valeriana.', 
    '[3] Raiz de asfódelo em pó.', 
    '[4] Vagem sudorífera.', 
    '[5] Ovos congelados de Cinzácaro', 
    '[6] Torta de melaço.', 
    '[7] Pergaminho novo.', 
    '[8] Grama recém cortada.', 
    '[9] Fios de barba de duende irlandês.', 
    '[10] Trevos de 4 folhas.',
    '[11] Pó de chifre de unicórnio.',
    '[12] Raiz de mandrágora.'
]

quant_ingredientes = [
    randint(1, 4),
    randint(1, 4),
    randint(1, 4),
    randint(1, 4),
    randint(1, 4),
    randint(1, 4),
    randint(1, 4),
    randint(1, 4),    
    randint(1, 4),
    randint(1, 4),
    randint(1, 4),
    randint(1, 4)
]

# Variáveis : 

bancada = []
segurando = ""
sair = ""


while True :


    # Interface :

    print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n"
        "\033[0;35m• • • • • • ~ ʚĭɞ ~ • • • • • •\033[m\n\n"
        "       Sua mochila contém :\n")


    for p, ing in enumerate(ingredientes):
        print(f"{ing} - {quant_ingredientes[p]}")

    print("\n \033[0;35m• • • • • • • • • • • • • • • •\033[m\n")


    # Verificando se o valor é válido e adicionando a sua bancada :

    segurando = int(input("Qual ingrediente deseja pegar?\n"))

    if  segurando > 0 and segurando < 13 :

        # Fazendo o controle da quantidade de itens :

        (quant_ingredientes[segurando - 1]) -= 1

        while (quant_ingredientes[segurando - 1]) < 0 :

                print("\n\n\033[0;31mVocê já usou todos os ingredientes!\033[m")
                segurando = int(input("\nQual ingrediente deseja pegar?\n"))
                continue
            

        else :

            bancada.append(segurando)

        if len(bancada) == 4 :
                print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\033[0;35m• • • • • • • • • • • • • • • •\033[m\n\nVocê pegou os seguintes ingredientes : \n")

                for p, ing in enumerate(bancada): 
                    print(ingredientes[ing - 1])

            # Loop para continuar com a poção ou reseta-la :

                while sair != "S" or sair  != "N":
                    sair = input("\n\n\033[0;32mDeseja fazer a poção agora? [S] ou [N]\033[m\n").lower().strip()[0]
                    
                    pocao = False

                # Confirmando as receitas das poções :

                    morto_vivo = [1, 2, 3, 4]
                    amortentia = [5, 6, 7, 8]
                    felix_felicis = [9, 10, 11, 12]

                    if sorted(morto_vivo) == sorted(bancada) :
                        nome_poc = "Morto-Vivo"
                        pocao = True
                    elif sorted(amortentia) == sorted(bancada) :
                        nome_poc = "Amortentia"
                        pocao = True
                    elif sorted(felix_felicis) == sorted(bancada) :
                        nome_poc = "Felix Felicis"
                        pocao = True
                    else :
                        pocao = False
                        
                        
                    if sair == "s" and pocao == True:
                        break

                    elif sair == "s" and pocao == False:
                            
                            carregamento = [
                                            "\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n"
                                            "◇◇◇◇◇◇◇◇◇◇◇◇◇◇◇◇◇◇◇◇◇◇◇◇◇◇◇◇◇◇◇◇◇◇◇◇\n\n"
                                            "\033[1;31m[🔥] Acendendo o fogo...\033[m\n",
                                            "\033[1;33m[🔪] Triturando os ingredientes...\033[m\n",
                                            "\033[1;36m[💦] Enchendo o caldeirão ...\033[m\n",
                                            "\033[1;32m[🥀]Adicionando os ingredientes ...\033[m\n",
                                            "\033[1;30m[⏱️ ] Mexendo o caldeirão ...\033[m\n",
                                            ". . .\n",
                                            ". . .\n",
                                            "💥💥\n\n"
                                            "\033[1;31mVocê adicionou os ingredientes errados e seu laboratório explodiu!\033[m\n\n"
                                              ]
                            
                            for t in (carregamento) :
                                print(t)
                                time.sleep(1)

                            break

                    elif sair == "n" :
                        bancada.clear()
                        break

        if sair == "s" and pocao == True:
            
        
            # Eficácia e produção das poções :

            efic_pocao = randint(1,10)
            efic = ""

            if efic_pocao == 1 :
                 efic = "\033[1;31m[1] Sua poção está terrível, uma bolha do caldeirão estourou no seu rosto e queimou parte dele.\033[m"
            elif efic_pocao == 2 :
                 efic = "\033[1;31m[2] Sua poção está horrorosa, ela explodiu todos os frascos em que estava.\033[m"
            elif efic_pocao == 3 :
                 efic = "\033[1;33m[3] Sua poção está horrível, ficou tão viscosa que você foi incapaz de tira-lá do frasco depois de fria.\033[m"
            elif efic_pocao == 4 :
                 efic = "\033[1;33m[4] Sua poção está péssima, o cheiro dela te fez sair às pressas do laboratório.\033[m"
            elif efic_pocao == 5 :
                 efic = "\033[1;34m[5] Sua poção está quase aceitável, ela funcionou, porém, causou urticárias por toda sua pele.\033[m"
            elif efic_pocao == 6 : 
                 efic = "\033[1;34m[6] Sua poção está aceitável, digna de um iniciante.\033[m"
            elif efic_pocao == 7 :
                 efic = "\033[1;30m[7] Sua poção está ótima! Feita com a maestria necessária.\033[m"
            elif efic_pocao == 8 :
                 efic == "\033[1;30m[8] Sua poção está mais que ótima! Você foi elogiado por toda sua turma.\033[m"
            elif efic_pocao == 9 :
                 efic = "\033[1;32m[9] Sua poção está acima da média! Cumpre exatamente com o necessário.\033[m"
            elif efic_pocao == 10 :
                 efic = "\033[1;32m[10] Sua poção está perfeita! Digna de um mestre.\033[m"
            

            carregamento = [ 
                            "\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n",
                            "◇◇◇◇◇◇◇◇◇◇◇◇◇◇◇◇◇◇◇◇◇◇◇◇◇◇◇◇◇◇◇◇◇◇◇◇\n\n",
                            "\033[1;31m[🔥] Acendendo o fogo...\033[m\n",
                            "\033[1;33m[🔪] Triturando os ingredientes...\033[m\n",
                            "\033[1;36m[💦] Enchendo o caldeirão...\033[m\n",
                            "\033[1;32m[🥀]Adicionando os ingredientes...\033[m\n\n"
                            "\033[1;30m[⏱️ ] Mexendo o caldeirão...\033[m\n",
                            "\033[1;34m[🧽] Limpando os frascos...\033[m\n",
                            "\033[1;35m[🕯️ ] Enchendo os frascos...\033[m\n",  
                            "\033[1;37m[✨] Lacrando as poções...\033[m\n\n",
                            "◇◇◇◇◇◇◇◇◇◇◇◇◇◇◇◇◇◇◇◇◇◇◇◇◇◇◇◇◇◇◇◇◇◇◇◇\n\n\n\n"
                            ]
            
            for t in (carregamento) :
                print(t)
                time.sleep(1)


            if efic_pocao > 4 :
                print(f"\033[1;32mParabéns!! Você criou a poção\033[m \033[1;37m{nome_poc}\033[m\n\n{efic}\n\n\n")
            
            if efic_pocao < 5 :
                print(f"{efic}\n\n\n")
            
    if sair == "s" :
        break

    else:
        continue

