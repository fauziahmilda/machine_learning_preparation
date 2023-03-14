import numpy as np

a = np.array(([2, 3], [1, 2]))
y = np.array(([23], [14]))

# y = a * x
# x = a^-1 * y

print(f"Matrix a: \n {a}")
print(f"Matrix y: \n {y}")

a_inv = np.linalg.inv(a)
print(f"Matrix a invers: \n {a_inv}")

# menyelesaikan persamaan linear
x1 = np.dot(a_inv, y)
print(f"x = a^-1 * y, dengan hasil \n {x1}")

# cara lain
x2 = np.linalg.solve(a, y)
print(f"x = a^-1 * y, dengan hasil \n {x2}")
