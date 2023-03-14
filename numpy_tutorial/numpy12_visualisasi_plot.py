import numpy as np
import matplotlib.pyplot as plt

# persamaan garis
# y = 2x + 3

x = np.arange(1, 10, 1)  # dari 1 - 10, dengan stepnya 1
y = 2*x + 3
print(f"Array x: \n {x}")
print(f"Array y: \n {y}")

plt.figure(1)  # membuat figure
plt.plot(x, y)


# membuat lingkaran

jari2 = 5

sudut = np.linspace(0, 2*np.pi, 100)
x2 = jari2*np.cos(sudut)
y2 = jari2*np.sin(sudut)

plt.figure(2)  # membuat figure
plt.plot(x2, y2)

# tampilkan
plt.show()
