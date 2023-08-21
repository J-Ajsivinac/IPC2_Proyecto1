from Nodes.nodePrincipal import Node
from Matrix.mainMatrix import MainMatrix
from Alerts.customAlerts import Alert


class LinkedListPrincipal:
    def __init__(self):
        self.first = None
        self.size = 0

    # inserta señales de audio a la lista
    def insert(self, name, d_matrix):
        # ingreso de nodos cuando no hay datos
        if self.first is None:
            self.first = Node(name, d_matrix)
            self.size += 1
            return
        # recorriendo la lista para agregar el elemento al final
        current = self.first
        while current.next_n:
            current = current.next_n
        current.next_n = Node(name, d_matrix)
        self.size += 1

    def print_e(self):
        current = self.first
        while current:
            current.matrix.display_matrix(current.name)
            # print(current.matrix.r, current.matrix.c)
            current = current.next_n

    # verifica si el nombre de la señal esta duplicado
    # si está duplicado procede a sobreescribir el valor de la señal anterior
    def verify_dup(self, name, d_matrix):
        current = self.first
        prev = None
        if self.size == 0:
            return False

        # se recorre la lista para encontrar si hay una señal con el mismo nombre
        while current and current.name != name:
            prev = current
            current = current.next_n

        temp = Node(name, d_matrix)
        # si current es None entonces quiere decir que no se encontraron señales con el mismo nombre
        if not current:
            return False
        # si prev es none quiere decir que estamos reemplazando el primer elemento en la lista
        elif prev is None:
            self.first = temp
            temp.next_n = current.next_n
            current.next_n = None
            return True
        # se reemplazan cualquier nodo que no sea el primero
        else:
            # al elemento anterior se le apunta el nuevo valor
            prev.next_n = temp
            # el nuevo valor apunta al valor que estaba apuntando el valor repetido
            temp.next_n = current.next_n
            # el valor repetido antiguo se apunta a None, para quitarle el enlace a
            # la listas principal
            current.next_n = None
            return True

    # retorna la matriz binaria de todos las señales de audio existentes
    def get_binary(self):
        if self.first is None:
            return None
        cloned_list = LinkedListPrincipal()
        current_data = self.first
        while current_data:
            Alert("procesando", f"Calculando la matriz binaria de: {current_data.name}")
            current_matrix = current_data.matrix
            # llamada a la función m_patrons() para obtener la matriz con 1 y 0
            matrix_temp = current_matrix.m_patrons()
            # se inserta el valor de la fila al clon
            cloned_list.insert(current_data.name, matrix_temp)
            current_data = current_data.next_n
        return cloned_list
        # self.proces_all_m(cloned_list)

    def create_groups(self, matrix_o, all_groups):
        current = self.first
        current_o = matrix_o.first
        while current:
            Alert("procesando", f"Realizando suma de tuplas de: {current.name}")
            current_matrix: MainMatrix = current.matrix
            original_matrix: MainMatrix = current_o.matrix
            all_groups.insert(
                current.name, current_matrix.group_similar(original_matrix)
            )
            current = current.next_n
            current_o = current_o.next_n
