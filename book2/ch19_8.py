import numpy as np

A = np.matrix([[2, 3],
               [5, 7]])
B = np.linalg.inv(A)
product_1 = A * B
product_2 = B * A

print(f"A_inv = {B}")
print(f"A * A_inv = {product_1}")
print(f"A_inv * A = {product_2}")
print(f"A * A_inv(round) = {product_1.round()}")
print(f"A_inv * A(round) = {product_2.round()}")

# A_inv = [[-7.  3.]
#          [ 5. -2.]]
# A * A_inv = [[ 1.00000000e+00 -4.44089210e-16]
#              [-7.10542736e-15  1.00000000e+00]]
# A_inv * A = [[ 1.00000000e+00 -8.88178420e-16]
#              [-1.33226763e-15  1.00000000e+00]]
# A * A_inv(round) = [[ 1. -0.]
#                     [-0.  1.]]
# A_inv * A(round) = [[ 1. -0.]
#                     [-0.  1.]]