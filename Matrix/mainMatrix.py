from Matrix.linkedListMatrix import LinkedListMatrix


class MainMatrix:
    def __init__(self, rows=0, columns=0):
        self.rows = LinkedListMatrix()
        if rows < 0:
            return
        if columns < 0:
            return
        rows = 3600 if rows > 3600 else rows
        columns = 130 if columns > 130 else columns

        self.r = rows
        self.c = columns
        for i in range(1, rows + 1):
            row = LinkedListMatrix()
            # print(i)
            for j in range(1, columns + 1):
                row.insert(j, 0, 0)
            self.rows.insert(i, 0, row)

    def create(self, d_matrix):
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

    def update(self, row, column, new_v):
        if row > self.r or column > self.c:
            return
        current_row = self.rows.first
        for _ in range(row - 1):
            current_row = current_row.next_node
        # print(current_row.time)
        current_row.value.update_value(column, new_v)  # un row

    def m_patrons(self):
        matrix_clone = LinkedListMatrix()
        current_row = self.rows.first
        for i in range(1, self.r + 1):
            clone_row = current_row.value.clone(self.c)
            matrix_clone.insert(i, 0, clone_row)
            current_row = current_row.next_node
        ret = MainMatrix()
        ret.create(matrix_clone)
        return ret
