class Matrix(object):
    def __init__(self, matrix_string):
        self.matrix_string = matrix_string
        self.rows_list = self.rows()

    def rows(self):
        if '\n' not in self.matrix_string:
            return [int(self.matrix_string)]
        else:
            rows_str = self.matrix_string.split('\n ')
            rows_l = [r.split(' ') for r in rows_str]
            return rows_l

    def row(self, index):
        return self.rows_list[index-1]

    def column(self, index):
        return [self.rows_list[i][index-1] for i in range(self.rows_list[0])]