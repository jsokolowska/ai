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
        """
            Performs mutation on given genotype

            This function randomly picks genes that are a subject of mutation
            Override to change mutation strategy (when mutation occurs)

        :param genotype: genotype of an individual to mutate
        :return: None
        """
        # Performing mutation inplace
        for i, gene in enumerate(genotype):
            if 0.0 < random.uniform(0.0, 1.0) <= self.mutation_chance:
                genotype[i] = self.mutateGene(gene)

    def mutateGene(self, gene):
        """
            Defines gene mutation strategy

            This function is called every time a gene has been chosen to mutate
            To change gene mutation behaviour override this function

        :param gene: individual gene to mutate
        :return: modified gene
        """
        return gene

    @property
    def mutation_chance(self):
        return self.__mutation_chance

    @mutation_chance.setter
    def mutation_chance(self, value=0.01):
        if value < 0.0 or value > 1.0:
            raise ValueError("Mutation chance value has to be a number from 0.0 to 1.0")

        self.__mutation_chance = value
