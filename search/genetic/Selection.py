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

    def __init__(self, selection_size=None):
        if selection_size<0:
            raise ValueError("Number of individuals to select must be greater than 0")
        self.selection_size = selection_size

    def select(self, population):
        pass

    def get_selection_size(self):
        return self.selection_size

    def set_selection_size(self, value):
        if value < 0:
            raise ValueError("Number of individuals to select must be greater than 0")
        self.selection_size = value
