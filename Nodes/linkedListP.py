from Nodes.nodePrincipal import Node


class LinkedList:
    def __init__(self):
        self.first = None
        self.size = 0

    def insert(self, name, data):
        if self.first is None:
            self.first = Node(name, data)
            return
        current = self.first
        while current.next_n:
            current = current.next_n
        current.next_n = Node(name, data)
        self.size += 1

    def print(self):
        current = self.first
        while current:
            print(current.matrix.display_matrix())
            current = current.next_n
