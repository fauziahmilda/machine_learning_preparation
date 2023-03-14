import numpy as np


a = np.array([1, 3])
b = np.array([2, 1])

# perkalian dot, skalar = |a| . |b| . cos teta
hasil_dot = np.dot(a, b)

print(f"Hasil perkalian vektor atau dot, {a} dengan {b}:\n {hasil_dot}")

# perkalian cross = a x b = |a| . |b| . sin teta = c
# ada arahnya

x = np.array([1, 2, 0])
y = np.array([2, 1, 0])

hasil_cross1 = np.cross(x, y)
hasil_cross2 = np.cross(y, x)

print(f"Hasil cross {x} dan {y}:\n {hasil_cross1}")
print(f"Hasil cross {y} dan {x}:\n {hasil_cross2}")
