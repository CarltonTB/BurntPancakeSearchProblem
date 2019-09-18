

class SearchTreeNode:

    def __init__(self, state, state_string, children, flip_index=None):
        self.state_string = state_string
        self.state = state
        # The flip action that was taken to arrive in this state
        self.flip_index = flip_index
        # The cost of the flip action that was taken to arrive in this state
        self.cost = len(state)-self.flip_index if flip_index is not None else None
        self.parent = None
        self.children = children

    def add_child(self, new_child):
        self.children.update({new_child.state_string: new_child})
        new_child.parent = self

    def __str__(self):
        tree_string = "parent: " + self.state_string + "\n"
        tree_string += "children: " + "\n"
        for key in self.children.keys():
            tree_string += self.children.get(key).state_string
            tree_string += "\n"
        return tree_string

