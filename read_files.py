import xml.etree.ElementTree as ET
from Matrix.mainMatrix import MainMatrix
from Nodes.linkedListP import LinkedList


class Read:
    def __init__(self):
        self.all_data = LinkedList()

    def read_file(self, route):
        self.tree = ET.parse(route)
        self.root = self.tree.getroot()
        print(self.root.tag)

    def load_data(self):
        for frecuency in self.root.findall("senal"):
            temp_m = MainMatrix(int(frecuency.get("t")), int(frecuency.get("A")))
            self.all_data.insert(frecuency.get("nombre"), temp_m)
            for data in frecuency.findall("dato"):
                # print(data.text)
                temp_m.update(int(data.get("t")), int(data.get("A")), int(data.text))

    def imprimir(self):
        self.all_data.print()


# ruta = Read()
# ruta.read_file("entrada.xml")
# ruta.load_data()
# ruta.imprimir()
