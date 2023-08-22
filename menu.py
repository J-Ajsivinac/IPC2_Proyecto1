from Alerts.customAlerts import Alert
from read_files import Read
from Nodes.linkedListP import LinkedListPrincipal
from writeFile import Write
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
                pass
            elif option == "6":
                pass
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

    def load_xml(self):
        self.titles(" Cargar Archivo")
        url = input(" 📂 Ingrese la ruta del Archivo: ")
        name, extension = os.path.splitext(url)
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
        self.show_signals()

    def procces_file(self):
        if self.signals.size == 0:
            Alert("error", "No hay datos cargados")
            return
        self.titles(" Procesar Archivo")
        matrix_m = self.signals.get_binary()
        # matrix_m.print_e()
        matrix_m.create_groups(self.signals, self.signals_g)
        self.signals_g.print_e()

    def create_XML(self):
        self.titles(" Escribir Archivo de Salida")
        url = input(" 📂 Ingrese la ruta del archivo, con nombre : ")
        name, extension = os.path.splitext(url)
        if url == "" or extension != ".xml":
            print(" ")
            Alert("error", "Ingrese una ruta válida")
            return
        print()
        url = url.replace("\\", "/")
        w = Write(url)
        w.write_document(self.signals_g)

    def show_student_data(self):
        self.titles(" Datos del Alumno")
        print("\t 🙍‍♂️ Joab Israel Ajsivinac Ajsivinac")
        print("\t 🆔 202200135")
        print('\t 📚 Introducción a la Programación y computación 2 Sección "N"')
        print("\t 💻 Ingenieria en Ciencias y Sistemas")
        print("\t 📆 4to Semestre")

    def show_signals(self):
        self.signals.print_e()
