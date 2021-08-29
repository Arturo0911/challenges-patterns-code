#!/bin/python3
from pprint import pprint

all_squares = [
    [[8, 1, 6], [3, 5, 7], [4, 9, 2]],
    [[6, 1, 8], [7, 5, 3], [2, 9, 4]],
    [[4, 9, 2], [3, 5, 7], [8, 1, 6]],
    [[2, 9, 4], [7, 5, 3], [6, 1, 8]],
    [[8, 3, 4], [1, 5, 9], [6, 7, 2]],
    [[4, 3, 8], [9, 5, 1], [2, 7, 6]],
    [[6, 7, 2], [1, 5, 9], [8, 3, 4]],
    [[2, 7, 6], [9, 5, 1], [4, 3, 8]],
]


def magic_square(square: list) -> int:
    global all_squares
    all_min_values = list()

    for i in all_squares:
        value = 0
        for x, y in zip(i,square):
            for r, c in zip(x,y):
                if r != c:
                    value += max([r, c]) - min([r, c])
        all_min_values.append(value)
    return min(all_min_values)


if __name__ == '__main__':
    pass
    # make_magic_squared()
    # print(magic_square([[4, 9, 2], [3, 5, 7], [8, 1, 5]]))
    # print(magic_square([[4, 8, 2], [4, 5, 7], [6, 1, 6]]))
    # print(square_magic.solve_magic_square([[4, 8, 2], [4, 5, 7], [6, 1, 6]]))
