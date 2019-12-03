import random
from skip_list import SkipList, Node


class TUSL:

    # Creates a new TUSL object, based on the skip_list.
    def __init__(self, skip_list):
        self.skip_list = skip_list
        self.max_height = self.skip_list.get_max_height()

        # TODO: Initialized TUSL_nodes and origin properly
        self.nodes = []
        self.circular()

    # Creates a string representation of the TUSL object.
    def __str__(self):
        max_height = self.skip_list.get_max_height()
        string_rep = ""
        for level in reversed(range(max_height + 1)):
            for node in self.nodes:
                if node.height >= level:
                    string_rep += str(node.value).center(5)
                else:
                    string_rep += "     "
            string_rep += "\n"
        return string_rep

    # Creates a circular skip list by removing the two boundary nodes
    def circular(self):
        first_node = self.skip_list.nodes[0]

        # Searches the through each node in the skip list for pointers to the end of the list
        for nodes in self.skip_list.nodes:
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
        self.nodes = self.skip_list.nodes[1:-1]

    def get_origin(self, target_value):
        node = self.skip_list.tallest_node
        layer = node.height

        origin = [None for i in range(layer+1)]
        while layer >= 0:
            next_node = node.next_nodes[layer]
            if node is next_node or node.value <= target_value <= next_node.value:
                origin[layer] = node
                layer -= 1
            elif node.value > next_node.value:
                if target_value <= next_node.value or target_value > node.value:
                    origin[layer] = node
                    layer -= 1
                else:
                    node = next_node
            else:
                node = next_node
        return origin

    # Search operation. Returns the node for the specified value.
    def search(self, value: float):
        target = random.randint(self.nodes[0].value, self.nodes[-1].value)
        origin = self.get_origin(target)
        nodes = [node.next_nodes[i] for i, node in enumerate(origin)]
        height = len(nodes) - 1

        while height >= 0:
            cur_node = nodes[height]
            next_node = cur_node.next_nodes[height]

            if cur_node.value == value:
                return cur_node
            elif next_node.value == value:
                return next_node
            elif cur_node is next_node or cur_node.value < value < next_node.value:
                if height == 0:
                    return None
                else:
                    height -= 1
            elif cur_node.value > next_node.value:
                if value < next_node.value or value > cur_node.value:
                    height -= 1
                else:
                    nodes = cur_node.next_nodes
            else:
                nodes = cur_node.next_nodes
        print("Shouldnt happen")
        return None

    # Returns a 2D list of nodes by layers, each index represents the layer (0 based)
    def nodes_per_layer(self):
        max_h = self.max_height
        layers = [[] for i in range(max_h+1)]
        for nodes in self.nodes:
            layers[nodes.height].append(nodes)
        return layers


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


    #for i in tusl.TUSL_nodes:
    #    print(i)

    print("----------- EXPERIEMENT -------------")
    origin = tusl.get_origin(84)
    # for i in range(100):
    #    print(tusl.get_origin(i))
    for i in range(100):
        print(tusl.search(i))




main()
