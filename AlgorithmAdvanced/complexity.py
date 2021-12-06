#!/usr/bin/python3

from random import randint
from typing import List


def bubble_sort(array: List[int]) -> List[int]:
    for x in range(1, len(array)):
        for y in range(1, len(array)):
            if array[y] < array[y-1]:
                array[y], array[y-1] = array[y-1], array[y]
    return array


def main():
    array = [5, 11, 14, 2, 34, 6, 7, 8, 1, 9]
    print(bubble_sort(array))


if __name__ == "__main__":
    main()
