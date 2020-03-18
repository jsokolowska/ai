"""
    Created by Joanna Sokołowska on 18.03.2020
    Github: https://github.com/jsokolowska
"""


class Selection:
    """
    Representation of selection

    Selection is an evolutionary mechanism ensuring survival of the fittest.
    User can manipulate selection by adjusting number_of_chosen parameter.
    """

    def __init__(self, number_of_chosen):
        self.number_of_chosen = number_of_chosen

    def select(self, population):
        pass

    @property
    def number_of_chosen(self):
        return self.number_of_chosen

    @number_of_chosen.setter
    def number_of_chosen(self, value):
        if value < 0:
            raise ValueError("Number of individuals to select must be greater than 0")
        self.number_of_chosen = value
