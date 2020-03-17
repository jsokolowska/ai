"""
    Created by: Rafal Uzarowicz
    Date: 17.03.2020
    Github: https://github.com/RafalUzarowicz
"""

from numpy import array


class Individual():

    def __init__(self):
        self.__gen = array([])

    @property
    def genotype(self):
        print("Getting genotype.")
        return self.__gen

    @genotype.setter
    def genotype(self, gen):
        print("Setting genotype.")
        self.__gen = gen

    @property
    def fenotype(self):
        print("Getting fenotype.")
        return self.__gen
