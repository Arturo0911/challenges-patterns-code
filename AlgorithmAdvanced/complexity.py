#!/usr/bin/python3

from random import randint
from typing import (
    List,
    Any
)

"""Dynamically"""


def heapify(array: list, n: int, i:int):
    largest = i
    left = 2*i + 1
    right = 2*i + 2

    if left < n and array[largest] < array[left]:
        largest = left

    if right < n and array[largest] < array[right]:
        largest = right
    
    if largest != i:
        array[largest], array[i] = array[i], array[largest]

        heapify(array, n, largest)

def heap_sort(array):
    
    size = len(array)

    for x in range(size//2 -1, -1, -1):
        heapify(array, size, x)

    for x in range(size-1, 0, -1):
        array[x], array[0] = array[0], array[x]
        heapify(array, x, 0)


    return array



def normal_fibonacci(n: int) -> int:
    if n <= 1:
        return n
    
    return normal_fibonacci(n-1) + normal_fibonacci(n-2)


"""Searching Algorithms"""


def binary_search(element: int, array: List[int]) -> Any:
    if element not in array:
        return False

    middle = len(array) // 2

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
            if array[y - 1] > array[y]:
                array[y], array[y - 1] = array[y - 1], array[y]

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

        while j > 0 and array[j - 1] > actual:
            array[j] = array[j - 1]
            j -= 1

        array[j] = actual

    return array


def merge_sort(array: List[int]) -> List[int]:
    """Split and conquist"""

    if len(array) > 1:

        middle = len(array) // 2
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
    # and after that you can iterate throught the variables

    if len(array) < 1:
        return []

    pivot = array[0]
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
    print(f"\n[*] This is the original array {array}\n\n")
    print(f"[*] Implementation of bubble sort {bubble_sort(array)}")
    print(f"[*] Implementation of insert sort {insert_sort(array)}")
    print(f"[*] Implementation of merge sort {merge_sort(array)}")
    print(f"[*] Implementation of quick sort {quick_sort(array)}")
    print(f"[*] Implementation of quick sort {heap_sort(array)}")


if __name__ == "__main__":
    main()
