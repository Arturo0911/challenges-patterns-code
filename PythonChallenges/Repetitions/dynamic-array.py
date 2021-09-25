#!/usr/bin/python

def dynamicArray(n: int, queries: int) -> None:
    matrix = [[] for _ in range(n)]
    last = 0

    for x in queries:
        if int(x[0]) == 1:
            idx = (int(x[1])^last)%n
            matrix[idx].append(int(x[2]))
        elif int(x[0]) == 2:
            idx = (int(x[1])^last)%n            
            last = matrix[idx][x[2]%len(matrix[idx])]
            print(last)


if __name__ == "__main__":
    pass
