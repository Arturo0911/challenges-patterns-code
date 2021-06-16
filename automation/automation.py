#!/usr/bin/python3

import sys
import os
from os.path import isdir



def get_money_spent(keyboards:list, drives:list, b:int) -> int:
    
    new_list_back = list()
        
    for i in keyboards:

        new_list_back  += [(i + value) for value in drives if (i +value)<= b]
        
    new_list_back.sort()


    if new_list_back != []:
        return new_list_back[len(new_list_back) - 1]
    else:
        return -1





#if __name__ == '__main__':

print("The first case: ", get_money_spent([4],[5],5 ))
print("The second case", get_money_spent([3,1],[5,2,8],10))

