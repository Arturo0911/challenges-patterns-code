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




def merge_sort(array: List[int]) -> List[int]:
    """Split and conquist"""

    if len(array) > 1:
        
        middle = len(array)//2
        left = array[:middle]
        right = array[middle:]

        # recursive calling
        merge_sort(left)
        merge_sort(right)

        # iterators
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
            k += 1
            i += 1
            
        while j < len(right):
            
            array[k] = right[j]
            k += 1
            j += 1

    return array


def quick_sort(array: List[int]) -> List[int]:

    # in this kind of algorithn you have to choose a pivot

    if len(array) < 1:
        return []

    pivot = array[2]
    left = list()
    right = list()

    for x in range(1, len(array)):

        if array[x] < pivot:
            left.append(array[x])
        else:
            right.append(array[x])
    
    return quick_sort(left) + [pivot] + quick_sort(right)


def main():
    array = [5, 11, 14, 2, 34, 6, 7, 8, 1, 9, 43, 31, 16]
    print(array)
    print(f"[*] Implementation of bubble sort {bubble_sort(array)}")
    print(f"[*] Implementation of insert sort {insert_sort(array)}")
    print(f"[*] Implementation of merge sort {merge_sort(array)}")
    print(f"[*] Implementation of quick sort {quick_sort(array)}")   


if __name__ == "__main__":
    main()
