class Node:
    def __init__(self, index=None, value=None, next_node=None):
        # index hace referencia a tanto filas y columnas
        self.index = index
        self.value = value
        self.next_node = next_node
