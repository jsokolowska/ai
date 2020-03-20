import unittest
import copy
import random

import numpy as np

import ai.search.ga as ga


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


class FlipBitMutationTest(unittest.TestCase):

    def setUp(self) -> None:
        self.mutation = ga.mutation.FlipBitMutation()

    def testMutationOccurrence(self):
        gene = True
        gene = self.mutation.mutateGene(gene)

        self.assertEqual(gene, False)

    def testMaxMutationChance(self):
        genotype = np.array([bool(random.randint(0, 1)) for i in range(100)])
        negation = [not genotype[i] for i in range(len(genotype))]

        self.mutation.mutation_chance = 1.0
        self.mutation.mutate(genotype)

        self.assertListEqual(list(genotype), negation)

    def testZeroMutationChance(self):
        genotype = np.array([bool(random.randint(0, 1)) for i in range(100)])
        genotype_copy = copy.deepcopy(genotype)

        self.mutation.mutation_chance = 0.0
        self.mutation.mutate(genotype)

        self.assertListEqual(list(genotype), list(genotype_copy))


class SwapGeneMutationTest(unittest.TestCase):

    def setUp(self) -> None:
        self.mutation = ga.mutation.SwapGeneMutation(1.0)

    def testMutationOccurrenceBool(self):
        genotype = np.array([True, False])
        self.mutation.mutate(genotype)

        self.assertListEqual(list(genotype), [False, True])

    def testMutationOccurrenceList(self):
        genotype = np.array([[1, 2], [3, 4, 5]])
        self.mutation.mutate(genotype)

        self.assertListEqual(list(genotype), [[3, 4, 5], [1, 2]])

    def testZeroMutationChance(self):
        genotype = np.array([1, 2])

        self.mutation.mutation_chance = 0.0
        self.mutation.mutate(genotype)

        self.assertListEqual(list(genotype), [1, 2])

    def testTooSmallGenotype(self):
        genotype = np.array([3.14])

        self.assertRaises(ValueError, self.mutation.mutate, genotype)

    def testMutateGeneInheritance(self):
        gene = True
        gene = self.mutation.mutateGene(gene)

        self.assertEqual(gene, True)


class ScrambleGenesMutationTest(unittest.TestCase):

    def setUp(self) -> None:
        self.mutation = ga.mutation.ScrambleGenesMutation(1.0)

    def testMutationOccurrenceBool(self):
        random.seed(1)  # Allows test to pass

        genotype = np.array([True, False])
        self.mutation.mutate(genotype)

        self.assertListEqual(list(genotype), [False, True])

    def testMutationOccurrenceList(self):
        random.seed(1)  # Allows test to pass

        genotype = np.array([[1, 2], [3, 4, 5]])
        self.mutation.mutate(genotype)

        self.assertListEqual(list(genotype), [[3, 4, 5], [1, 2]])

    def testZeroMutationChance(self):
        genotype = np.array([1, 2])

        self.mutation.mutation_chance = 0.0
        self.mutation.mutate(genotype)

        self.assertListEqual(list(genotype), [1, 2])

    def testTooSmallGenotype(self):
        genotype = np.array([3.14])

        self.assertRaises(ValueError, self.mutation.mutate, genotype)

    def testMutateGeneInheritance(self):
        gene = True
        gene = self.mutation.mutateGene(gene)

        self.assertEqual(gene, True)


class InverseGenesMutationTest(unittest.TestCase):

    def setUp(self) -> None:
        self.mutation = ga.mutation.InverseGenesMutation(1.0)

    def testMutationOccurrenceBool(self):
        genotype = np.array([True, False])
        self.mutation.mutate(genotype)

        self.assertListEqual(list(genotype), [False, True])

    def testMutationOccurrenceList(self):
        genotype = np.array([[1, 2], [3, 4, 5]])
        self.mutation.mutate(genotype)

        self.assertListEqual(list(genotype), [[3, 4, 5], [1, 2]])

    def testZeroMutationChance(self):
        genotype = np.array([1, 2])

        self.mutation.mutation_chance = 0.0
        self.mutation.mutate(genotype)

        self.assertListEqual(list(genotype), [1, 2])

    def testTooSmallGenotype(self):
        genotype = np.array([3.14])

        self.assertRaises(ValueError, self.mutation.mutate, genotype)

    def testMutateGeneInheritance(self):
        gene = True
        gene = self.mutation.mutateGene(gene)

        self.assertEqual(gene, True)


if __name__ == "__main__":
    unittest.main()
