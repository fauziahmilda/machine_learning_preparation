import numpy as np

# untuk menyelesaikan persamaan linier

# invers matrix
# a = np.array(([1, 2], [3, 4]))
a = np.array([[1, -1], [1, 1]])

print(f"Matrix a: \n {a}")

a_inv = np.linalg.inv(a)

print(f"Invers matrix a:\n {a_inv}")

bukti = np.dot(a, a_inv)

print(f"Hasil pembuktian:\n {np.floor(bukti)}")

# determinan matrix
a_det = np.linalg.det(a)
a_det_inv = np.linalg.det(a_inv)

print(f"Determinan dari a:\n {a_det}")
print(f"Determinan dari a invers:\n {a_det_inv}")
