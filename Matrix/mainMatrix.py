from Matrix.linkedListMatrix import LinkedListMatrix
from Alerts.customAlerts import Alert
from Matrix.likedListReduce import LinkedListReduce


# clase que se encarga del manejo de la matriz
class MainMatrix:
    # Para agregar la matriz inicial se pasan los parametros rows, y columns
    # si es para la creación de la matriz binaria no se pasan los parametros
    def __init__(self, rows=0, columns=0):
        self.rows = LinkedListMatrix()
        rows = 3600 if rows >= 3600 else rows
        columns = 130 if columns >= 130 else columns
        self.r = rows
        self.c = columns
        for i in range(1, rows + 1):
            # creación de una lista que guarde todos los datos de 1 sola fila
            row = LinkedListMatrix()
            # print(i)
            for j in range(1, columns + 1):
                # inserta ceros según el tamaño de columans pasadas
                row.insert(j, 0)
            # se inserta la fila a la lista que guarda las filas
            self.rows.insert(i, row)

    # crea una matriz que tenga las propiedades de mainMatrix
    # pasando como parametro la matriz base
    def create(self, d_matrix, rows, columns):
        self.r = rows
        self.c = columns
        self.rows = d_matrix

    def display_matrix(self, name):
        current_row = self.rows.first
        print(name)
        while current_row:
            c_1 = current_row.value.first
            while c_1:
                print(str(c_1.value), end="\t")
                c_1 = c_1.next_node
            # print(current_row.time)
            print(" ")
            current_row = current_row.next_node
        print(" ")

    # cambia los valores iniciales (0) por los valores que estan en el archivo de entrada
    def update(self, row, column, new_v):
        if row > self.r or column > self.c or row <= 0 or column <= 0:
            return
        # se obtiene la primera fila
        current_row = self.rows.first
        for _ in range(row - 1):
            # current_row contiene la fila a la cual le debemos cambiar el valor
            current_row = current_row.next_node
        # se cambia el valor según la fila y columna, la fila se obtuvo en el for
        current_row.value.update_value(column, new_v)  # un row

    # crea y retorn la matriz minimizada
    def m_patrons(self):
        matrix_b = LinkedListMatrix()
        current_row = self.rows.first
        for i in range(1, self.r + 1):
            # obtiene una fila pero ya solo con unos o ceros
            clone_row = current_row.value.binary(self.c)
            # se inserta el valor de la fila a la matriz
            matrix_b.insert(i, clone_row)
            current_row = current_row.next_node
        # ret contiene a la matriz que es una lista sin propiedades de mainMatrix
        matrix_ret = MainMatrix()
        # crea la matriz para que pueda usar los metodos de mainMatrix
        matrix_ret.create(matrix_b, self.r, self.c)
        return matrix_ret
        # self.group_similar(matrix_b=)

    def search_row(self, index):
        current = self.rows.first
        while current:
            if current.index == index:
                break
            current = current.next_node
        return current.value

    def get_row_add(self, row):
        current_row = self.rows.first
        for _ in range(row - 1):
            # current_row contiene la fila a la cual le debemos cambiar el valor
            current_row = current_row.next_node
        return current_row

    def group_similar(self, matrix_original):
        current_row = self.rows.first
        current_row_matrix = matrix_original.rows.first
        matrix_reduce = LinkedListReduce()
        for i in range(1, self.r + 1):
            if not current_row:
                continue
            comp_row = current_row.next_node
            row_temp = matrix_original.search_row(current_row.index)

            # print(row_temp)  # linkedlistMatrix
            # print(f"comp {comp_row.value}")  # matrix node
            times = f"{i}"
            name_group = f"{i}"
            for _ in range(i + 1, self.r + 1):
                if not current_row or not comp_row:
                    continue

                temp = None

                if current_row.value == comp_row.value:
                    times += f",{comp_row.index}"
                    row_temp += matrix_original.search_row(comp_row.index)
                    temp = comp_row.next_node
                    self.rows.delete_row(comp_row.index)

                if not comp_row.next_node:
                    comp_row = temp
                else:
                    comp_row = comp_row.next_node

            matrix_reduce.insert(name_group, times, row_temp)
            temp2 = current_row.next_node
            current_row_matrix = current_row_matrix.next_node
            self.rows.delete_row(current_row.index)
            current_row = temp2

        matrix_ret = MainMatrix()
        matrix_ret.create(matrix_reduce, self.r, self.c)

        return matrix_ret
