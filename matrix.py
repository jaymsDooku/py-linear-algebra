class Matrix:

    @staticmethod
    def identity(n):
        result = Matrix(n, n)
        for i in range(n):
            result.contents[i][i] = 1
        return result

    def __init__(self, rows, cols):
        self.rows = rows
        self.cols = cols
        self.contents = [[0 for c in range(cols)] for r in range(rows)]

    def row(self, r):
        return self.contents[r]

    def set_row(self, r, new_row):
        self.contents[r] = new_row

    def col(self, c):
        return [self.contents[r][c] for r in range(self.rows)]

    def set_col(self, c, new_col):
        for r in range(self.rows):
            self.contents[r][c] = new_col[r]

    def set(self, r, c, v):
        self.contents[r][c] = v

    def transpose(self):
        result = Matrix(self.rows, self.cols)
        result.contents = [[self.contents[r][c] for r in range(self.rows)] for c in range(self.cols)]
        return result

    def square(self):
        return self.rows == self.cols

    def symmetric(self):
        if not self.square():
            return False

        for r in range(self.rows):
            for c in range(self.cols):
                upper = self.contents[r][c]
                lower = self.contents[c][r]
                if upper != lower:
                    return False
        return True

    def upper_triangular(self):
        if not self.square():
            return False

        for r in range(1, self.rows):
            for c in range(r):
                if self.contents[r][c] != 0:
                    return False

        return True

    def lower_triangular(self):
        if not self.square():
            return False

        for r in range(self.rows):
            for c in range(r + 1, self.rows - r):
                if self.contents[r][c] != 0:
                    return False

        return True

    def adjust_cols(self, new_cols):
        result = Matrix(self.rows, new_cols)
        result.contents = [[self.contents[r][c] for c in range(self.cols)] for r in range(self.rows)]
        return result

    def augment(self, other):
        if self.rows != other.rows:
            raise ValueError("Matrices must have equal rows to augment.")

        aug = self.adjust_cols(self.cols + other.cols)
        for c in range(other.cols):
            aug.set_col(self.cols() + c, other.col(c))
        return aug

    def reduce(self, other):
        #aug = self.augment(other)
        pass

    def back_sub(self, reduced):
        pass

    def __mul__(self, other):
        if self.cols != other.rows:
            raise ValueError("Columns don't equal Rows of other matrix.")

        result = Matrix(self.rows, other.cols)

        for r in range(self.rows):
            for c in range(other.cols):
                row = self.row(r)
                col = other.col(c)
                inner_prod = sum([r * c for r, c in zip(row, col)])
                result.contents[r][c] = inner_prod

        return result
