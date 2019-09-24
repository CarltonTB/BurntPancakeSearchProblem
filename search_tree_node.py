

class SearchTreeNode:

    def __init__(self, state, state_string, children, flip_index=None):
        self.state_string = state_string
        self.state = state
        # The flip action that was taken to arrive in this state
        self.flip_index = flip_index
        # The cost of the flip action that was taken to arrive in this state
        self.cost = self.flip_index + 1 if flip_index is not None else None
        self.parent = None
        self.children = children

    def add_child(self, new_child):
        self.children.update({new_child.state_string: new_child})
        new_child.parent = self

    def get_tie_breaker_id(self):
        state_string = "".join(self.state)
        state_string = state_string.replace('w', '1')
        state_string = state_string.replace('b', '0')
        return int(state_string)

    def __gt__(self, other):
        """Since the priority queue dequeues the "smaller" nodes first,
         when nodes have equal priority ((fn) value) the tie-breaking comparison
         should consider the node with the smaller tie-breaker id as lower priority
         (having larger priority number), which is why the node with smaller tie-breaker id
         must be considered "larger" if the 2 nodes have same f(n) value.
         """
        return self.get_tie_breaker_id() < other.get_tie_breaker_id()

    def __lt__(self, other):
        """This is similarly counter-intuitive for the reasons mentioned in the __gt__ function"""
        return self.get_tie_breaker_id() > other.get_tie_breaker_id()

    def __str__(self):
        tree_string = "parent: " + self.state_string + "\n"
        tree_string += "children: " + "\n"
        for key in self.children.keys():
            tree_string += self.children.get(key).state_string
            tree_string += "\n"
        return tree_string

