import unittest
from pancake_problem import *


class PancakeTests(unittest.TestCase):

    def test_initial_input_parsing(self):
        self.assertEqual((['1b', '2b', '3b', '4w'], '-a'), convert_input_string_to_problem("1b2b3b4w-a"))
        self.assertEqual((['1b', '2b', '3b', '4w'], '-f'), convert_input_string_to_problem("1b2b3b4w-f"))
        self.assertEqual((['4b', '1w', '2w', '3b'], '-a'), convert_input_string_to_problem("4b1w2w3b-a"))
        self.assertEqual((['4b', '1w', '2w', '3b'], '-f'), convert_input_string_to_problem("4b1w2w3b-f"))

    def test_state_transition_function(self):
        self.assertEqual((['3w', '2b', '1b', '4w'], 4, 0), get_next_state(['4b', '1w', '2w', '3b'], 0))
        self.assertEqual((['4b', '3w', '2b', '1b'], 3, 1), get_next_state(['4b', '1w', '2w', '3b'], 1))
        self.assertEqual((['4b', '1w', '3w', '2b'], 2, 2), get_next_state(['4b', '1w', '2w', '3b'], 2))
        self.assertEqual((['4b', '1w', '2w', '3w'], 1, 3), get_next_state(['4b', '1w', '2w', '3b'], 3))
        self.assertEqual((['1w', '2w', '3w', '4w'], 4, 0), get_next_state(['4b', '3b', '2b', '1b'], 0))

    def test_goal_test(self):
        self.assertFalse(goal_test(['4b', '3w', '2b', '1b']))
        self.assertTrue(goal_test(['1w', '2w', '3w', '4w']))

    def test_convert_state_to_string(self):
        self.assertEqual("1b2b3b4w", convert_state_to_string(['1b', '2b', '3b', '4w']))
        self.assertEqual("4b1w2w3b", convert_state_to_string(['4b', '1w', '2w', '3b']))

    def test_get_tie_breaker_id(self):
        self.assertEqual(10203041, get_tie_breaker_id(['1b', '2b', '3b', '4w']))
        self.assertEqual(11302141, get_tie_breaker_id(['1w', '3b', '2w', '4w']))

    def test_heuristic(self):
        self.assertEqual(heuristic(['1w', '2w', '3w', '4w']), 0)
        self.assertEqual(heuristic(['1w', '2w', '3w', '4b']), 4)
        self.assertEqual(heuristic(['1b', '2w', '3w', '4w']), 1)
        self.assertEqual(heuristic(['4w', '2w', '3b', '1b']), 4)
        self.assertEqual(heuristic(['1w', '3b', '2w', '4w']), 3)

    def test_get_possible_next_states(self):
        self.assertEqual([(['4w', '3w', '2w', '1w'], 4, 0), (['1b', '4w', '3w', '2w'], 3, 1), (['1b', '2b', '4w', '3w'], 2, 2), (['1b', '2b', '3b', '4w'], 1, 3)], get_possible_next_states(['1b', '2b', '3b', '4b']))

    def test_bfs_search(self):
        # print(run_bfs_search(['4b', '3b', '2b', '1b']))
        # print(run_bfs_search(['1b', '2b', '3b', '4b']))
        print(run_bfs_search(['1b', '2b', '3b', '4w']))


if __name__ == '__main__':
    unittest.main()
