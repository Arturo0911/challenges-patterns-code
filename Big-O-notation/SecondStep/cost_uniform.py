#!/usr/bin/python3

from Node import Node
from typing import Dict, List, Tuple, Any
from functools import cmp_to_key


def compare(x: Node, y: Node):
    return x.get_cost() - y.get_cost()



def search_uniform(
        connections: Any, 
        initial_state: Any, 
        solution: Any) -> Node:


    solved = False
    border_nodes = list()
    visited_nodes = list()
    initial_node = Node(initial_state)
    initial_node.set_cost(0)
    border_nodes.append(initial_node)

    while (not solved) and len(border_nodes) != 0:

        border_nodes = sorted(border_nodes, key=cmp_to_key(compare))
        node = border_nodes[0]

        visited_nodes.append(border_nodes.pop(0))

        if node.get_data() == solution:
            solved = True
            return node
        else:
            data_node = node.get_data()
            child_list = list()
            for one_child in connections[data_node]:
                child = Node(one_child)
                cost = connections[data_node][one_child]

                child.set_cost(cost + node.get_cost())
                child_list.append(child)

                if not child.in_list(visited_nodes):
                    if child.in_list(border_nodes):
                        for n in border_nodes:
                            if n.is_equal(child) and n.get_cost() > child.get_cost():
                                border_nodes.remove(n)
                                border_nodes.append(child)
                    else:
                        border_nodes.append(child)
                        node.set_childs(child_list)







def main():
    connections ={
        'A':{'B':15, 'C':10, 'D':23},
        'B':{'E':6},
        'C':{'E':6,'F':8},
        'D':{'F':8},
        'E':{'G':12, 'F':8},
        'F':{'C':10, 'D':23, 'H':15,'I':8, 'E':6},
        'G':{'H':15, 'Z':4},
        'H':{'F':8, 'I':8, 'G':12, 'Z':4},
        'I':{'F':8, 'H':15, 'Z':4}
    }

    initial = 'A'
    solution = 'Z'
    result = list()
    node_solution = search_uniform(connections=connections, 
            initial_state=initial, 
            solution=solution
    )
    print(dir(node_solution))
    print(node_solution.get_father())
    # print(search_node.get_father())
    # node = search_node
    # while node.get_father() != None:
    #     result.append(node.get_data())
    #     node = node.get_father()

    # result.append(initial_state)
    # result.reverse
    # print(result)

if __name__ == "__main__":
    main()
