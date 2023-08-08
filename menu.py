class Menu:
    def menu(self):
        while True:
            self.options()
            option = input("Elija una Opción: ")
            if not option.isdigit():
                print("Ingrese solo números")
                continue
            if option == "1":
                pass
            elif option == "2":
                pass
            elif option == "3":
                pass
            elif option == "4":
                self.datos_estudiante()
            elif option == "5":
                pass
            elif option == "6":
                pass
            elif option == "7":
                break
            else:
                print("Opción Inválida")

    def datos_estudiante(self):
        print("Joab Israel Ajsivinac Ajsivinac")
        print("202200135")
        print('Introducción a la Programación y computación 2 Sección "N"')
        print("Ingenieria en Ciencias y Sistemas")
        print("4to Semestre")

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
