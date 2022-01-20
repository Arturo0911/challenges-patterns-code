#!/usr/bin/python3

from typing import (
    Any,
    List,
    Dict
)
from random import (
    randint,
    choices
)


Genome = List[int]
Population = List[Genome]
Thing = namedTuple("Thing", ["name", "value", "weight"])


things = [
    Thing('Laptop', 500, 2200),
    Thing('HeadPhones', 150, 160),
    Thing('Coffe Mug', 60, 350),
    Thing('Notepad', 40, 333),
    Thing('Water Bottle', 30, 192)
]






def create_genom(size: int) -> Genome:
    """
        :size of the initial genom to be created,
        using the randint function to choice form
        0 or 1
    """
    return [randint(0, 1) for _ in range(size)]


def generate_population(size: int, genome_length: int) -> Population:
    return [create_genome(genome_length) for _ in range(size)]



def fitness(genome: Genome, things: [Thing], weight_limit: int) -> int:

    if len(genome) != len(things):
        raise ValueError("genome and things should be of the same size")

    value = 0
    weight = 0

    for i, thing in enumerate(things):
        if genomer[i] == 1:
            weight += thing.weight
            value += thing.value

            if weight > weight_limit:
                return 0

    return value


def selection_pair(population: Population, fitness_func: FitnessFunc) -> Population:
    return choices(
        population=population,
        weights=[fitness_func(genome] for genome in population],
        k=2
    )


def score():
    pass


def crossover():
    pass



def main():
    print(create_genom(25))



if __name__ == "__main__":
    main()
