#!/usr/bin/python3

class Array:
    def __init__(self, capacity, fill_value=None) -> None:
        self.items = list()
        for x in range(capacity):
            self.items.append(fill_value)
    
    def __len__(self):
        return len(self.items)
    
    def __str__(self) -> str:
        return str(self.items)

    def __iter__(self):
        return iter(self.items)
    
    def __getitem__(self, index:int):
        return self.items[index]

    def __setitem__(self, index, new_item):
        self.items[index] = new_item
        




def main():
    pass


if __name__ == "__main__":
    main()
