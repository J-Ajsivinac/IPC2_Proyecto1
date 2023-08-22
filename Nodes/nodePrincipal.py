# Nodo principal que guarda los datos de las señales de audio
class Node:
    def __init__(self, name, matrix, processed=False):
        self.name = name
        self.processed = processed
        self.matrix = matrix
        self.next_n = None
