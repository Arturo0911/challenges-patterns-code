#!/usr/bin/python3


class Node:
    def __init__(self, value) -> None:
        self.left = None
        self.right = None
        self.value = value
    
    def print_tree(self):
        print(self.value)
    
    def insert(self, value):
        if self.value:
            pass
        else:
            pass
    



def main():
    node = Node(12)
    node.print_tree()


if __name__ == "__main__":
    main()