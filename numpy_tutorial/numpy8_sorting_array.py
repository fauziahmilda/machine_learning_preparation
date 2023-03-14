import numpy as np

a = np.floor(np.random.randn(1, 6)*10)  # generate random array
print(f"Random array: \n {a}")
print("-------------------------------------")
print(f"Nilai max dari a:\n {a.max()}")
print(f"Posisi index nilai max:\n {a.argmax()}")
print("-------------------------------------")
print(f"Nilai min dari a:\n {a.min()}")
print(f"Posisi index nilai min:\n {a.argmin()}")
print("-------------------------------------")

# cara mengurutkan
print("Mengurutkan nilai a dari kecil ke besar:")
print(np.sort(a))
print("-------------------------------------")

# mengurutkan berdaraskan argumen
print("Mengurutkan dari argumen")
print(np.argsort(a))
print("-------------------------------------")


# untuk 2 DIMENSI
b = np.floor(np.random.randn(2, 2)*10)

print(f"Dua dimensi:\n {b}")


# multitype array: isinya campuran -- disort
dtipe = [('nama', 'S255'), ('tinggi', int)]  # s255 : max char
data = [('zoe', 160),
        ('jill', 150),
        ('sri', 165)]  # list
f = np.array(data, dtype=dtipe)

print(f"Array campuran: \n {f}")
print(f"Seteleh disort berdasarkan tinggi")
print(np.sort(f, order='tinggi'))
print(f"Seteleh disort berdasarkan nama")
print(np.sort(f, order='nama'))
