#!/usr/bin/python3



def recursive(n: int, base: int) -> int:

    if n == 0:
        return 1 * (base ** 5)
    else:
        return 2 * recursive(n-1, base)




def main():
    n = 5
    base = n
    print(recursive(n, base))



if __name__ == "__main__":
    main()
