import xml.etree.ElementTree as ET
from Matrix.mainMatrix import MainMatrix
from Alerts.customAlerts import Alert


class Read:
    def read_file(self, route):
        # lectura del XML
        self.tree = ET.parse(route)
        self.root = self.tree.getroot()

    def load_data(self, all_data):
        # recorre todo el arcivo y obtiene los elementos con la etiqueta senal
        Alert("procesando", "Leyendo datos del XML")
        for frecuency in self.root.findall("senal"):
            name_temp = frecuency.get("nombre")

            if not frecuency.get("t").isdigit() or not frecuency.get("A").isdigit():
                Alert(
                    "error",
                    f"No se puede agregar la señal {name_temp}, porque el parámetro t o A no son enteros",
                )
                continue

            time_max = int(frecuency.get("t"))
            amplitude_max = int(frecuency.get("A"))
            if time_max <= 0:
                Alert(
                    "error",
                    f"No se puede agregar la señal {name_temp}, porque el tiempo <= 0",
                )
                continue

            if amplitude_max <= 0:
                Alert(
                    "error",
                    f"No se puede agregar la señal {name_temp}, porque la amplitud > 0",
                )
                continue
            # creación de una matriz según lo indique el archivo XML
            # la matriz inicialmente es de solo ceros

            matrix_temp = MainMatrix(time_max, amplitude_max)

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
                if data.text is None:
                    continue
                if (
                    not data.text.isdigit()
                    or not data.get("t").isdigit()
                    or not data.get("A").isdigit()
                ):
                    continue
                matrix_temp.update(
                    int(data.get("t")), int(data.get("A")), int(data.text)
                )
        Alert("exito", "Datos Cargados")
