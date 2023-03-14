import numpy as np

a = np.array([1, 2, 3])
b = np.array([4, 5, 6])
aMat = np.zeros((2, 3))
bMat = np.ones((2, 3))

# stacking matrix, menumpuk matrix

c1 = np.hstack((a, b))
c2 = np.vstack((a, b))
cMat1 = np.hstack((aMat, bMat))
cMat2 = np.vstack((aMat, bMat))

# array stack
print(f"Horizontal array :\n {c1}")
print(f"Vertikal array :\n {c2}")

# matrix stack
print(f"Horizontal matrix :\n {cMat1}")
print(f"Vertikal matrix :\n {cMat2}")
