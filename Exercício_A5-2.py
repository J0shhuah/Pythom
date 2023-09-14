"""Exercício 2"""

from random import randint
from colorama import Fore, init

init(autoreset=True)

print(" \n ")
print(Fore.LIGHTCYAN_EX + "· · • Jogo de ímpar ou par • · ·")
print(" ")

# Variáveis importantes aqui:

escolha = (str(input("Escolha entre Ímpar ou Par:\n")))
numero = (int(input("Escolha um número aleatório:\n")))
              
oponente = randint(0, 1000)
calculo = (numero + oponente) % 2

resultadoPar = True
ganhar = False
resultadoFinal = ""

# Isso identifica se o resultado será par ou ímpar.

if calculo == 0:
    resultadoPar = True
    resultadoFinal = "Par"
else:
    resultadoPar = False
    resultadoFinal = "Ímpar"

if escolha == "Par" and resultadoPar == True:
    ganhar = True
elif escolha == "Ímpar" and resultadoPar == False:
    ganhar = True
else:
    ganhar = False


if ganhar == True:
    print(Fore.LIGHTGREEN_EX + " \nParabéns você ganhou!")
else:
    print(Fore.RED + " \nVocê perdeu!")

print(f" \nSeu número {numero} --- Número do oponente {oponente}\n{numero} + {oponente} = {numero+oponente} -- {resultadoFinal}")