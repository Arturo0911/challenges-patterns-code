#!/usr/bin/env python3

"""
github.com/Arturo0911/challenges_patterns_code
:author: Arturo Negreiros (aka H0n3yL04d)
"""

from typing import (
    List,
    Tuple,
)
import matplotlib.pyplot as plt
import sys
import random
from random import randint
from pprint import pprint
import numpy as np


random.seed(42)


def fx(n: float) -> float:
    """f(x) = x²+2"""
    return (n**2) + 2


def montecarlos_implementation(size: int, limit_upper: int, limit_lower: int) -> Tuple[float, List[float], List[float]]:
    r"""
    >>>∫( upper_lower a - limit_upper b) f(x) => f(x) = x²+2
    >>>The form is => (b-a)*Σ f((b-1)*z - a) / n

    :param: limit_upper: b
    :param: limit_lower: a
    :param: n: size of the elements 
    :param: z: it's each random number generated for the simulation 
    """
    z_random = [random.uniform(0, 1) for _ in range(size)]
    possibles_numbers = [fx((limit_upper - limit_lower)*z + limit_lower) for z in z_random]
    summatory = (limit_upper - limit_lower)*(sum(possibles_numbers))/size
    return summatory, possibles_numbers, z_random


def pi_number(n: int) -> float:
    x, y = np.random.uniform(-1, 1, size=(2, n))
    inside = (x**2 + y**2) <= 1
    plt.figure(figsize=(12, 12))
    plt.plot(x[inside], y[inside], 'b.')
    # plt.plot(x[exterior], y[exterior], 'r.')
    plt.show()

def MC_implementation(size_elements: int):
    """
    For this implementation, we gonna to say the
    ∫( upper_lower a - limit_upper b) f(x) => f(x) = x³+2
    additional parameter m => 30


    It's not too much to say, that this implementation 
    is whenever the limit upper and lower, their difference
    it's by one (b-a) = 1
    """

    x_vals = [random.uniform(0, 1) for _ in range(size_elements)]
    # to get g(x), we have to implement the function previously 
    # indicated
    
    # gx = [fx(x) for x in x_vals]
    # plt.figure(figsize=(12, 12))
    # plt.plot(x_vals, gx, label="random numbers")
    # plt.plot(gx, label='g(x) numbers')
    # plt.legend()
    # plt.show()
    # the approximation 
    # approximation = sum(gx)/len(gx)
    return approximation



def main():
    print("""\n\n
    \t\t This is the way to execute this code: python AlgorithmSimulation.py 100
    \t\t where 100 is the size of elements to generate the approximation
    \t\t could be 100 1000 or maybe 10000, well, if your pc support this biggest numbers
    \t\t then try with 10000000 :)
    """)
    try:
        # size = int(sys.argv[1])
        # summatory, possibles_numbers, z_random = montecarlos_implementation(size=size, limit_upper=3, limit_lower=1)
        # plt.figure(figsize=(12, 12))
        # plt.plot(z_random, possibles_numbers, label="random numbers")
        # plt.legend()
        # plt.show()
        pi_number(10000)

    except Exception as e:
        print("""
        I specifically told you use
        python3 AlgorithmSimulation.py <the number of 
        the elements>
        """)
        print(str(e))
        exit(1)
    except KeyboardInterrupt:
        exit(0)



if __name__ == "__main__":
    main()
