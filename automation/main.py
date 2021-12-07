

from typing import List, Any



def insert_sort(array: List[int]) -> List[int]:

    for x in range(1, len(array)):
        actual = array[x]
        j = x
        while j > 0 and array[j-1] > actual:

            array[j] = array[j-1]
            j -= 1
        
        array[j] = actual
    return array




def main():
    array  = [5, 3, 77, 81, 23, 32, 2, 1, 8, 9]

    print(f"the array is {array}")
    print(f"Insert sort => {insert_sort((array))}")

if __name__ == "__main__":
    main()