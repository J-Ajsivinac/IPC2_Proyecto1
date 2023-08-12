from Nodes.nodePrincipal import Node


class LinkedList:
    def __init__(self):
        self.first = None
        self.size = 0

    def insert(self, name, data):
        if self.first is None:
            self.first = Node(name, data)
            self.size += 1
            return
        current = self.first
        while current.next_n:
            current = current.next_n
        current.next_n = Node(name, data)
        self.size += 1

    def print_e(self):
        current = self.first
        # print(current)
        while current:
            current.matrix.display_matrix()
            current = current.next_n

    def verify_dup(self, name, data):
        current = self.first
        prev = None
        # print(self.size)
        if self.size == 0:
            return False

        while current and current.name != name:
            prev = current
            current = current.next_n

        temp = Node(name, data)
        if not current:
            return False
        elif prev is None:
            self.first = temp
            temp.next_n = current.next_n
            current.next_n = None
            return True
        else:
            prev.next_n = temp
            temp.next_n = current.next_n
            current.next_n = None
            return True

        return False
