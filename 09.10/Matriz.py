listaNumero = [1,2,3,4,5,6,7,8,9,10]
sublista = []
subListanumero = 3
for i in range (0,len (listaNumero), subListanumero):
    subListaP = listaNumero[i:i + subListanumero]
    sublista.append(subListaP)
print(sublista)
#outra forma
subListaForma = [[]for _ in range(3)]
listA = [1,2]
listB = [3,4,5]
listC = [6,7,8,9]
subListaForma[0].extend(listA)
subListaForma[1].extend(listB)
subListaForma[2].extend(listC)
print(subListaForma)
#liata do Luigi
a = []
a.append(listA)
a.append(listB)
a.append(listC)
print(a)
#outra forma de fazer 
listaOutra = [1,2,3,4,5,6]
sublistaP1 = listaOutra [2:len(listaOutra) - 1]
print(sublistaP1)