import math
a = int(input('Digite o valor de A:'))
b = int(input('Digite o valor de B:'))
c = int(input('Digite o valor de C:'))

delta = b*b - 4*a*c

x1 = (-b+math.sqrt(delta)) / (2*a)
x2 = (-b-math.sqrt(delta)) / (2*a)
print('Temos com solução duas raízes reais e diferentes')
print('x1 = ' , x1)
print('x2 = ' , x2)