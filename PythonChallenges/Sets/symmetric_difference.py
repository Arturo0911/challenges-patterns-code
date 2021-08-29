#!/usr/bin/env python


def symmetric_difference(m: list, n: list):
    stack = list()

    for x, y in zip(m, n):
        if (x not in n) and (y not in m):
            stack.append(x)
            stack.append(y)
    stack.sort()
    for x in stack:
        print(X)

if __name__ == "__main__":
    m_size = int(input())
    m_array = list(map(int, input().split()))

    n_size = int(input())
    n_array = list(map(int, input().split()))

    symmetric_difference(m_array, n_array)
