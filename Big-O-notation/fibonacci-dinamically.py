#!/usr/bin/python3



def fibonacci(n: int, cache: dict) -> int:

    if n in cache:
        return cache[n]

    cache[n] = fibonacci(n-1, cache) + fibonacci(n-2, cache)
    return cache[n]


if __name__ == "__main__":
    print(fibonacci(901, {0:0, 1:1}))


