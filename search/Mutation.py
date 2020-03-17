"""
    Created by michal-swiatek on 17.03.2020
    Github: https://github.com/michal-swiatek
"""

import random


class Mutation:
    """
        Representation of mutation

        Mutation is a genetic operator responsible for maintaining genetic
        diversity within population
        By adjusting mutation_chance parameter user can control mutation rate
    """

    def __init__(self, mutation_chance=0.01):
        self.mutation_chance = mutation_chance

    def mutate(self, genotype):
        for gene in genotype:
            if random.uniform(0.0, 1.0) < self.mutation_chance:
                self.mutateGene(gene)

    def mutateGene(self, gene):
        pass

    @property
    def mutation_chance(self):
        return self.__mutation_chance

    @mutation_chance.setter
    def mutation_chance(self, value=0.01):
        if value < 0.0 or value > 1.0:
            raise ValueError("Mutation chance value has to be number from 0.0 to 1.0")

        self.__mutation_chance = value
