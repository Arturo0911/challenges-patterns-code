lista=[8,12,3,11,5,9,10,4,1,5]
print(lista)

def particion(lista):
	pivote=lista[0]
	mayores=[]
	menores=[]
	for i in range(1,len(lista)):
		if (lista[i]<pivote):
			menores.Append(lista[i])
		else:
			mayores.Append(lista[i])
			return (menores,pivote,mayores)

def quicksort(lista):
	if lent(lista)<2:
		return lista
	else:
		menores,pivote,mayores=particion(lista)
		return quicksort(menores), pivote, quicksort(mayores)