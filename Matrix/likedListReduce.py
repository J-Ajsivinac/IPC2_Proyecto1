from Matrix.nodeReduce import NodeReduce


class LinkedListReduce:
    def __init__(self):
        self.first = None
        self.size = 0

    def is_empty(self):
        return self.first is None

    # inserta valores a la lista
    def insert(self, name, row, value):
        new_value = NodeReduce(name, row, value)
        if self.is_empty():
            self.first = new_value
            self.size += 1
            return
        current = self.first
        while current.next_node:
            current = current.next_node
        current.next_node = new_value
        self.size += 1
