import random


class Mutation:
    """
        Representation of mutation
    """

    def __init__(self, mutation_chance=0.01):
        self._mutation_chance = mutation_chance

    def mutate(self, genotype):
        for gene in genotype:
            if random.uniform(0.0, 1.0) < self._mutation_chance:
                self.mutateGene(gene)

    def mutateGene(self, gene):
        pass
