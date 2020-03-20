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
        Useful for genotypes that represent permutations
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
                raise ValueError("Sample size exceeded genotype length")
            else:
                genotype[pos1], genotype[pos2] = genotype[pos2], genotype[pos1]


class ScrambleGenesMutation(Mutation):
    """
        Mutation type that scramble genes within randomly chosen range

        This mutation type happens at most once within given genotype
        Works on any gene type, genes can only change position
        Useful for genotypes that represent permutations
    """
    def mutate(self, genotype: []) -> None:
        """
            Performs mutation instead of mutateGene() function

            When mutation occurs, a position and scramble range are
            randomly chosen, then genes within that range are shuffled

        :param genotype: genotype of given individual
        :return: None
        """
        if len(genotype) < 2:
            raise ValueError("Attempt to scramble genotype of length smaller than 2")

        if 0.0 < random.uniform(0.0, 1.0) <= self.mutation_chance:
            scramble_range = random.randint(2, len(genotype))   # Scramble at least 2 genes to be effective
            position = random.randint(0, len(genotype) - scramble_range)    # Prevents from going out of range

            # Fisher-Yates shuffle algorithm
            for i in range(position + scramble_range - 1, position, -1):
                j = random.randint(position, i)

                genotype[i], genotype[j] = genotype[j], genotype[i]


class InverseGenesMutation(Mutation):
    """
        Mutation type that inverses genes position within randomly chosen range

        This mutation type happens at most once within given genotype
        Works on any gene type, genes can only change position
        Useful for genotypes that represent permutations
    """
    def mutate(self, genotype: []) -> None:
        """
            Performs mutation instead of mutateGene() function

            When mutation occurs, a position and inverse range are randomly
            chosen, then positions of genes within that range are inverted

        :param genotype: genotype of given individual
        :return: None
        """
        if len(genotype) < 2:
            raise ValueError("Attempt to inverse genotype of length smaller than 2")

        if 0.0 < random.uniform(0.0, 1.0) <= self.mutation_chance:
            inversion_range = random.randint(2, len(genotype))   # Inverse at least 2 genes to be effective
            position = random.randint(0, len(genotype) - inversion_range)    # Prevents from going out of range

            for i in range(0, int(inversion_range / 2)):
                # Shift everything by position
                index1 = i + position
                index2 = inversion_range - 1 - i + position

                genotype[index1], genotype[index2] = genotype[index2], genotype[index1]
