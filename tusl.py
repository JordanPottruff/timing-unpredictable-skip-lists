import random


class SkipList:

    # Creates a new SkipList object, which is initially empty.
    def __init__(self):
        self.entry_node = None
        self.nodes = []

    # Creates a string representation of the TUSL object.
    def __str__(self):
        pass

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


def main():
    list = SkipList()
    for i in range(100):
        list.insert(i)
    print(list)
    print(list.search(10))


# main()
