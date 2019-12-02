import random
from bisect import bisect_left
from skip_list import SkipList


class TUSL:

    # Creates a new TUSL object, based on the skip_list.
    def __init__(self, skip_list):
        self.TUSL_skip_list = skip_list
        self.max_height = self.TUSL_skip_list.get_max_height()

        # TODO: Initialized TUSL_nodes and origin properly
        self.TUSL_nodes = []
        self.circular()

    def get_origin(self, target_value):
        node = self.TUSL_skip_list.tallest_node
        layer = node.height

        origin = [None for i in range(layer)]
        while layer >= 0:
            next_node = node.next_nodes[layer]
            print(node.value)
            print(next_node.value)
            print(target_value)
            print()
            if node is next_node or node.value <= target_value <= next_node.value or next_node.value <= target_value <= node.value:
                origin[layer] = node
                layer -= 1
            else:
                node = next_node
        return origin

    # Creates a string representation of the TUSL object.
    def __str__(self):
        max_height = self.TUSL_skip_list.get_max_height()
        string_rep = ""
        for level in reversed(range(max_height+1)):
            for node in self.TUSL_nodes:
                if node.height >= level:
                    string_rep += str(node.value).center(5)
                else:
                    string_rep += "     "
            string_rep += "\n"
        return string_rep

    # Creates a circular skip list by removing the two boundary nodes
    def circular(self):
        first_node = self.TUSL_skip_list.nodes[0]

        # Searches the through each node in the skip list for pointers to the end of the list
        for nodes in self.TUSL_skip_list.nodes:
            values = nodes.get_next_node_values()
            if 'inf' in values:
                # Once the we find nodes that has a pointer to the end of the skip list, we store the index of the
                # of the pointer into an array.
                node_index = get_index_of_strings(values, 'inf')

                # Iterate through the created node pointer index to the pointer of the first node index.
                # This is possible since the first node of the list is a node of "-inf" that has pointers to the next
                # nodes
                for index in node_index:
                    nodes.next_nodes[index] = first_node.next_nodes[index]
        # Finally, we remove the boundary nodes as the skip list is already circular.
        self.TUSL_nodes = self.TUSL_skip_list.nodes[1:-1]
        self.origin_target = self.random_node()

    # Search operation. Returns the node for the specified value.
    def search(self, value: float):
        ogtg = self.origin_target
        max_h = self.max_height
        print("OGTG: " + str(ogtg))
        layers = self.nodes_per_layer()
        for i, layer in enumerate(layers):
            print(i)
            for node in layer:
                print("NODE " + str(node))
                print(node.next_nodes[i])
            break







        # start = self.origin
        # print("value: " + str(value))
        # print(start)
        #
        # while True:
        #     current = start
        #     next_node = current.next_nodes[start.height]
        #
        #     if current.value == value:
        #         return current
        #     elif next_node.value < value:
        #         if next_node is not current:
        #             current = next_node
        #         else:
        #             if current.height == 0:
        #                 pass
        return False

    # Insertion operation. Places the specified value into the skip list, if not already present.
    def insert(self, value: float):
        pass

    # This is a helper function that handles the complexity of creating a new node given a list of the nodes that come
    # before it at each layer. The prev_nodes list has the immediate preceding node for level=0 at index 0, and the
    # immediate preceding node for level=1 at 1, and so on.
    def __insert_into_path(self, prev_nodes, value):
        pass

    # Returns a 2D list of nodes by layers, each index represents the layer (0 based)
    def nodes_per_layer(self):
        max_h = self.max_height
        layers = [[] for i in range(max_h+1)]
        for nodes in self.TUSL_nodes:
            layers[nodes.height].append(nodes)
        return layers

    # Find a random node in the TUSL
    def random_node(self):
        if len(self.TUSL_nodes) is not 0:
            return random.choice(self.TUSL_nodes)
        else:
            return None



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

    print(tusl)


    for i in tusl.TUSL_nodes:
        print(i)

    print("----------- EXPERIEMENT -------------")
    print(tusl.get_origin(20))
    # print(tusl.search(0))




main()
