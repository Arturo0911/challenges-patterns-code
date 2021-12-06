


def insertion(array):
    print(array)
    for x in range(1, len(array)):

        print(f"Iterator for {x}")
        actual = array[x]
        j = x

        while j > 0 and array[j-1] > actual:

            print(f"While iterator {j} {x}")

            j -= 1




if __name__ == "__main__":

    array = [5, 11, 14, 2, 34, 6, 7, 8, 1, 9]
    insertion(array)
