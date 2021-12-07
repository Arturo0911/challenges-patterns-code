#!/usr/bin/python3


def recursive(n: int, base: int) -> int:
    r"""The goal of this object is return
    :: (2 ** n . n ** 5) """

    if n == 0:
        return 1 * (base**5)

    return 2 ** recursive(n-1, base)




def main():
    n = 5
    base = n
    print(recursive(5, base))



if __name__ == "__main__":
    main()
