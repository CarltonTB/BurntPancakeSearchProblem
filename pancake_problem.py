# Solve the burnt pancake problem using either BFS or A*
# Author: Carlton Brady
from textwrap import wrap
import queue
from search_tree import *


def convert_input_string_to_problem(input_string):
    """given an input string of the form 1b2b3b4w-a return a tuple containing
    a list of strings for the state and a single string for the search algorithm to use"""
    start_state = wrap(input_string, 2)
    search_type = start_state.pop(len(start_state)-1)
    return start_state, search_type


def get_next_state(state, flip_index, return_cost=True):
    """given a state which is a list of strings and an index at which to flip,
        return the next state, the cost of performing that flip, and the flip that was made"""
    next_state = list.copy(state)
    cost = len(next_state)-flip_index
    next_state[flip_index:len(next_state)] = next_state[flip_index:len(next_state)][::-1]
    for i in range(flip_index, len(next_state)):
        if 'b' in next_state[i]:
            next_state[i] = next_state[i].replace('b', 'w')
        elif 'w' in next_state[i]:
            next_state[i] = next_state[i].replace('w', 'b')

    if return_cost:
        return next_state, cost, flip_index
    else:
        return next_state


def get_possible_next_states(state, return_cost=True):
    """given a state which is a list of strings, return a list of all possible states
    that could be arrived at next with the action taken and their cost"""
    possible_next_states = []
    for i in range(0, len(state)):
        next_state = get_next_state(state, i, return_cost)
        possible_next_states.append(next_state)
    return possible_next_states


def goal_test(state):
    """check if a particular state is the goal"""
    return state == ['1w', '2w', '3w', '4w']


def convert_state_to_string(state):
    """convert a state from list form back into a single string"""
    state_string = ""
    for pancake in state:
        state_string += pancake
    return state_string


def get_tie_breaker_id(state):
    state_string = convert_state_to_string(state)
    state_string = state_string.replace('w', '1')
    state_string = state_string.replace('b', '0')
    return int(state_string)


def heuristic(state):
    """given a state, return the result of the heuristic:
    number of the largest pancake that is out of place"""
    h = 0
    # Loop through all the pancakes
    for i in range(0, len(state)):
        pancake_id = int(state[i][0])
        if pancake_id != i + 1 or 'b' in state[i]:
            # if its burnt side up or the pancake is at the wrong index, then it is out of place
            if pancake_id > h:
                h = pancake_id
    return h


def search(problem):
    """given a problem that is a tuple of start state and search algorithm like so:
        (['4b', '1w', '2w', '3b'], '-a')
        run the specified search algorithm"""
    search_type = problem[1]
    if search_type == '-a':
        return run_a_star_search(problem[0])
    elif search_type == '-f':
        return run_bfs_search(problem[0])
    else:
        return "No valid search algorithm was specified"


def get_solution_state_sequence(goal_tree_node):
    solution_list = []
    cur_node = goal_tree_node
    while cur_node.parent is not None:
        solution_list.append(cur_node.state_string)
        cur_node = cur_node.parent
    solution_list.append(cur_node.state_string)
    # Reverse the order since we were traversing the tree from goal to start
    solution_list = solution_list[::-1]
    solution_string = ""
    for state_string in solution_list:
        solution_string += state_string + "\n"
    return solution_string


def run_bfs_search(start_state):
    """given a starting state that is a list of strings, run BFS search
     and print all steps taken to get to the goal state"""
    search_tree_root = SearchTree(start_state, convert_state_to_string(start_state), {})
    # the fringe is a FIFO queue
    fringe = queue.Queue()
    # first, we enqueue the start state and update the search tree
    fringe.put(search_tree_root)
    # Next, do BFS until the goal is in the fringe
    print("Running BFS Search...")
    while not fringe.empty():
        node_to_expand = fringe.get()
        if heuristic(node_to_expand.state) == 0:
            return get_solution_state_sequence(node_to_expand)
        else:
            possible_next_states = get_possible_next_states(node_to_expand.state, return_cost=False)
            # put the possible next states in descending order based on tie-breaker id
            possible_next_states = sorted(possible_next_states, key=get_tie_breaker_id, reverse=True)
            for state in possible_next_states:
                new_state = SearchTree(state, convert_state_to_string(state), {})
                fringe.put(new_state)
                node_to_expand.add_child(new_state)
    return "Error: failed to find a solution using BFS"


def run_a_star_search(start_state):
    """given a starting state that is a list of strings, run A* search
     and print all steps taken to get to the goal state"""
    return
