#!/usr/bin/python3





def rotateleft(d: int, arr: list) -> list:

    new_pos = dict()
    for pos, val in enumerate(arr):
        if pos < d:
            new_pos[len(arr) - d + pos] = val
        elif pos == len(arr)-1:
            new_pos[len(arr) - d - 1] = val
        else:
            new_pos[pos - d] = val
    for x, y in new_pos.items():
        arr[x] = y

    return arr
# this should be the output [3, 4, 5, 1, 2]

def main():

    rotateleft(2, [1, 2, 3, 4, 5])



if __name__ == "__main__":
    main()
