from Matrix.nodeMatrix import Node


class LinkedListMatrix:
    def __init__(self):
        self.first = None
        self.size = 0

    def is_empty(self):
        return self.first is None

    # inserta valores a la lista
    def insert(self, row, value):
        new_value = Node(row, value)
        if self.is_empty():
            self.first = new_value
            self.size += 1
            return
        current = self.first
        while current.next_node:
            current = current.next_node
        current.next_node = new_value
        self.size += 1

    def delete_row(self, index):
        current = self.first
        last = None

        while current and current.index != index:
            last = current
            current = current.next_node

        if not last:
            self.first = current.next_node
            current.next_node = None
            self.size -= 1
        elif current:
            last.next_node = current.next_node
            current.next_node = None
            self.size -= 1

    # muestara los valores actuales en consola
    def display(self):
        current = self.first
        while current:
            print(current.value, end="\t")
            current = current.next_node
        print()

    # se encarga de cambiar el valor de un elemento según la columna que se le pase
    def update_value(self, column, new_value):
        current = self.first
        while current:
            if current.index == column:
                if new_value != 0:
                    current.value = new_value
                break
            current = current.next_node

    # regresa la matriz binaria necesaria para agrupar
    def binary(self, size):
        original = self.first
        clone = LinkedListMatrix()
        for i in range(1, 1 + size):
            if original.value != 0:
                clone.insert(i, 1)
            else:
                clone.insert(i, 0)
            original = original.next_node
        return clone

    def __eq__(self, value_comp):
        current = self.first
        current_value_comp = value_comp.first
        while current:
            if current.value != current_value_comp.value:
                return False
            current = current.next_node
            current_value_comp = current_value_comp.next_node
        return True

    def get_row(self):
        current = self.first
        row_copy = LinkedListMatrix()
        while current:
            row_copy.insert(current.index, current.value)
            current = current.next_node
        return row_copy

    def __add__(self, other):
        current = self.first
        current_other = other.first
        row = LinkedListMatrix()
        i = 1
        while current:
            current.value += current_other.value
            row.insert(i, current.value)
            i += 1
            current = current.next_node
            current_other = current_other.next_node
        return row

    def empty_list(self):
        self.first = None
        self.size = 0
