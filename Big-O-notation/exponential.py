#!/usr/bin/python3


def exponential(exp: int, num: int) -> int:
    if exp == 0:
        return 1
    
    if exp == 1:
        return num

    return num * exponential(exp-1, num)


def main():
    print(exponential(5, 2))



if __name__ == "__main__":
    main()
