from random import randint
from time import sleep
from colorama import Fore, init
import math
from datetime import date
anoAtual = date.today().year
engrenagemLogica = anoAtual + 51
for contador in range(anoAtual, engrenagemLogica):
    print(contador,end=' ')
print(' ')
print(' ')


anoAtual = date.today().year
engrenagemLogica = anoAtual + 11

print('Década 1: ')
for contador in range(anoAtual, engrenagemLogica):
    print(contador,end=' ')
    

anoAtual = 2033
engrenagemLogica = anoAtual + 11
print(' ')
print(' ')
print('Década 2: ')
for contador in range(anoAtual, engrenagemLogica):
    print(contador,end=' ')

anoAtual = 2043
engrenagemLogica = anoAtual + 11
print(' ')
print(' ')
print('Década 3: ')

for contador in range(anoAtual, engrenagemLogica):
    print(contador,end=' ')

anoAtual = 2053
engrenagemLogica = anoAtual + 11
print(' ')
print(' ')
print('Década 4: ')
for contador in range(anoAtual, engrenagemLogica):
    print(contador,end=' ')


anoAtual = 2063
engrenagemLogica = anoAtual + 11
print(' ')
print(' ')
print('Década 5: ')
for contador in range(anoAtual, engrenagemLogica):
    print(contador,end=' ')
print(' ')
print(' ')
computador = randint(1,5)
print(computador)

if computador == 1:
    print('Na 1° Década terá um eclipse lunar que afetará a magia de Hogwarts')
elif computador == 2:
    print('''Na 2° Década Valdemort contruirá um império e destruirá Hogwarts''')
elif computador == 3:
    print('Na 3° Década Harry travará uma grande guerra contra o império ')
elif computador == 4:
    print('Na 4° Década a paz reinará em Hogwarts')
elif computador == 5:
    print('Na 5° Década o mundo acaba')

