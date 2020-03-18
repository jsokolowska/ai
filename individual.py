"""
    Created by: Rafal Uzarowicz
    Created: 17.03.2020
    Last modification: 18.03.2020
    Github: https://github.com/RafalUzarowicz
"""

from numpy import array


class Individual():

    def __init__(self):
        self.__gen = array([])
        self.__name = ""

    def __str__(self):
        if self.__name == "":
            return "Fenotype: {}".format(self.__gen)
        else:
            return "Name: {} - Fenotype {}".format(self.__name, self.__gen)

    def __repr__(self):
        return str(self)

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

    @property
    def name(self):
        print("Getting name")
        return self.__name

    @name.setter
    def name(self, newName):
        print("Setting name")
        self.__name = newName
