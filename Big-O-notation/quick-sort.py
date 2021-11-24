#!/usr/bin/python3



def quick_sort(array: list) -> list:

    if len(array) < 1:
        return []

    # choose pivot
    final_array = list()
    pivot = array[0]
    left = list()
    right = list()

    for x in range(1, len(array)):
        if array[x] < pivot:
            left.append(array[x])
        else:
            right.append(array[x])


    return final_array + quick_sort(left) + [pivot] + quick_sort(right)




def main():
    array_value = [4, 9, 2, 1, 6, 3, 8]
    print(quick_sort(array_value))



if __name__ == "__main__":
    main()
