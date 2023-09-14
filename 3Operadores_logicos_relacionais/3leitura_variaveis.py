'''Leitura de variáveis o usuário poderá 
digitar valores via teclado. Obs os valores
sempre serão tipo string, é importante sempre 
converter para uma variável númerica caso 
seja necessário fazer algum tipo de operação 
matemática
'''

x = int(input("digite o número 1:"))
y = int(input("digite o número 2:"))
r = x + y 
print(f'O resultado é {r}')