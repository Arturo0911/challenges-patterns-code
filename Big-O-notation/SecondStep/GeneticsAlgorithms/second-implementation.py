#!/usr/bin/python3

"""
The main goal of the impelementation of the genetic-algorithm
it's try to make the search of the best solution

The process begin with a set of individuals wich is called population.
Each individual is a solution to the problem you want to solve.
Individuals => is characterized by a set of  a paramaters(variables)
Known as Genes. Genes are joined into a string to form Chromosome (solution)

"""

import time
import os
from random import randint
from multiprocessing import Process


def make_genome():

    genome = list()

    while len(genome) <= 200:

        new_genome = [randint(0, 1) for _ in range(6)]

        if new_genome not in genome:
            genome.append(new_genome)
        else:
            continue
    print(genome)


def main():
    make_genome()



if __name__ == "__main__":
    main()
