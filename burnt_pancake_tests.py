import unittest
from burnt_pancake_problem import *


class PancakeTests(unittest.TestCase):

    def test_initial_input_parsing(self):
        self.assertEqual((['1b', '2b', '3b', '4w'], '-a'), convert_input_string_to_problem("1b2b3b4w-a"))
        self.assertEqual((['1b', '2b', '3b', '4w'], '-f'), convert_input_string_to_problem("1b2b3b4w-f"))
        self.assertEqual((['4b', '1w', '2w', '3b'], '-a'), convert_input_string_to_problem("4b1w2w3b-a"))
        self.assertEqual((['4b', '1w', '2w', '3b'], '-f'), convert_input_string_to_problem("4b1w2w3b-f"))

    def test_state_transition_function(self):
        test_start_state = ['4b', '1w', '2w', '3b']
        test_start_state_node = SearchTreeNode(test_start_state, "".join(test_start_state), {})
        next_state_node = get_next_state(test_start_state_node, 0)
        self.assertEqual((['4w', '1w', '2w', '3b']), next_state_node.state)
        self.assertEqual(1, next_state_node.cost)
        self.assertEqual(0, next_state_node.flip_index)

        next_state_node2 = get_next_state(test_start_state_node, 1)
        self.assertEqual((['1b', '4w', '2w', '3b']), next_state_node2.state)
        self.assertEqual(2, next_state_node2.cost)
        self.assertEqual(1, next_state_node2.flip_index)

        next_state_node3 = get_next_state(test_start_state_node, 2)
        self.assertEqual((['2b', '1b', '4w', '3b']), next_state_node3.state)
        self.assertEqual(3, next_state_node3.cost)
        self.assertEqual(2, next_state_node3.flip_index)

        next_state_node4 = get_next_state(test_start_state_node, 3)
        self.assertEqual((['3w', '2b', '1b', '4w']), next_state_node4.state)
        self.assertEqual(4, next_state_node4.cost)
        self.assertEqual(3, next_state_node4.flip_index)

    def test_goal_test(self):
        self.assertFalse(goal_test(['4b', '3w', '2b', '1b']))
        self.assertTrue(goal_test(['1w', '2w', '3w', '4w']))

    def test_get_tie_breaker_id(self):
        test_state = ['1b', '2b', '3b', '4w']
        test_state_node = SearchTreeNode(test_state, "".join(test_state), {})
        test_state2 = ['1w', '3b', '2w', '4w']
        test_state_node2 = SearchTreeNode(test_state2, "".join(test_state2), {})
        self.assertEqual(10203041, get_tie_breaker_id(test_state_node))
        self.assertEqual(11302141, get_tie_breaker_id(test_state_node2))

    def test_heuristic(self):
        self.assertEqual(heuristic(['1w', '2w', '3w', '4w']), 0)
        self.assertEqual(heuristic(['1w', '2w', '3w', '4b']), 4)
        self.assertEqual(heuristic(['1b', '2w', '3w', '4w']), 1)
        self.assertEqual(heuristic(['4w', '2w', '3b', '1b']), 4)
        self.assertEqual(heuristic(['1w', '3b', '2w', '4w']), 3)

    def test_get_possible_next_states(self):
        test_start_state = ['1b', '2b', '3b', '4b']
        test_start_state_node = SearchTreeNode(test_start_state, "".join(test_start_state), {})
        next_state_list = get_possible_next_states(test_start_state_node)
        self.assertEqual(4, len(next_state_list))

    def test_bfs(self):
        solution = run_bfs(['4b', '3b', '2b', '1b'])
        solution2 = run_bfs(['1b', '2b', '3b', '4b'])
        solution3 = run_bfs(['1b', '2b', '3b', '4w'])

        self.assertTrue("1w2w3w4w" in solution)
        # The number of new line characters will match the number of states in the solution
        self.assertEqual(2, solution.count('\n'))

        self.assertTrue("1w2w3w4w" in solution2)
        self.assertEqual(9, solution2.count('\n'))

        self.assertTrue("1w2w3w4w" in solution3)
        self.assertEqual(7, solution3.count('\n'))

    def test_a_star_search(self):
        solution = run_a_star_search(['4b', '3b', '2b', '1b'])
        solution2 = run_a_star_search(['1b', '2b', '3b', '4b'])
        solution3 = run_a_star_search(['1b', '2b', '3b', '4w'])
        self.assertTrue("1w2w3w4w" in solution)
        # The number of new line characters will match the number of states in the solution
        self.assertEqual(2, solution.count('\n'))

        self.assertTrue("1w2w3w4w" in solution2)
        self.assertEqual(11, solution2.count('\n'))

        self.assertTrue("1w2w3w4w" in solution3)
        self.assertEqual(8, solution3.count('\n'))

    def test_compare_searches(self):
        solution_a_star = run_a_star_search(['1b', '2b', '3b', '4w'])
        solution_bfs = run_bfs(['1b', '2b', '3b', '4w'], show_costs=True)

        solution_a_star2 = run_a_star_search(['1b', '2b', '3b', '4b'])
        solution_bfs2 = run_bfs(['1b', '2b', '3b', '4b'], show_costs=True)

        self.assertTrue("1w2w3w4w g=20" in solution_a_star2)
        self.assertTrue("1w2w3w4w g=28" in solution_bfs2)

        self.assertTrue("1w2w3w4w g=13" in solution_a_star)
        self.assertTrue("1w2w3w4w g=15" in solution_bfs)


if __name__ == '__main__':
    unittest.main()
