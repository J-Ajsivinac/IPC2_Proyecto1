# Nodo principal que guarda los datos de las señales de audio
class Node:
    def __init__(self, name, matrix):
        self.name = name
        self.matrix = matrix
        self.next_n = None
