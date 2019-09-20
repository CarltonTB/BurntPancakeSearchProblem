import unittest
import search_tree_node
from burnt_pancake_problem import *
import queue


class SearchTreeTests(unittest.TestCase):

    def test_tree_creation(self):
        root = search_tree_node.SearchTreeNode(['1b', '2b', '3b', '4w'], "".join(['1b', '2b', '3b', '4w']), {})
        n1 = search_tree_node.SearchTreeNode(['1b', '2b', '3b', '4b'], "".join(['1b', '2b', '3b', '4b']), {}, 3)
        n2 = search_tree_node.SearchTreeNode(['1b', '2b', '4w', '3w'], "".join(['1b', '2b', '4w', '3w']), {}, 2)
        n3 = search_tree_node.SearchTreeNode(['1b', '2b', '4w', '3b'], "".join(['1b', '2b', '4w', '3b']), {}, 3)
        n1.add_child(n3)
        n1.add_child(n2)
        root.add_child(n1)
        self.assertEqual(2, get_total_cost_along_path(n3))
        self.assertEqual(3, get_total_cost_along_path(n2))
        self.assertEqual(1, len(root.children.keys()))

    def test_tree_node_priority_queue(self):
        root = search_tree_node.SearchTreeNode(['1b', '2b', '3b', '4w'], "".join(['1b', '2b', '3b', '4w']), {})
        n1 = search_tree_node.SearchTreeNode(['1b', '2b', '3b', '4b'], "".join(['1b', '2b', '3b', '4b']), {}, 3)
        n2 = search_tree_node.SearchTreeNode(['1b', '2b', '4w', '3w'], "".join(['1b', '2b', '4w', '3w']), {}, 3)
        fringe = queue.PriorityQueue()
        fringe.put((0, root))
        fringe.put((1, n2))
        fringe.put((1, n1))
        self.assertEqual(3, fringe.qsize())
        root = fringe.get()
        n2 = fringe.get()
        n1 = fringe.get()
        # this shows that given 2 nodes n1 and n2 with the same priority number,
        # the one with the larger tie-breaker id (n2) is dequeue'd first
        self.assertEqual(['1b', '2b', '3b', '4w'], root[1].state)
        self.assertEqual(['1b', '2b', '4w', '3w'], n2[1].state)
        self.assertEqual(['1b', '2b', '3b', '4b'], n1[1].state)


if __name__ == '__main__':
    unittest.main()
