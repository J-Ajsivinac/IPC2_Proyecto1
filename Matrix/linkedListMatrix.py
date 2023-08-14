from Matrix.nodeMatrix import Node


class LinkedListMatrix:
    def __init__(self):
        self.first = None

    def is_empty(self):
        return self.first is None

    def insert(self, row, column, value):
        new_value = Node(row, column, value)
        if self.first is None:
            self.first = new_value
            return
        current = self.first
        while current.next_node:
            current = current.next_node
        current.next_node = new_value

    def display(self):
        current = self.first
        while current:
            print(current.value, end="\t")
            current = current.next_node
        print()

    def update_value(self, column, new_value):
        current = self.first
        while current:
            if current.time == column:
                current.value = new_value
                break
            current = current.next_node

    def clone(self, size):
        original = self.first
        clone = LinkedListMatrix()
        for i in range(1, 1 + size):
            if original.value != 0:
                clone.insert(i, 0, 1)
            else:
                clone.insert(i, 0, 0)
            original = original.next_node
        return clone
