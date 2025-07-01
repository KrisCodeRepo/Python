import numpy as np

A = np.array([200, 17])
AT = A.T
print(A)
print(AT)
W = np.array([[1, 2], [3, 4], [5, 6]])
B = np.array([5, 6, 7])
Z = np.dot(W, A) + B     
print("Z:", Z)
sig = 1/ (1 + np.exp(-Z))
print("sigmoid:", sig)
