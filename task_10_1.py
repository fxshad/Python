from typing import List


class Matrix:
    def __init__(self, matrix: List[List[int]]):
        self.matrix = matrix

        for i in self.matrix:
            if len(i) != len(self.matrix[0]):
                raise ValueError('fail initialization matrix')


    def __str__(self):
        new_mtrx = ""
        for i in self.matrix:
            new_mtrx += "| "
            for n in i:
                new_mtrx += f"{n} "
            new_mtrx += "|\n"
        return new_mtrx


    def __add__(self, other):
        for i in range(len(self.matrix)):
            for n in range(len(self.matrix[i])):
                self.matrix[i][n] = (self.matrix[i][n] + other.matrix[i][n])
        return Matrix(self.matrix)



if __name__ == '__main__':
    first_matrix = Matrix([[1, 2], [3, 4], [5, 6]])
    second_matrix = Matrix([[6, 5], [4, 3], [2, 1]])

    print(first_matrix)

    """
    | 1 2 |
    | 3 4 |
    | 5 6 |
    """

    print(first_matrix + second_matrix)

    """
    | 7 7 |
    | 7 7 |
    | 7 7 |
    """
    fail_matrix = Matrix([[1, 2], [3, 4, 7], [5, 6]])
    """
    Traceback (most recent call last):
      ...
    ValueError: fail initialization matrix
    """

