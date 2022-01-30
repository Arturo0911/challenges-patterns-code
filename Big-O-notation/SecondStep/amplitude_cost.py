#!/usr/bin/env python3

from functools import cmp_to_key
from Node import Node
from typing import Any
from pprint import pprint


def compare(x: Node, y: Node) -> bool:
    return x.get_cost() - y.get_cost()


def uniform_cost_search(
        connections: Any, 
        initial_state: Any, 
        solution: Any) -> Node:

    solved: bool = False
    nodes_visited = list()
    border_nodes = list()

    initial_node = Node(initial_state)

    initial_node.set_cost(0)

    border_nodes.append(initial_node)

    pprint(connections)
    while (not solved) and len(border_nodes) != 0:
        # sorte the list of border nodes
        border_nodes = sorted(border_nodes, key=cmp_to_key(compare))

        node = border_nodes[0]

        # extract node and push it to the visited
        nodes_visited.append(border_nodes.pop(0))
        
        if node.get_data() == solution:
            solved = True
            return node
        else:
            # auxiliar variable
            node_data = node.get_data()

            # creating a new child list
            child_list = list()
            print(node_data) 
            for one_child in connections[node_data]:
                child = Node(one_child)
                cost = connections[node_data][one_child]
                
                child.set_cost(node.get_cost() + cost)
                child_list.append(child)

        break




def main():
    connections = {
        'A': {'B': 15, 'C': 10, 'D': 23},
        'B': {'E': 6},
        'C': {'E': 6, 'F': 8},
        'D': {'F': 8},
        'E': {'B': 15, 'C': 10, 'F': 8, 'G': 12},
        'F': {'C': 10, 'D': 23, 'E': 6, 'H': 15, 'I': 8},
        'G': {'E': 6, 'H': 15, 'Z': 4},
        'H': {'F': 8, 'I': 8, 'G': 12, 'Z': 4},
        'I': {'F': 8, 'H': 15, 'Z': 4}
    }

    """
    We want to know, in how to get the optimal path or road from A to Z
    whenever the condition will be the lower as possible.
    """
    solution = 'Z'
    uniform_cost_search(connections, 'A', solution)




if __name__ == "__main__":
    main()
