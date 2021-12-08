#!/usr/bin/python3


from random import randint

# bubble sort
# el más fácil
def bubble_sort(lista):
    for i in range(1, len(lista)):
        for j in range(1, len(lista)):
            # condición
            if lista[j-1] > lista[j]:
                lista[j], lista[j-1] = lista[j-1], lista[j]
                # si la lista original era así [7, 6]
                # lista me quede así [6,7]
    return lista


def merge_sort(lista):

    if len(lista) > 1:
    
        middle = len(lista)//2
        left = lista[:middle]
        right = lista[middle:]

        merge_sort(left)
        merge_sort(right)

        # iteradores
        i = 0
        j = 0
        k = 0

        while i < len(left) and j < len(right):

            if left[i] < right[j]:
                lista[k]  = left[i]
                i += 1
            else:
                lista[k] = right[j]
                j += 1
            
            k += 1
        
        while i < len(left):
            lista[k] = left[i]
            i += 1
            k += 1

        while j < len(right):
            lista[k] = right[j]
            j += 1
            k += 1
        
    return lista



def quick_sort():
    pass

def insert_sort(lista): # es exponencial O(n)²
    if len(lista) > 1:
        for i in range(1, len(lista)):
            actual  = lista[i]
            index = i
            while (index > 0) and (lista[index-1] > actual):
                lista[index] = lista[index-1]
                index = index - 1
            lista[index] = actual

            """
            lista que vamos a ordenar:
            [12, 15, 7, 8, 26, 21,13, 4, 6, 91, 1]

            recorrer desde el elemento 1 hasta el número 10 => 1 2 3 4 5 6 7 8 9
            
                - cuando i vale 1 entonces:

                    actual = lista[1] => 15
                    indice = i => 1

                    while 1 > 0 and 12 > 15:
                        no va a ocurrir
                
                - cuando i vale 2 entonces:

                    actual = lista[2] => 7
                    indice = i => 2

                    while 2 > 0 and 15 > 7:

                        lista[indice] = lista[indice - 1] se realiza esto y la lista
                         
                            [12, 15, 7, 8, 26, 21,13, 4, 6, 91, 1] original

                            [12, 15, 15, 8, 26, 21,13, 4, 6, 91, 1] cambiado
                        

            """
    return lista

def heap_sort():
    pass


def main():

    # lista aleatoria xD
    array = [12, 15, 7, 8, 26, 21,13, 4, 6, 91, 1]
    print(array)
    # print(bubble_sort(array))
    # print(insert_sort(array))
    print(merge_sort(array))
    """
    Mediante el ordenamiento de burbuja, ordenar el siguiente conjunto de elementos
    """


if __name__ == "__main__":
    main()