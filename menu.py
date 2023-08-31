from Alerts.customAlerts import Alert
from read_files import Read
from Nodes.linkedListP import LinkedListPrincipal
from writeFile import Write
from graph import Graph
import os


class Menu:
    def __init__(self):
        self.signals = LinkedListPrincipal()
        self.signals_g = LinkedListPrincipal()

    def menu(self):
        while True:
            self.options()
            option = input("Elija una Opción: ")
            if not option.isdigit():
                Alert("error", "Ingrese solo númeroes enteros")
                continue

            if option == "1":
                self.load_xml()
            elif option == "2":
                self.procces_file()
            elif option == "3":
                self.create_XML()
            elif option == "4":
                self.show_student_data()
            elif option == "5":
                self.create_graph()
            elif option == "6":
                self.restore()
            elif option == "7":
                Alert("exito", "Cierre de Sesión")
                break
            else:
                Alert("error", "Opción Inválida")

    def options(self):
        print()
        print(
            " ╔════════════════════════════════════════════════════════════════════════╗"
        )
        print(
            " ║                             Proyecto 1                                 ║"
        )
        print(
            " ╠════════════════════════════════════════════════════════════════════════╣"
        )
        print(
            " ║                                                                        ║"
        )
        print(
            " ║                        \033[34mMenú Principal\033[0m                                  ║"
        )
        print(
            " ║                     1. Cargar Archivo                                  ║"
        )
        print(
            " ║                     2. Procesar Archivo                                ║"
        )
        print(
            " ║                     3. Escribir Archivo de Salida                      ║"
        )
        print(
            " ║                     4. Mostrar datos del Estudiante                    ║"
        )
        print(
            " ║                     5. Generar Gráfica                                 ║"
        )
        print(
            " ║                     6. Inicializar Sistema                             ║"
        )
        print(
            " ║                     7. Salida                                          ║"
        )
        print(
            " ║                                                                        ║"
        )
        print(
            " ╚════════════════════════════════════════════════════════════════════════╝\n"
        )

    def titles(self, title):
        print()
        print(" ╔═══════════════════════════════════════════════════════╗")
        print(" ║", end="")
        print(" %-53s" % title, end="")
        print(" ║")
        print(" ╚═══════════════════════════════════════════════════════╝\n")

    def verfy_size(self):
        if self.signals.size == 0:
            Alert("error", "No hay datos cargados")
            return True
        return False

    def load_xml(self):
        self.titles(" Cargar Archivo")
        url = input(" 📂 Ingrese la ruta del Archivo: ")
        _, extension = os.path.splitext(url)
        # verificación de que la ruta sea válida
        # No cadena vacia o elementos distintos a los .xml
        if url == "" or extension != ".xml":
            print(" ")
            Alert("error", "Ingrese una ruta válida")
            return
        print()
        url = url.replace("\\", "/")
        if not os.path.exists(url):
            print(" ")
            Alert(
                "error",
                f"No se encontro ningún archivo con el nombre {os.path.basename(url)}",
            )
            return
        read = Read()
        read.read_file(url)
        read.load_data(self.signals)
        # self.show_signals()

    def procces_file(self):
        if self.verfy_size():
            return

        self.titles(" Procesar Archivo")
        matrix_m = self.signals.get_binary()
        matrix_m.create_groups(self.signals, self.signals_g)
        # self.signals_g.print_e()
        Alert("exito", "Datos Procesados")

    def create_XML(self):
        if self.verfy_size():
            return

        self.titles(" Escribir Archivo de Salida")
        url = input(" 📂 Ingrese la ruta de destino, junto con el nombre y extensión : ")
        name, extension = os.path.splitext(url)
        if url == "" or extension != ".xml":
            print(" ")
            Alert("error", "Ingrese una ruta válida")
            return
        print()
        url = url.replace("\\", "/")
        Alert("procesando", "Creando archivo de salida")
        w = Write(url)
        w.write_document(self.signals_g)
        Alert("exito", "Archivo de Salida Creado/Actualizado")

    def show_student_data(self):
        self.titles(" Datos del Alumno")
        print("\t 🙍‍♂️ Joab Israel Ajsivinac Ajsivinac")
        print("\t 🆔 202200135")
        print('\t 📚 Introducción a la Programación y computación 2 Sección "N"')
        print("\t 💻 Ingenieria en Ciencias y Sistemas")
        print("\t 📆 4to Semestre")

    def create_graph(self):
        if self.verfy_size():
            return

        self.titles(" Generar Gráfica")
        signal_select = self.signals.select_signal()
        Alert("procesando", f"Generando gráfica de {signal_select.name}")
        graph_entry = Graph(signal_select.name)
        graph_entry.create_original(signal_select.matrix)

        if self.signals_g.size != 0:
            Alert(
                "procesando",
                f"Generando gráfica reducida de {signal_select.name}",
            )
            signal_g_select = self.signals_g.get_data_signal(signal_select.name)
            graph_groups = Graph(signal_select.name)
            graph_groups.create_reduced(signal_g_select.matrix)

    def restore(self):
        self.titles(" Inicializr Sistema")
        self.signals.empty_list()
        self.signals_g.empty_list()
        Alert("exito", "Se inicializo el sistema")

    def show_signals(self):
        self.signals.print_e()
