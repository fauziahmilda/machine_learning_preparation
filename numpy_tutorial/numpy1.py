import numpy as np

# membuat vector
a = np.array([1, 2, 3, 4, 5])
b = np.array([1.5, 2.5, 5, 6, 7])

# membuat vector dengan range
c = np.arange(1, 10, 2)  # batas bawah, batas atas, step

# membuat linear space
d = np.linspace(1, 10, 4)  # batas bawah, batas atas, pembagi

# array multi dimensi atau matrix
e = np.array([(1, 2, 3), (4, 5, 6)])
e2 = e + 1

# matix dengan nilai nol
f = np.zeros(5)  # vektor
f2 = np.zeros((5, 5))  # matrix

# matix dengan nilai satu
g = np.ones(5)  # vektor
g2 = np.ones((5, 5))  # matrix

# matix identitas
h1 = np.identity(5)
h2 = np.eye(5)

# display
print(a)
print(b)
print(c)
print(d)
print(e)
print(e2)
print(f)
print(f2)
print(g)
print(g2)
print(h1)
print(h2)