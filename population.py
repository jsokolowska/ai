"""
    Created by:                 Anton Masiukevich
    Date of creation:           17.03.2020
    Date of last modification:  19.03.2020
    Profile:                    https://github.com/Tocha10101
"""

import numpy as np

class Population():

    """
        A class to represent population in given genetic algorithm
    """

    def __init__(self, individs=np.array([])):
        self.__individs = individs

    def getIndivids(self) -> np.array:
        print("Getter called")
        return self.__individs

    def setIndivids(self, individs: np.array):
        print("Setter called")
        if len(individs) < 0:
            raise ValueError("There is an error with given population")
        self.__individs = individs

    def delIndivids(self):
        self.__individs = np.array([])

    # TODO: restoring population method

    individs = property(fget=getIndivids, fset=setIndivids, fdel=delIndivids)