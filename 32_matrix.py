import numpy as np
import sys

if __name__ == "__main__":
    """ Implement matrix.

    Two ways of getting matrix.
    1. Use standard lists (Note : Implement transpose and multiplication yourself ;-))
    2. Use numpy
    Move to numpy as it contains many more features for math
    """
    # 3x3 matrix
    A = [[1, 2, 3],
         [4, 5, 6],
         [7, 8, 9]]
    print("A : ", A)
    print("A[1] : ", A[1])
    # pay attention to the 0-based index of the list
    print("A[1][2] : ", A[1][2])
    # len on 2D Matrix works as expected
    print(len(A))
    # Add two matrices using nested loop

    B = [[9, 8, 7],
         [6, 5, 4],
         [3, 2, 1]]

    R = [[0, 0, 0],
         [0, 0, 0],
         [0, 0, 0]]

    # iterate through rows
    for i in range(len(A)):
        # iterate through columns
        for j in range(len(A[0])):
            R[i][j] = A[i][j] + B[i][j]
    for i in R:
        print(i)
    # use numpy
    x = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
    y = np.array([[9, 8, 7], [6, 5, 4], [3, 2, 1]])
    print("numpy element-wise op")
    print("x+y : \n", np.add(x, y))
    print("x*y : \n", np.multiply(x, y))
    print("sqrt(x): \n", np.sqrt(x))
    print("numpy matrix multiplication")
    print("np.dot(x,y): \n", np.dot(x, y))
    print("x.T: \n", x.T)
    print("np.zeros((2,3)) \n", np.zeros((2,3)))
    print("np.ones((3,3)) \n", np.ones((3,3)))
    print("row 1 of A", A[0])
    print("column 1 of A", A[0, :])
    # slicing works as expected in numpy arrays
    print(sys.path)
