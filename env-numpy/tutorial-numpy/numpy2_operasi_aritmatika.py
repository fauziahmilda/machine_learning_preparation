import numpy as np

# list
a = [1, 2, 3, 4, 5]
b = [6, 7, 8, 9, 10]

anp = np.array([1, 2, 3, 4, 5])
bnp = np.array([6, 7, 8, 9, 10])

# penjumlahan
hasil = a + b
hasil_np = anp + bnp

# pengurangan
# hasil2 = a-b  # tidak bisa
hasil_np2 = anp - bnp  # bisa

# perkalian
# hasil3 = a*b  # tidak bisa
hasil_np3 = anp * bnp  # bisa

# pembagian
# hasil3 = a/b  # tidak bisa
hasil_np4 = anp / bnp  # bisa

# kuadrat
hasil_np5 = anp**2

# ----------------------------
c = np.array(([1, 2, 3], [4, 5, 6]))
d = np.array(([7, 8, 9], [-1, -2, -3]))

hasilcd = c + d

print(hasil)  # menambahkan urutan dibelakang array
print(hasil_np)  # saling menambahkan dengan element yang indexnya sama

print("------------------------")

print(f"pengurangan: {hasil_np2}")

print("------------------------")

print(f"perkalian: {hasil_np3}")

print("------------------------")

print(f"pembagian: {hasil_np4}")

print("------------------------")

print(f"kuadrat: {hasil_np5}")

print("------------------------")

print(f"penjumlahan matrix:\n {hasilcd}")
