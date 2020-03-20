import unittest
import copy
import random

import ai.search.genetic as ga


class BaseMutationTest(unittest.TestCase):
    def setUp(self) -> None:
        self.mutation = ga.mutation.Mutation()

    def testSetMutationChance(self):
        self.mutation.mutation_chance = 0.5

        self.assertEqual(self.mutation.mutation_chance, 0.5)

    def testSetMutationChanceException(self):
        def setMutationChance(mutation_chance):
            self.mutation.mutation_chance = mutation_chance

        self.assertRaises(ValueError, setMutationChance, -0.1)
        self.assertRaises(ValueError, setMutationChance, 1.1)

    def testDefaultMutateGene(self):
        self.mutation.mutation_chance = 1.0
        gene1 = "gene1"
        gene2 = True

        gene1 = self.mutation.mutateGene(gene1)
        gene2 = self.mutation.mutateGene(gene2)

        self.assertEqual(gene1, "gene1")
        self.assertEqual(gene2, True)


class BasicMutation(ga.mutation.Mutation):
    def mutateGene(self, gene):
        return not gene


class BasicMutationImplementationTest(unittest.TestCase):

    def setUp(self) -> None:
        self.mutation = BasicMutation()

    def testMutationOccurrence(self):
        gene = True
        gene = self.mutation.mutateGene(gene)

        self.assertEqual(gene, False)

    def testMaxMutationChance(self):
        genotype = [bool(random.randint(0, 1)) for i in range(100)]
        negation = [not genotype[i] for i in range(len(genotype))]

        self.mutation.mutation_chance = 1.0
        self.mutation.mutate(genotype)

        self.assertListEqual(genotype, negation)

    def testZeroMutationChance(self):
        genotype = [bool(random.randint(0, 1)) for i in range(100)]
        genotype_copy = copy.deepcopy(genotype)

        self.mutation.mutation_chance = 0.0
        self.mutation.mutate(genotype)

        self.assertListEqual(genotype, genotype_copy)


if __name__ == "__main__":
    unittest.main()
