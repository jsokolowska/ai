"""
    Created by: Rafal Uzarowicz
    Date of creation: 17.03.2020
    Date of last modification: 18.03.2020
    Github: https://github.com/RafalUzarowicz
"""

from numpy import array


class Individual():

    def __init__(self, genotype=None):
        if genotype is None:
            genotype = []

        self.__genotype = array(genotype)
        self.__fitness = None

    def __str__(self):
        if self.__fitness is None:
            return "Fenotype: {0}".format(self.__genotype)
        else:
            return "Fitness: \"{0}\" - Fenotype: {1}".format(self.__fitness, self.__genotype)

    def __repr__(self):
        return str(self)

    def generateFenotype(self):
        return self.__genotype

    @property
    def genotype(self):
        print("Getting genotype.")
        return self.__genotype

    @genotype.setter
    def genotype(self, newGenotype):
        print("Setting genotype.")
        self.__genotype = newGenotype

    @property
    def fitness(self):
        print("Getting fitness")
        return self.__fitness

    @fitness.setter
    def fitness(self, newFitness):
        print("Setting name")
        self.__fitness = newFitness
