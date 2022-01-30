#!/usr/bin/env python3


from Node import Node
from typing import Any



def compare(x: Node, y: Node) -> bool:
    return x.get_cost() - y.get_cost()


def uniform_cost_search(
        connections: Any, 
        initial_state: Any, 
        solution: Any) -> Node:
    
    solved: bool = False
    nodes_visited = list()
    border_notes = list()

    initial_node = Node(initial_state)
    
    print(initial_node.get_cost())

    initial_node.set_cost(0)

    print(initial_node.get_cost())



def main():
    uniform_cost_search({}, 'A', None)




if __name__ == "__main__":
    main()
