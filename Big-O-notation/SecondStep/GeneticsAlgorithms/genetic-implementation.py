#!/usr/bin/python3

from typing import (
    Any,
    List,
    Dict
)
from random import randint


Genome = List[int]
Population = List[Genome]


def create_genom(size: int) -> Genome:
    """
        :size of the initial genom to be created,
        using the randint function to choice form
        0 or 1
    """
    return [randint(0, 1) for _ in range(size)]


def generate_population(size: int, genome_length: in) -> Population:
    return [create_genome(genome_length) for _ in range(size)]



def fitness(genome: Genome, things: [Thing], weight_limit: int) -> int:
    pass


def score():
    pass


def crossover():
    pass






def main():
    print(create_genom())



if __name__ == "__main__":
    main()
