#!/usr/bin/python3
from typing import Dict

def fibonacci(n: int, cache: Dict[int, int]) -> int:

    if n in cache:
        return cache[n]

    cache[n] = fibonacci(n-1, cache) + fibonacci(n-2, cache)
    return cache[n]


if __name__ == "__main__":
    print(fibonacci(901, {0:0, 1:1}))


