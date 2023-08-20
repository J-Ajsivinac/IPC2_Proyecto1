class NodeReduce:
    def __init__(self, group_name=None, index=None, value=None, next_node=None):
        # index hace referencia a tanto filas y columnas
        self.group_name = group_name
        self.index = index
        self.value = value
        self.next_node = next_node
