import random
from skip_list import SkipList


class TUSL:

    # Creates a new TUSL object, based on the skip_list.
    def __init__(self, skip_list):
        self.TUSL_skip_list = skip_list

        # TODO: Initialized TUSL_nodes properly
        self.TUSL_nodes = []

    # Creates a string representation of the TUSL object.
    def __str__(self):
        max_height = self.TUSL_skip_list.get_max_height()
        string_rep = ""
        for level in reversed(range(max_height+1)):
            for node in self.TUSL_skip_list.nodes:
                if node.height >= level:
                    string_rep += str(node.value).center(5)
                else:
                    string_rep += "     "
            string_rep += "\n"
        return string_rep

    # Creates a circular skip list by removing the two boundary nodes
    def circular(self):
        first_node = self.TUSL_skip_list.nodes[0]
        for nodes in self.TUSL_skip_list.nodes:
            values = nodes.get_next_node_values()
            if 'inf' in values:
                n = get_index_of_strings(values, 'inf')
                for index in n:
                    nodes.next_nodes[index] = first_node.next_nodes[index]
        self.TUSL_nodes = self.TUSL_skip_list.nodes[1:-1]

    # Search operation. Returns the node for the specified value.
    def search(self, value: float):
        pass

    # Insertion operation. Places the specified value into the skip list, if not already present.
    def insert(self, value: float):
        pass

    # This is a helper function that handles the complexity of creating a new node given a list of the nodes that come
    # before it at each layer. The prev_nodes list has the immediate preceding node for level=0 at index 0, and the
    # immediate preceding node for level=1 at 1, and so on.
    def __insert_into_path(self, prev_nodes, value):
        pass


class Node:

    def __init__(self, value: float, height: int, next_nodes: list):
        self.value = value
        self.height = height
        self.next_nodes = next_nodes

    def __str__(self):
        return "val: {}, height: {}, next_nodes: {}".format(self.value, self.height, str(self.next_nodes))

    def add_next_node(self, node):
        self.next_nodes.append(node)


# Generates a random height according to a coin flip probability of continuing to the next level.
def random_height():
    height = 0
    while random.choice([True, False]):
        height += 1
    return height


# Generate an index array, where the index where the str appears
def get_index_of_strings(arr, str):
    index = []
    for i, string in enumerate(arr):
        if string == str:
            index.append(i)
    return index


def main():
    skip_list = SkipList()
    for i in range(100):
        skip_list.insert(i)

    tusl = TUSL(skip_list)
    tusl.circular()

    print(tusl)
    for i in tusl.TUSL_nodes:
        print(i)


main()
