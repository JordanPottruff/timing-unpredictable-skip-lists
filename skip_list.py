import random

class SkipList:

    def __init__(self):
        self.start_node, self.end_node = bounding_nodes()
        self.nodes = [self.start_node, self.end_node]

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

    def insert(self, value: float):
        # Start search at head (should have value -inf).
        current = self.nodes[0]
        height = current.height

        prev_nodes = []

        while True:
            next_node = current.next_nodes[height]

            if value < next_node.value:
                prev_nodes.insert(0, current)
                if height == 0:
                    self.__insert_into_path(prev_nodes, value)
                    return

                # Need to go to a lower level, but keep track of this node for when
                # we generate the inserted node in the future.
                height -= 1

            elif value > next_node.value:
                current = next_node
            else:
                print("Value already in list!")

    def __insert_into_path(self, prev_nodes, value):
        height = random_height()
        new_node = Node(value, height, [])

        for i in range(height+1):
            if i > self.start_node.height:
                self.start_node.add_next_node(new_node)
                new_node.add_next_node(self.end_node)
                self.start_node.height = i
                self.end_node.height = i
            else:
                next_node = prev_nodes[i].next_nodes[i]

                new_node.add_next_node(next_node)
                prev_nodes[i].next_nodes[i] = new_node

        self.nodes.insert(self.nodes.index(prev_nodes[0])+1, new_node)


class Node:

    def __init__(self, value: float, height: int, next_nodes: list):
        self.value = value
        self.height = height
        self.next_nodes = next_nodes

    def __str__(self):
        return "val: {}, height: {}, next_nodes: {}".format(self.value, self.height, str(self.next_nodes))

    def add_next_node(self, node):
        self.next_nodes.append(node)


def bounding_nodes():
    positive_inf_node = Node(float('inf'), 0, [])
    negative_inf_node = Node(float('-inf'), 0, [positive_inf_node])
    return negative_inf_node, positive_inf_node


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

main()