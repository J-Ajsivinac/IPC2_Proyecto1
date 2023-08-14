from Nodes.nodePrincipal import Node


class LinkedList:
    def __init__(self):
        self.first = None
        self.size = 0

    def insert(self, name, d_matrix):
        if self.first is None:
            self.first = Node(name, d_matrix)
            self.size += 1
            return
        current = self.first
        while current.next_n:
            current = current.next_n
        current.next_n = Node(name, d_matrix)
        self.size += 1

    def print_e(self):
        current = self.first
        while current:
            current.matrix.display_matrix(current.name)
            current = current.next_n

    def verify_dup(self, name, d_matrix):
        current = self.first
        prev = None
        # print(self.size)
        if self.size == 0:
            return False

        while current and current.name != name:
            prev = current
            current = current.next_n

        temp = Node(name, d_matrix)
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

    def get_minim(self):
        if self.first is None:
            return None
        cloned_list = LinkedList()
        current_data = self.first
        while current_data:
            current_matrix = current_data.matrix
            # print(current_matrix)
            matrix_temp = current_matrix.m_patrons()
            cloned_list.insert(current_data.name, matrix_temp)
            current_data = current_data.next_n
        return cloned_list
