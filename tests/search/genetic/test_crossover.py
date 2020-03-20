import unittest
import random
import copy

import numpy as np

import ai.search.ga as ga


class BaseCrossoverTest(unittest.TestCase):

    def setUp(self) -> None:
        self.crossover = ga.crossover.Crossover()

        self.parent_a = np.array([random.randint(0, 10) for i in range(10)])
        self.parent_b = np.array([random.randint(0, 10) for i in range(10)])

        self.parent_a_copy = copy.deepcopy(self.parent_a)
        self.parent_b_copy = copy.deepcopy(self.parent_b)

    def testDefaultCross(self):
        self.parent_a, self.parent_b = self.crossover.cross(self.parent_a, self.parent_b)

        self.assertListEqual(list(self.parent_a), list(self.parent_a_copy))
        self.assertListEqual(list(self.parent_b), list(self.parent_b_copy))

    def testInplaceCross(self):
        self.crossover.cross(self.parent_a, self.parent_b, inplace=True)

        self.assertListEqual(list(self.parent_a), list(self.parent_a_copy))
        self.assertListEqual(list(self.parent_b), list(self.parent_b_copy))


