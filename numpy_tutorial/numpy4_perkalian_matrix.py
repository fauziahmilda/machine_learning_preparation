import numpy as np


a = np.array(([1, 2], [4, 5]))
b = np.ones([2, 2])

print(f"matrix a:\n {a}")
print(f"matrix b:\n {b}")

# perkalian matrix
# cara pertama
c1 = np.dot(a, b)
c2 = a.dot(b)

print(f"hasil perkalian cara 1:\n {c1}")
print(f"hasil perkalian cara 2:\n {c2}")
