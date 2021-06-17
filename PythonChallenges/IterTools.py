#!/usr/bin/python3


from itertools import product

A = list(map(int, input().split()))
B = list(map(int, input().split()))


for x in list(product(A, B)):
    print(x,"", end="")
print()

