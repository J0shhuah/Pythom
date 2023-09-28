vetA=(2,5,6,4,2,3)
vetB=(3,4,5,6,8,2)
for valor in range(0,len(vetA)):
    r = vetA[valor]*vetB[valor]
    print(f'{vetA[valor]} * {vetB[valor]} = {r}')

x = int(input('Digite o número: '))
g = [1,3]
g.append(x)
print(g)

g.remove(x)
print(g)

