import unittest
from search.genetic.Selection import Selection


class TestSelection(unittest.TestCase):

    def test_set_selection_size(self):
        selection = Selection(10)
        with self.assertRaises(ValueError): selection.set_selection_size(-10)
