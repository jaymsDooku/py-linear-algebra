from matrix import Matrix


def main():
    a = Matrix(2, 3)
    a.set_row(0, [1, 2, 3])
    a.set_row(1, [3, 2, 1])
    print("a: ", a.contents)

    b = Matrix(3, 2)
    b.set_col(0, [0, 1, 0])
    b.set_col(1, [2, -1, 1])
    print("b: ", b.contents)

    ab = a * b
    print("ab: ", ab.contents)
    ba = b * a
    print("ba: ", ba.contents)

    at = a.transpose()
    print("at: ", at.contents)
    bt = b.transpose()
    print("bt: ", bt.contents)

    i = Matrix.identity(3)
    print("i: ", i.contents)
    print("symmetric: ", i.symmetric())
    print("upper triangular: ", i.upper_triangular())
    print("lower triangular: ", i.lower_triangular())


if __name__ == '__main__':
    main()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
