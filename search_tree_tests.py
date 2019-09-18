import unittest
import search_tree
from pancake_problem import *


class SearchTreeTests(unittest.TestCase):
    def test_tree_creation(self):
        root = search_tree.SearchTree(['1b', '2b', '3b', '4w'], convert_state_to_string(['1b', '2b', '3b', '4w']), {})
        n1 = search_tree.SearchTree(['1b', '2b', '3b', '4b'], convert_state_to_string(['1b', '2b', '3b', '4b']), {})
        n2 = search_tree.SearchTree(['1b', '2b', '4w', '3w'], convert_state_to_string(['1b', '2b', '4w', '3w']), {})
        n3 = search_tree.SearchTree(['1b', '2b', '4w', '3b'], convert_state_to_string(['1b', '2b', '4w', '3b']), {})
        n1.add_child(n3)
        n1.add_child(n2)
        root.add_child(n1)
        self.assertEqual(1, len(root.children.keys()))


if __name__ == '__main__':
    unittest.main()
