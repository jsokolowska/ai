"""
    Created by: Rafal Uzarowicz
    Date: 17.03.2020
    Github: https://github.com/RafalUzarowicz
"""

class Individual:
    __gen = []

    def getGen(self):
        return self.__gen

    def setGen(self, gen):
        self.__gen = gen

    def getFeno(self):
        return self.__gen

