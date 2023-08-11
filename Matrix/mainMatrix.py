from Matrix.linkedListMatrix import LinkedListMatrix


class MainMatrix:
    def __init__(self, rows, columns):
        self.rows = LinkedListMatrix()
        self.r = rows
        self.c = columns
        for i in range(1, rows + 1):
            row = LinkedListMatrix()
            # print(i)
            for j in range(1, columns + 1):
                row.insert(j, 0, 0)
            self.rows.insert(i, 0, row)

    def display_matrix(self):
        current_row = self.rows.first
        while current_row:
            c_1 = current_row.value.first
            while c_1:
                print(str(c_1.value), end="\t")
                c_1 = c_1.next_node
            # print(current_row.time)
            print(" ")
            current_row = current_row.next_node

    def update(self, row, column, new_v):
        if row > self.r or column > self.c:
            return
        current_row = self.rows.first
        for _ in range(row - 1):
            current_row = current_row.next_node
        # print(current_row.time)
        current_row.value.update_value(column, new_v)  # un row
