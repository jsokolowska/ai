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

    def mutate(self, genotype: []) -> None:
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
    def mutation_chance(self) -> float:
        return self.__mutation_chance

    @mutation_chance.setter
    def mutation_chance(self, value: float) -> None:
        if value < 0.0 or value > 1.0:
            raise ValueError("Mutation chance value has to be a number from 0.0 to 1.0")

        self.__mutation_chance = float(value)


class FlipBitMutation(Mutation):
    """
        Standard flip bit mutation

        This mutation type can occur more than once within single genotype
        Works only on genotypes that hold type that can be converted to boolean
        Mutation is performed by flipping bit value of particular gene in genome
    """
    def mutateGene(self, gene: bool) -> bool:
        """
            Flips given bit value

        :param gene: gene in form of boolean
        :return: gene as boolean
        """
        return bool(not gene)


class SwapGeneMutation(Mutation):
    """
        Mutation type that swaps two randomly chosen genes

        This mutation type happens at most once within given genotype
        Works on any gene type, only swap operation is performed
    """
    def mutate(self, genotype: []) -> None:
        """
            Performs mutation instead of mutateGene() function

            When mutation occurs, two genes are chosen randomly and their
            position in genotype is swapped

        :param genotype: genotype of given individual
        :return: None
        """
        if 0.0 < random.uniform(0.0, 1.0) <= self.mutation_chance:
            try:
                pos1, pos2 = random.sample(range(len(genotype)), 2)
            except ValueError:
                print("Sample size exceeded genotype length")
                return

            genotype[pos1], genotype[pos2] = genotype[pos2], genotype[pos1]

    def mutateGene(self, gene) -> None:
        """
            Gene mutation is handled in mutate() function therefore this
            function does nothing

        :param gene: any gene type
        :return: None
        """
        pass
