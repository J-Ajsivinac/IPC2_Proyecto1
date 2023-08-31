import graphviz
from Matrix.mainMatrix import MainMatrix
from Alerts.customAlerts import Alert


class Graph:
    def __init__(self, signal_name):
        self.signal_name = signal_name
        self.dot = graphviz.Digraph(
            f"{signal_name}",
            filename=f"{signal_name}.gv",
            node_attr={
                "shape": "box",
                "fontname": "Helvetica",
                "fillcolor": "#ffffff",
                "color": "#cec9f1",
                "style": "filled,rounded",
            },
            format="svg",
        )
        # self.dot.attr(dpi="500")

    # Crear grafico para la matriz Original
    def create_original(self, matrix: MainMatrix):
        self.dot.node(
            "root",
            label=f"{self.signal_name}",
            color="#7580f9",
            fontcolor="#ffffff",
            fillcolor="#7580f9",
        )
        self.dot.node("time", label=f"t={matrix.r}", group="1", color="#7580f9")
        self.dot.node("amplitude", label=f"A={matrix.c}", group="1", color="#7580f9")

        current_row = matrix.rows.first

        with self.dot.subgraph(name="cluster_1") as c:
            c.attr(style="rounded", color="#9d9bca", bgcolor="#eef1fa")
            for i in range(1, matrix.r + 1):
                current_data = current_row.value.first
                for j in range(1, matrix.c + 1):
                    c.node(f"{i}_{j}", label=f"{current_data.value}", group=f"{i}")
                    if i > 1:
                        last_i = i - 1
                        c.edge(f"{last_i}_{j}", f"{i}_{j}", color="#7475ae")
                    if j > 1 and i == 1:
                        last_j = j - 1
                        c.edge(
                            f"{i}_{last_j}", f"{i}_{j}", color="#7475ae", style="invis"
                        )
                    current_data = current_data.next_node
                current_row = current_row.next_node
            with c.subgraph() as s:
                s.attr(rank="same")
                for j in range(1, matrix.c + 1):
                    s.node(f"1_{j}")

        self.dot.edge("root", "time", color="#7580f9")
        self.dot.edge("root", "amplitude", color="#7580f9")

        for i in range(1, matrix.c + 1):
            self.dot.edge("root", f"1_{i}", color="#7580f9")
        value_r = self.generar()
        if value_r:
            Alert("exito", f"Gráfica de '{self.signal_name}' generada")

    # crear graficos para la matriz reducida
    def create_reduced(self, matrix: MainMatrix):
        self.dot.node(
            "root",
            label=f"{self.signal_name}\nreducida",
            color="#7580f9",
            fontcolor="#ffffff",
            fillcolor="#7580f9",
        )
        self.dot.node("amplitude", label=f"A={matrix.c}", group="1", color="#7580f9")

        current_row = matrix.rows.first

        with self.dot.subgraph(name="cluster_2") as c:
            c.attr(style="rounded", color="#9d9bca", bgcolor="#eef1fa")
            for i in range(1, matrix.r + 1):
                current_data = current_row.value.first
                for j in range(matrix.c + 1):
                    if j == 0:
                        c.node(
                            f"{i}_{j}",
                            label=f"g={current_row.group_name}\n(t={current_row.index})",
                            group=f"{i}",
                        )
                    else:
                        c.node(f"{i}_{j}", label=f"{current_data.value}", group=f"{i}")
                        current_data = current_data.next_node
                    if i > 1:
                        last_i = i - 1
                        c.edge(
                            f"{last_i}_{j}",
                            f"{i}_{j}",
                            color="#7475ae",
                        )
                    if j > 0 and i == 1:
                        last_j = j - 1
                        c.edge(
                            f"{i}_{last_j}", f"{i}_{j}", color="#7475ae", style="invis"
                        )
                current_row = current_row.next_node

            with c.subgraph() as s:
                s.attr(rank="same")
                for j in range(matrix.c + 1):
                    s.node(f"1_{j}")

        self.dot.edge("root", "amplitude", color="#7580f9")
        for i in range(matrix.c + 1):
            self.dot.edge("root", f"1_{i}", color="#7580f9")
        value_r = self.generar("_reducida")
        if value_r:
            Alert("exito", f"Gráfica reducida de '{self.signal_name}' generada")

    def generar(self, n_reduce=""):
        nombre = f"img/{self.signal_name}{n_reduce}.svg".replace("\\", "/")
        try:
            self.dot.render(outfile=nombre, format="svg")
        except Exception as exce:
            Alert("error", "En la generación de la gráfica")
            print(exce)
            return False
        return True
