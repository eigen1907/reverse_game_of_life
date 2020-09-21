import numpy as np

a = np.array([[0, 1, 2, 3], [4, 5, 6, 7], [8, 9, 10, 11], [12, 13, 14, 15]])

b = np.copy(a[1:3, 1:3])

print(a[2][2])