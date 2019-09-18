

class SearchTree:

    def __init__(self, state, state_string, children):
        self.state_string = state_string
        self.state = state
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

