#!/usr/bin/python3

from random import randint
from typing import (
    List,
    Any
)


"""Searching Algorithms"""
def binary_search(element: int, array: List[int]) -> Any:

    if element not in array:
        return False

    middle = len(array)//2

    if array[middle] == element:
        return True

    if array[middle] < element:
        return binary_search(element, array[middle:])
    else:
        return binary_search(element, array[:middle])


"""Sorting Algorithms"""
def bubble_sort(array: List[int]) -> List[int]:
    for x in range(1, len(array)):
        for y in range(1, len(array)):
            if array[y-1] > array[y]:
                array[y], array[y-1] = array[y-1], array[y]

            """
            # if you want to implement the sorting in reverse
            # umcomment this part and try to do it!! :)
            if array[y-1] < array[y]:
                array[y], array[y-1] = array[y-1], array[y]"""

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



def main():
    array = [5, 11, 14, 2, 34, 6, 7, 8, 1, 9]
    print(array)
    print(f"[*] Implementation of bubble sort {bubble_sort(array)}")
    print(f"[*] Implementation of insert sort {insert_sort(array)}")
    


if __name__ == "__main__":
    main()
