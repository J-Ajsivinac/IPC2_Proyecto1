import xml.etree.ElementTree as ET
from Matrix.mainMatrix import MainMatrix
from Nodes.linkedListP import LinkedList
from Alerts.customAlerts import Alert


class Read:
    def read_file(self, route):
        # lectura del XML
        self.tree = ET.parse(route)
        self.root = self.tree.getroot()

    def load_data(self):
        all_data = LinkedList()
        # recorre todo el arcivo y obtiene los elementos con la etiqueta senal
        for frecuency in self.root.findall("senal"):
            name_temp = frecuency.get("nombre")
            # creación de una matriz según lo indique el archivo XML
            # la matriz inicialmente es de solo ceros
            matrix_temp = MainMatrix(int(frecuency.get("t")), int(frecuency.get("A")))

            # verificación de nombres duplicados, si existen nombres duplicados
            # se sobreescriben
            if all_data.verify_dup(name_temp, matrix_temp):
                Alert(
                    "advertencia",
                    f"Se encontró una matriz con el mismo nombre: {name_temp}",
                )
                Alert("procesando", f"Sustituyendo: {name_temp}")
            else:
                # si no hay repetición se agrega con normalidad
                all_data.insert(name_temp, matrix_temp)
            # se recorre los elementos de la etiqueta senal, para cambiar los valores ceros iniciales
            for data in frecuency.findall("dato"):
                matrix_temp.update(
                    int(data.get("t")), int(data.get("A")), int(data.text)
                )
        Alert("exito", "Datos Cargados")
        return all_data
