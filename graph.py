import graphviz
from Nodes.nodePrincipal import Node
from Matrix.mainMatrix import MainMatrix


class Graph:
    def __init__(self, signal_name):
        self.signal_name = signal_name
        self.dot = graphviz.Digraph(
            f"{signal_name}",
            filename=f"{signal_name}.gv",
            node_attr={"shape": "box"},
            format="svg",
        )
        # self.dot.attr(dpi="500")

    def create_original(self, matrix: MainMatrix):
        self.dot.node("root", label=f"{self.signal_name}")
        self.dot.node("time", label=f"t={matrix.r}", group="1")
        self.dot.node("amplitude", label=f"A={matrix.c}", group="1")

        current_row = matrix.rows.first

        with self.dot.subgraph(name="custer") as c:
            for i in range(1, matrix.r + 1):
                current_data = current_row.value.first
                for j in range(1, matrix.c + 1):
                    c.node(f"{i}{j}", label=f"{current_data.value}", group=f"{i}")
                    if i > 1:
                        last_i = i - 1
                        c.edge(f"{last_i}{j}", f"{i}{j}")
                    current_data = current_data.next_node
                current_row = current_row.next_node

        self.dot.edge("root", "time")
        self.dot.edge("root", "amplitude")

        for i in range(1, matrix.c + 1):
            self.dot.edge("root", f"1{i}")
        self.generar()

    def create_reduced(self, matrix: MainMatrix):
        self.dot.node("root", label=f"{self.signal_name} reducida")
        self.dot.node("amplitude", label=f"A={matrix.c}", group="1")

        current_row = matrix.rows.first

        with self.dot.subgraph(name="custer") as c:
            for i in range(1, matrix.r + 1):
                current_data = current_row.value.first
                for j in range(matrix.c + 1):
                    print(current_data.value)
                    if j == 0:
                        c.node(
                            f"{i}{j}",
                            label=f"g={current_row.group_name} (t={current_row.index})",
                            group=f"{i}",
                        )
                    else:
                        c.node(f"{i}{j}", label=f"{current_data.value}", group=f"{i}")
                        current_data = current_data.next_node
                    if i > 1:
                        last_i = i - 1
                        c.edge(f"{last_i}{j}", f"{i}{j}")

                current_row = current_row.next_node

        self.dot.edge("root", "amplitude")
        for i in range(matrix.c + 1):
            self.dot.edge("root", f"1{i}")
        self.generar("_reducida")

    def generar(self, n_reduce=""):
        nombre = f"img/{self.signal_name}{n_reduce}.svg".replace("\\", "/")
        self.dot.render(outfile=nombre, format="svg")
