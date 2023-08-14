import xml.etree.ElementTree as ET
from Matrix.mainMatrix import MainMatrix
from Nodes.linkedListP import LinkedList
from Alerts.customAlerts import Alert


class Read:
    def read_file(self, route):
        self.tree = ET.parse(route)
        self.root = self.tree.getroot()
        # print(self.root.tag)

    def load_data(self):
        all_data = LinkedList()
        for frecuency in self.root.findall("senal"):
            name_temp = frecuency.get("nombre")
            matrix_temp = MainMatrix(int(frecuency.get("t")), int(frecuency.get("A")))
            # verify =
            # print(name_temp)
            if all_data.verify_dup(name_temp, matrix_temp):
                Alert(
                    "advertencia",
                    f"Se encontró una matriz con el mismo nombre: {name_temp}",
                )
                Alert("procesando", f"Sustituyendo: {name_temp}")
            else:
                all_data.insert(name_temp, matrix_temp)
                # print(".")
            for data in frecuency.findall("dato"):
                # print(data.text)
                matrix_temp.update(
                    int(data.get("t")), int(data.get("A")), int(data.text)
                )
        Alert("exito", "Datos Cargados")
        return all_data
