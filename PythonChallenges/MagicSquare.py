#!/bin/python3

#
# Complete the 'formingMagicSquare' function below.
#
# The function is expected to return an INTEGER.
# The function accepts 2D_INTEGER_ARRAY s as parameter.
#
from statistics import mode
from typing import Any
from pprint import pprint


class MagicSquare:

    def _magic_constant(self, square: list, option=True) -> Any:
        if option:
            area = list()
            for i in range(0, 3):
                sum_horizontal = 0
                sum_vert = 0
                for j in range(0, 3):
                    sum_horizontal += square[i][j]
                    sum_vert += square[j][i]
                area.append(sum_horizontal)
                area.append(sum_vert)
            area.append((square[0][0] + square[1][1] + square[2][2]))
            area.append((square[0][2] + square[1][1] + square[2][0]))
            return mode(sorted(area))
        else:
            less_cost = list()
            number = self._magic_constant(square, True)
            for i in range(0, 3):
                sum_horizontal = 0
                sum_vert = 0
                for j in range(0, 3):
                    sum_horizontal += square[i][j]
                    sum_vert += square[j][i]

                    if j == 2:
                        print(square[i][j - 2], square[i][j - 1], square[i][j])
                        if number != sum_horizontal:
                            # print(sum_horizontal)
                            less_cost.append(abs(number - sum_horizontal))

                        if number != sum_vert:
                            # print(sum_vert)
                            less_cost.append(abs(number - sum_vert))

            return sum(less_cost)

    def solve_magic_square(self, square: list) -> int:
        pprint(square)
        return self._magic_constant(square, False)


if __name__ == '__main__':
    square_magic = MagicSquare()
    print(square_magic.solve_magic_square([[4, 9, 2], [3, 5, 7], [8, 1, 5]]))
    # print(square_magic.solve_magic_square([[4, 8, 2], [4, 5, 7], [6, 1, 6]]))
