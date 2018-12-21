import numpy as np

# on shapes, reshape
mat_1 = np.arange(2, 20, 2.5, float)
print mat_1
print "mat_1.shape: \n", mat_1.shape


# reshape to 2d
mat_2 = mat_1.reshape(2, 4)
print "mat_2.shape: \n", mat_2.shape
print mat_2

# reshape as 3d
mat_3 = mat_1.reshape(2, 2, 2)
print "mat_3.shape: \n", mat_3.shape
print mat_3

# print np.__version__
# random matrix
mat_rand = np.empty((5, 6))
print "mat_rand \n", mat_rand

# identity matrix
mat_eye = np.eye(7)
print "mat_eye \n", mat_eye

# zero matrix
mat_zero = np.zeros((4, 5))
print "mat_zero \n", mat_zero

