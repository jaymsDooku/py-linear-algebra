import vector


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

    def __str__(self):
        result = "["
        for r in range(self.rows):
            result += self.contents[r].__str__()
            if r < self.rows - 1:
                result += ",\n"
        result += "]"
        return result

    def clone(self):
        result = Matrix(self.rows, self.cols)
        result.contents = [[self.contents[r][c] for c in range(self.cols)] for r in range(self.rows)]
        return result

    def row(self, r):
        return self.contents[r]

    def set_row(self, r, new_row):
        self.contents[r] = new_row

    def col(self, c):
        return [self.contents[r][c] for r in range(self.rows)]

    def set_col(self, c, new_col):
        if self.rows != len(new_col):
            raise ValueError("New column incompatible size.")

        for r in range(self.rows):
            self.contents[r][c] = new_col[r]

    def set(self, r, c, v):
        self.contents[r][c] = v

    def get(self, r, c):
        return self.contents[r][c]

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
        for r in range(self.rows):
            for c in range(self.cols):
                if c < self.cols:
                    result.contents[r][c] = self.contents[r][c]
        return result

    def exchange(self, r1, r2):
        temp = self.contents[r2]
        self.contents[r2] = self.contents[r1]
        self.contents[r1] = temp

    def augment(self, other):
        if self.rows != other.rows:
            raise ValueError("Matrices must have equal rows to augment.")

        aug = self.adjust_cols(self.cols + other.cols)
        for c in range(other.cols):
            aug.set_col(self.cols + c, other.col(c))
        return aug

    def reduce(self, other):
        if isinstance(other, vector.Vector):
            other = other.to_matrix()

        aug = self.augment(other)

        def all_zeroes(row):
            for col in range(aug.cols):
                if aug.get(row, col) != 0:
                    return False
            return True

        pr = 0
        for c in range(self.cols):
            pivot = aug.get(pr, c) if pr < aug.rows else 0
            if pivot == 0:
                for r in range(c, aug.rows):
                    pivot = aug.get(r, c)
                    if pivot != 0:
                        aug.exchange(c, r)
                        break

            if pivot != 0:
                if pivot != 1:
                    for k in range(aug.cols):
                        aug.set(pr, k, (aug.get(pr, k) / pivot))
                    pivot = 1

            for r in range((pr + 1), aug.rows):
                ratio = aug.get(r, c)
                for k in range(aug.cols):
                    val = aug.get(r, k) - ratio * aug.contents[pr][k]
                    aug.set(r, k, val)

            for r in range((pr + 1), aug.rows):
                if all_zeroes(r) and r != aug.rows - 1:
                    for o in range(r + 1, aug.rows):
                        if not all_zeroes(o):
                            aug.exchange(r, o)
                            break

            pr += 1
            print(aug)

        return aug, pr

    def back_sub(self):
        aug = self.clone()

        for pr in range(aug.rows - 1, -1, -1):
            pivot = 0
            c = 0
            for k in range(aug.cols):
                if aug.get(pr, k) != 0:
                    pivot = aug.get(pr, k)
                    c = k
                    break

            if pivot != 0:
                for r in range(pr - 1, -1, -1):
                    ratio = aug.get(r, c)
                    if pivot != 1:
                        ratio /= pivot

                    for k in range(aug.cols):
                        val = aug.get(r, k) - ratio * aug.get(pr, k)
                        aug.set(r, k, val)

            print(aug)

        return aug

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
