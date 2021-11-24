#!/usr/bin/python3


def main():


    array: list = [1, 7, 2, 5, 6, 4, 3]

    for x in range(1, len(array)):

        index = x
        actual = array[x]

        while index > 0 and (array[index-1] > actual):
            array[index] = array[index - 1] 
            index -= 1

        array[index] = actual

    print(array)


if __name__ == "__main__":
    main()
