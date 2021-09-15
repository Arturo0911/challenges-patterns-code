#!/usr/bin/python3


def list_comprehension_try(word):

    return [char for pos, char in enumerate(word) if char not in word[:pos]]




def merge_the_tools(string, k):
    def split(word):
        elements = list()
        for x in word:
            if x not in elements:
                elements.append(x)
        return elements
    
    splits = int(len(string)/k)
    
    for x in range(k, len(string)+1, k):
        for i in split(string[x-k: x]):
            print(i, end="")
        print()

if __name__ == '__main__':
    
    merge_the_tools("AABCAAADA", 3)