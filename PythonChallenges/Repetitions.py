#!/usr/bin/python3

from itertools import permutations

word, steps = input().split()

print(*["".join(i) for i in permutations(sorted(word), int(steps))], sep="\n")
