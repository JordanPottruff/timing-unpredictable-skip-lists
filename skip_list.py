# skip_list.py
# Implementation of the normal skip list data structure.
import random


class SkipList:

    # Creates a new SkipList object, which is initially empty.
    def __init__(self):
        self.start_node, self.end_node = bounding_nodes()
        # This self.nodes list is not necessary for the actual algorithms themselves. Instead, we will begin queries
        # at the start_node. None the less, maintaining a linked list representing the bottom layer of the skip list
        # makes the __str__ implementation easier.
        self.nodes = [self.start_node, self.end_node]
        self.tallest_node = None

    # Creates a string representation of the skip list object. The output should be a string that, when printed,
    # resembles the skip list diagrams found online.
    def __str__(self):
        max_height = self.start_node.height

        string_rep = ""
        for level in reversed(range(max_height+1)):
            for node in self.nodes:
                if node.height >= level:
                    string_rep += str(node.value).center(5)
                else:
                    string_rep += "     "
            string_rep += "\n"
        return string_rep

    # Search operation. Returns the node for the specified value.
    def search(self, value: float):
        current = self.start_node
        height = current.height

        # We can now traverse the skip list until we find the location at the bottom-most layer or we find that the
        # element already exists.
        while True:
            # Next node is the node pointed to at the current level.
            next_node = current.next_nodes[height]

            # If our target value is less than the value of the next node at this level, then we need to drop down to
            # a lower level (if possible).
            if value < next_node.value:

                # If we are at the bottom-most layer (the true linked list layer), then we cannot drop any further. This
                # means that our target value does not exist, and we therefore return 'None'.
                if height == 0:
                    return None

                # If we are not yet at the lowest level, then we need to continue moving down the layers.
                else:
                    height -= 1

            # If the target value is larger than the next node value, then we simply jump across the linked list (in
            # constant time) to reach this next_node. We will continue the search from there.
            elif value > next_node.value:
                current = next_node

            # If the target value is equal to our next node, then we will return the node itself.
            else:
                return next_node

    # Insertion operation. Places the specified value into the skip list, if not already present.
    def insert(self, value: float):
        # Start the search at the starting node (left-most node in self.nodes list).
        current = self.start_node
        height = current.height

        # While traversing the skip list, we will need to record the largest node at each level that is smaller than the
        # inserted value. This will allow us to quickly update the connections at each level for the new node. The
        # prev_nodes variable will be a list with the node at level=0 at index 0, level=1 at 1, etc.
        prev_nodes = []

        # We can now traverse the skip list until we find the location at the bottom-most layer or we find that the
        # element already exists.
        while True:
            # Next node is the node pointed to at the current level.
            next_node = current.next_nodes[height]

            # If our target value is less than the value of the next node at this level, then we need to drop down to
            # a lower level (if possible).
            if value < next_node.value:

                # For the given level we just evaluated (stored in the variable 'height'), the current node must be the
                # largest node that is still less than the target value. Otherwise, the above condition would not have
                # been triggered yet.
                prev_nodes.insert(0, current)

                # If we are at the bottom-most layer (the true linked list layer), then we have found the correct
                # location for our new value: immediately after the current node (which is before the next_node, which
                # we established to be too large in the if-statement).
                if height == 0:

                    # A helper method is used to insert the value as a new node. This method updates all the necessary
                    # pointers at each level that is less than or equal to the height of the new node (via the
                    # prev_nodes list).
                    self.__insert_into_path(prev_nodes, value)
                    return

                # If we are not yet at the lowest level, then we need to continue moving down the layers.
                else:
                    height -= 1

            # If the target value is larger than the next node value, then we simply jump across the linked list (in
            # constant time) to reach this next_node. We will continue the search from there.
            elif value > next_node.value:
                current = next_node

            # If the target value is equal to our next node, then we will print a simple statement letting the user
            # know.
            else:
                print("Value already in list!")

    # This is a helper function that handles the complexity of creating a new node given a list of the nodes that come
    # before it at each layer. The prev_nodes list has the immediate preceding node for level=0 at index 0, and the
    # immediate preceding node for level=1 at 1, and so on.
    def __insert_into_path(self, prev_nodes, value):
        # We first generate a random height for this node according to a coin toss probability.
        height = random_height()
        # We now create a new node object, which is initialized with no next nodes.
        new_node = Node(value, height, [])

        # We iterate through each level less than or equal to the node's generated height in order to set the previous
        # node at each layer to point to the new node, and the new node to point to the next node in that layer.
        for i in range(height+1):
            # When we visit a layer that is higher than the previously highest node (which is also the height of the
            # start and ending nodes), then we can simply link this node to the start and end nodes.
            if i > self.start_node.height:
                # Reset tallest node to be the current node.
                self.tallest_node = new_node
                # The new node is added as the next node for the starting node at the current height (i).
                self.start_node.add_next_node(new_node)
                # The next node of the new node is the ending node.
                new_node.add_next_node(self.end_node)
                # The starting and ending nodes are updated to be of height i.
                self.start_node.height = i
                self.end_node.height = i
            # For layers that are less than the highest layer, we can simply update the nodes neighboring our new node.
            # These nodes found using the prev_nodes list, which records the preceding node of the new node at each
            # layer.
            else:
                # We can get the node that should immediately follow the new node by simply grabbing the next node of
                # the previous node at the current layer.
                next_node = prev_nodes[i].next_nodes[i]

                # The new node is then updated to point to this next node.
                new_node.add_next_node(next_node)
                # The previous node is updated to point to the new node (rather than the next node).
                prev_nodes[i].next_nodes[i] = new_node

        # Lastly, we need to update the underlying linked list to contain the new node as well.
        self.nodes.insert(self.nodes.index(prev_nodes[0])+1, new_node)

    # Return the max height of the skip list
    def get_max_height(self):
        return self.nodes[0].height


class Node:
    def __init__(self, value: float, height: int, next_nodes: list):
        self.value = value
        self.height = height
        self.next_nodes = next_nodes

    def __str__(self):
        next_nodes = self.get_next_node_values()
        return "val: {}, height: {}, next_nodes: {}".format(self.value, self.height, next_nodes)

    def add_next_node(self, node):
        self.next_nodes.append(node)

    def get_next_node_values(self):
        next_nodes = []
        for values in self.next_nodes:
            next_nodes.append(str(values.value))
        return next_nodes


# Creates the "bounding notes" which are nodes with negative and positive infinity values.
def bounding_nodes():
    positive_inf_node = Node(float('inf'), 0, [])
    negative_inf_node = Node(float('-inf'), 0, [positive_inf_node])
    return negative_inf_node, positive_inf_node


# Generates a random height according to a coin flip probability of continuing to the next level.
def random_height():
    height = 0
    while random.choice([True, False]):
        height += 1
    return height


def main():
    list = SkipList()
    for i in range(1000):
        list.insert(i)
    print(list)
    print(list.search(2))


# main()
