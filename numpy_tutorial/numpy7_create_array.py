import numpy as np

a = np.array(([1, 2, 3], [4, 5, 6]), dtype=int)

print(a)

# membuat array dengan menggunakan function
b = np.array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
print(b)


def kuadrat(baris, kolom):
    return kolom**2


def jumlah(baris, kolom):
    return (kolom + baris)


print(kuadrat(1, 5))

# c = np.fromfunction(kuadrat, ukuran matrix, tipe)
c = np.fromfunction(kuadrat, (2, 8), dtype=int)
print(c)

d = np.fromfunction(jumlah, (4, 4), dtype=float)
print(d)

# membuat matrix atau array dengan menggunakan iterasi
iterable = (x*x for x in range(5))

e = np.fromiter(iterable, dtype=int)
print(f"Matrix dari iterable:\n {e}")

# multitype array: isinya campuran
dtipe = [('nama', 'S255'), ('tinggi', int)]  # s255 : max char
data = [('zoe', 160),
        ('jill', 160),
        ('sri', 165)]  # list
f = np.array(data, dtype=dtipe)

print(f"Array campuran: \n {f}")
