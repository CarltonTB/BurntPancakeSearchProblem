import unittest
import search_tree_node
from burnt_pancake_problem import *


class SearchTreeTests(unittest.TestCase):
    def test_tree_creation(self):
        root = search_tree_node.SearchTreeNode(['1b', '2b', '3b', '4w'], "".join(['1b', '2b', '3b', '4w']), {})
        n1 = search_tree_node.SearchTreeNode(['1b', '2b', '3b', '4b'], "".join(['1b', '2b', '3b', '4b']), {})
        n2 = search_tree_node.SearchTreeNode(['1b', '2b', '4w', '3w'], "".join(['1b', '2b', '4w', '3w']), {})
        n3 = search_tree_node.SearchTreeNode(['1b', '2b', '4w', '3b'], "".join(['1b', '2b', '4w', '3b']), {})
        n1.add_child(n3)
        n1.add_child(n2)
        root.add_child(n1)
        self.assertEqual(1, len(root.children.keys()))


if __name__ == '__main__':
    unittest.main()
