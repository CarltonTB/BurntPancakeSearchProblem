# Solve the burnt pancake problem using either BFS or A*
# Author: Carlton Brady
from textwrap import wrap
import queue
from search_tree_node import *


def convert_input_string_to_problem(input_string):
    """given an input string of the form 1b2b3b4w-a return a tuple containing
    a list of strings for the state and a single string for the search algorithm to use"""
    start_state = wrap(input_string, 2)
    search_type = start_state.pop(len(start_state)-1)
    return start_state, search_type


def get_next_state(start_state_node, flip_index):
    """given a state which is a SearchTree node and an index at which to flip,
        return the next state node, the cost of performing that flip, and the flip that was made"""
    next_state = list.copy(start_state_node.state)
    cost = len(next_state)-flip_index
    next_state[flip_index:len(next_state)] = next_state[flip_index:len(next_state)][::-1]
    for i in range(flip_index, len(next_state)):
        if 'b' in next_state[i]:
            next_state[i] = next_state[i].replace('b', 'w')
        elif 'w' in next_state[i]:
            next_state[i] = next_state[i].replace('w', 'b')

    return SearchTreeNode(next_state, "".join(next_state), {}, flip_index=flip_index)


def get_possible_next_states(state_node):
    """given a state which is a list of strings, return a list of all possible states
    that could be arrived at next with the action taken and their cost"""
    possible_next_states = []
    for i in range(0, len(state_node.state)):
        next_state = get_next_state(state_node, i)
        possible_next_states.append(next_state)
    return possible_next_states


def goal_test(state):
    """check if a particular state is the goal"""
    return state == ['1w', '2w', '3w', '4w']


def get_tie_breaker_id(state_node):
    state_string = "".join(state_node.state)
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
        return run_bfs(problem[0])
    else:
        return "No valid search algorithm was specified"


def get_solution_string(goal_tree_node, show_costs=False):
    state_sequence_solution_list = []
    cur_node = goal_tree_node
    spatula_index = None
    while cur_node.parent is not None:
        g = get_total_cost_along_path(cur_node)
        h = heuristic(cur_node.state)
        cost_string = ""
        if spatula_index is not None:
            # insert the spatula into the string
            cur_node.state.insert(spatula_index, '|')
        if show_costs:
            cost_string += " g=" + str(g) + ", h=" + str(h)
        state_sequence_solution_list.append("".join(cur_node.state) + cost_string)
        spatula_index = cur_node.flip_index
        cur_node = cur_node.parent
    # when we exit the loop we are at the root of the tree, which is the start state
    g = get_total_cost_along_path(cur_node)
    h = heuristic(cur_node.state)
    cost_string = ""
    if show_costs:
        cost_string += " g=" + str(g) + ", h=" + str(h)
    cur_node.state.insert(spatula_index, '|')
    state_sequence_solution_list.append("".join(cur_node.state) + cost_string)
    # Reverse the order since we were traversing the tree from goal to start
    state_sequence_solution_list = state_sequence_solution_list[::-1]
    solution_string = ""
    for state_string in state_sequence_solution_list:
        solution_string += state_string + "\n"
    return solution_string


def get_total_cost_along_path(state_node):
    """Given a search tree node, calculate total cost it takes to get to that state"""
    cur_node = state_node
    total_cost = 0
    while cur_node.parent is not None:
        total_cost += cur_node.cost
        cur_node = cur_node.parent
    return total_cost


def run_bfs(start_state, show_costs=False):
    """given a starting state that is a list of strings, run BFS search
     and print all steps taken to get to the goal state"""
    search_tree_root = SearchTreeNode(start_state, "".join(start_state), {})
    # the fringe is a FIFO queue
    fringe = queue.Queue()
    # first, we enqueue the start state
    fringe.put(search_tree_root)
    # Next, do BFS until the goal is in the fringe
    print("Running BFS...")
    while not fringe.empty():
        node_to_expand = fringe.get()
        if goal_test(node_to_expand.state):
            print("Solution found:\n")
            solution_string = get_solution_string(node_to_expand, show_costs=show_costs)
            print(solution_string)
            return solution_string
        else:
            possible_next_states = get_possible_next_states(node_to_expand)
            # put the possible next states in descending order based on tie-breaker id
            possible_next_states = sorted(possible_next_states, key=get_tie_breaker_id, reverse=True)
            for new_state_node in possible_next_states:
                node_to_expand.add_child(new_state_node)
                fringe.put(new_state_node)
    return "Error: failed to find a solution using BFS"


def run_a_star_search(start_state, show_costs=True):
    """given a starting state that is a list of strings, run A* search
     and print all steps taken to get to the goal state"""
    search_tree_root = SearchTreeNode(start_state, "".join(start_state), {})
    # The fringe is a priority queue, with the priority number being the value return from the function:
    # f(n) = g(n) + h(n)
    fringe = queue.PriorityQueue()
    g = 0
    # first, we enqueue the start state
    fringe.put((g + heuristic(start_state), search_tree_root))
    # Next, do A* until the goal is dequeue'd from the priority queue
    print("Running A* search...")
    while not fringe.empty():
        node_to_expand = fringe.get()[1]
        # g = get_total_cost_along_path(node_to_expand)
        if heuristic(node_to_expand.state) == 0:
            print("Solution found:\n")
            solution_string = get_solution_string(node_to_expand, show_costs=show_costs)
            print(solution_string)
            return solution_string
        else:
            possible_next_states = get_possible_next_states(node_to_expand)
            # put the possible next states in the priority queue based on f(n) value
            for new_state_node in possible_next_states:
                node_to_expand.add_child(new_state_node)
                fringe.put((get_total_cost_along_path(new_state_node) + heuristic(new_state_node.state), new_state_node))
    return "Error: failed to find a solution using A* search"

