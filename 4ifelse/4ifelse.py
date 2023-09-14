moeda = True
ponto = 0
nome = str(input('Nome do personagem: '))
if(nome == 'Mário' and moeda == True)or(nome == 'mario' and moeda == True):
    ponto = ponto + 1 
    print(f'{nome} pegou a moeda e teve {ponto}')
    moeda = str (input("Deseja pegar mais uma moeda?\n"))
    if(moeda == 'Sim'):
        ponto = ponto + 1
        print(f'{nome} pegou a moeda e teve {ponto}')
    else:
        print(f'Não quis pegar mais moedas')
else:
    print('Não pegou a moeda')