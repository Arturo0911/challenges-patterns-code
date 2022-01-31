#!/usr/bin/env python3

"""
github.com/Arturo0911/challenges_patterns_code
:author: Arturo Negreiros (aka H0n3yL04d)
"""

import matplotlib.pyplot as plt
import sys
import random
from random import randint
from pprint import pprint

random.seed(42)


def fx(n: int) -> float:
    # f(x) = x³+2
    return (n**2) + 2


def MC_implementation(size_elements: int):
    """
    For this implementation, we gonna to say the
    ∫( upper_lower a - limit_upper b) f(x) => f(x) = x³+2
    additional parameter m => 30
    """
    
    x_vals = [random.uniform(0, 1) for _ in range(size_elements)]
    # to get g(x), we have to implement the function previously 
    # indicated
    
    gx = [fx(x) for x in x_vals]
    plt.figure(figsize=(12, 12))
    plt.plot(x_vals, gx, label="random numbers")
    # plt.plot(gx, label='g(x) numbers')
    plt.legend()
    plt.show()
    # the approximation 
    approximation = sum(gx)/len(gx)
    return approximation



def main():
    print("""\n\n
    \t\ttry this => python3 AlgorithmSimulation.py 100
    \t\twhere 100 is the size of elements to generate 
    \t\tthe approximation
    """)
    try:
        size = int(sys.argv[1])
        print(MC_implementation(size_elements=size))
    except Exception as e:
        print("""
        I specifically told you use
        python3 AlgorithmSimulation.py <the number of 
        the elements>
        """)
        exit(1)
    except KeyboardInterrupt:
        exit(0)


if __name__ == "__main__":
    main()
