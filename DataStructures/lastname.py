#!/usr/bin/python3

import sys


def main():
    patterns = "*"
    
    limit = int(sys.argv[1])
    for x in range(1, limit):
        if x == 1:
            print(patterns+(' '*limit)+patterns)
        elif x == limit-1 :
            print(patterns+(' '*limit)+patterns)
        else:
            print(patterns+(' '*(x-1)+patterns)+(' '*(limit-x))+patterns)



if __name__ == "__main__":
    main()
