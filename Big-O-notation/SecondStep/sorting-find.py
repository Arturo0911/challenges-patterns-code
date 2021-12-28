#!/usr/bin/python3

from typing import (
    List,
    Any
)

def sorting(array: List[int], solution: List[int]) -> List[int]:
    

    if array != solution:
        central = array
        left = array
        right = array

        middle = len(array)//2
        index = 0
        final = len(array)-1
        
        
        central[middle], central[middle-1] = central[middle-1], central[middle]
        left[index], left[index+1] = left[index+1], left[index]
        right[final-1], right[final] = right[final], right[final-1]
        
        if central != solution:
            return sorting(central, solution)
            
        """if left == solution:
            return solution
        else:
            return sorting(left, solution)

        if right == solution:
            return solution
        else:
            return sorting(right, solution)"""
    return solution



def main():
    
    print(sorting([3,4, 1, 2], [4,3,2,1]))


if __name__ == "__main__":
    main()
