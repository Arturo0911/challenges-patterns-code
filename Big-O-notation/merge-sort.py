#!/usr/bin/python3


def merge_sort(array: list) -> list:

    if len(array) > 1:

        middle = len(array) // 2

        left = array[:middle]
        right = array[middle:]

        merge_sort(left)
        merge_sort(right)

        # making iterables for subists
        i = 0
        j = 0

        # making an iterable for main list
        k = 0

        while i < len(left) and j < len(right):

            if left[i] < right[j]:
                array[k] = left[i]
                i += 1
            else:
                array[k] = right[j]
                j += 1
            k += 1
        while i < len(left):
            array[k] = left[i]
            i += 1
            k += 1
        while j < len(right):
            array[k] = right[j]
            j += 1
            k += 1
        return array

def main():

    array_value = [7, 4, 6, 10, 11, 45, 89, 8, 9, 1, 3, 2, 5]
    print(f"array: {array_value}\n\n")
    print(merge_sort(array_value))



if __name__ == "__main__":
    main()
