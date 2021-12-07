#!/usr/bin/python3


from random import randint
from typing import List, Any


def quick_sort(array: List[int]) -> List[int]:
    """The goal of this kinna algorithm is
    make others list that containts the values in separates 
    values, it's simmilar to split and conquer"""

    return array




def insert_sort(array: List[int]) -> List[int]:

    for x in range(1, len(array)):
        actual = array[x]
        j = x
        while j > 0 and array[j-1] > actual:

            array[j] = array[j-1]
            j -= 1
        
        array[j] = actual
    return array


def merge_sort(array: List[int]) -> List[int]:

    if len(array) > 1:
        
        middle = len(array)//2
        left = array[:middle]
        right = array[middle:]

        merge_sort(left)
        merge_sort(right)

        i, j, k = 0, 0, 0

        while i < len(left) and j < len(right):

            if left[i] < right[j]:
                array[k] = left[i]
                i += 1
            else:
                array[k] = right[j]
                j += 1
            
            k += 1
        
        while i < len(left):
            array[k] = left[i]
            i += 1
            k += 1
        
        while j < len(right):
            array[k] = right[j]
            j += 1
            k += 1

    return array

def bubble_sort(array: List[int]) -> List[int]:

    for n in range(1, len(array)):
        for m in range(1, len(array)):
            if array[m-1] > array[m]:
                array[m-1], array[m] = array[m], array[m-1]

    return array

def main():
    array  = [5, 3, 77, 81, 23, 32, 2, 1, 8, 9]
    new_list = [randint(1, 56) for _ in range(15)]

    print(f"the array is {new_list}")
    print(f"Insert sort => {insert_sort((new_list))}")
    print(f"Merge sort => {merge_sort((new_list))}")
    print(f"bubble sort => {bubble_sort((new_list))}")

if __name__ == "__main__":
    main()