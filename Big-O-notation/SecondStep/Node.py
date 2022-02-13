#!/usr/bin/python3


from typing import (
    Any,
    List
)


class Node:

    def __init__(self, data: Any, childs: Any=None) -> None:
        self.data = data
        self.childs = None
        self.father = None
        self.cost = None
        self.set_childs(childs)

    def get_data(self):
        return self.data

    def set_data(self, data):
        self.data = data

    def get_cost(self):
        return self.cost

    def set_cost(self, cost):
        self.cost = cost

    def get_father(self):
        return self.father

    def set_father(self, father):
        self.father = father

    def get_childs(self):
        return self.childs

    def set_childs(self, childs):
        self.childs = childs

        if self.childs != None:
            for h in self.childs:
                h.father = self
    
    def is_equal(self, node) -> bool:
        if self.get_data() == node.get_data():
            return True
        else:
            return False

    def in_list(self, list_nodes) -> bool:
        in_the_list = False
        
        for x in list_nodes:
            if self.is_equal(x):
                in_the_list = True
        return in_the_list



