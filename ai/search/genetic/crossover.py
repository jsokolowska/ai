"""
    Created by michal-swiatek on 17.03.2020
    Github: https://github.com/michal-swiatek
"""


class Crossover:
    """
        Representation of crossover

        Crossover is a genetic operator responsible for generating offspring
        from parents. Child's genotype is a mix of both parents genes and
        crossover defines strategy according to which parent genes are chosen
    """

    def cross(self, parent_a: [], parent_b: [], inplace=False):
        """
            Performs crossover of two individuals

            To change crossover strategy override this function

        :param parent_a: genotype of first individual
        :param parent_b: genotype of second individual
        :param inplace: should an operation take place on individuals or copy
        :return: when not inplace - pair of new individuals
        """
        if inplace:
            pass
        else:
            return parent_a, parent_b
