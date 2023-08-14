from Matrix.nodeMatrix import Node


class LinkedListMatrix:
    def __init__(self):
        self.first = None

    def is_empty(self):
        return self.first is None

    # inserta valores a la lista
    def insert(self, row, value):
        new_value = Node(row, value)
        if self.first is None:
            self.first = new_value
            return
        current = self.first
        while current.next_node:
            current = current.next_node
        current.next_node = new_value

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
