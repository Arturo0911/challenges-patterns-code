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

    solved = False
    nodes_visited = []
    border_nodes = []
    initial_node = Node(initial_state)
    initial_node.set_cost(0)
    border_nodes.append(initial_node)


    while (not solved) and len(border_nodes) != 0:
        # sorte the list of border nodes
        border_nodes = sorted(border_nodes, key=cmp_to_key(compare))
        node = border_nodes[0]
        # extract node and push it to the visited
        nodes_visited.append(border_nodes.pop(0))
        
        if node.get_data() == solution:
            print(f"node.get_data() {node.get_data()}")
            solved = True
            print(node.get_father())
            return node
        else:
            # auxiliar variable
            node_data = node.get_data()
            child_list = []
            for one_child in connections[node_data]:
                child = Node(one_child)
                cost = connections[node_data][one_child]
                # print(f"the cost {cost}")
                child.set_cost(node.get_cost() + cost)
                child_list.append(child)

                if not child.in_list(nodes_visited):
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

    """
    We want to know, in how to get the optimal path or road from A to Z
    whenever the condition will be the lower as possible.
    """
    initial_state = 'A'
    solution = 'Z'
    solution_node = uniform_cost_search(connections=connections, 
            initial_state = initial_state, 
            solution=solution)
    # print(solution_node)
    result = []
    node = solution_node

    while node.get_father() != None:
        # print("hello")
        # print(node.get_data())
        result.append(node.get_data())
        node = node.get_father()

    result.append(initial_state)
    result.reverse
    print(result)



if __name__ == "__main__":
    main()
