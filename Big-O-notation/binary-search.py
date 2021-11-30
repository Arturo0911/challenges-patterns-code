#!/usr/bin/python3


from typing import Any
from random import randint


def binary_search(element: int, array: list) -> Any:
    
    pivot = len(array)//2

    if array[pivot] == element:
        return True

    if array[pivot] <= element:
        return binary_search(element, array[:pivot])
    else:
        return binary_search(element, array[pivot:])


def main():
    array = sorted([randint(1,15) for _ in range(10)])
    print(binary_search(array[4], array))



if __name__ == "__main__":
    main()
