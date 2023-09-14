from datetime import date

diaAtual = date.today().day
mesAtual = date.today().month
anoAtual = date.today().year

nome = input('Digite seu nome: ')
diaNascimento = int(input('Dia do Nascimento: '))
mesNascimento = int(input('Mês do Nascimento: '))
anoNascimento = int(input('Ano do Nascimento: '))

ano = anoAtual-anoNascimento 
if(mesNascimento<mesAtual):
    print(f'Sua idade é: {ano} anos')

ano = ano-1
if(mesNascimento>mesAtual):
    print(f'Sua idade é: {ano} anos')
ano = anoAtual-anoNascimento
if(mesNascimento==mesAtual and diaNascimento<diaAtual):
    print(f'Sua idade é: {ano} anos')

ano = anoAtual-anoNascimento 
ano = ano-1
if(mesNascimento==mesAtual and diaNascimento>diaAtual):
    print(f'Sua idade é: {ano} anos')
    
ano = anoAtual-anoNascimento   
if(mesNascimento==mesAtual and diaNascimento==diaAtual):
    print(f'Sua idade é: {ano} anos\n PARABÉNSS 🥳🎈🎉✨')

