import numpy as np

a = np.arange(10)**2

print(a)

# mengambil nilai
print(f"Element ke 1 dari a adalah {a[0]}")
print(f"Element ke 7 dari a adalah {a[6]}")
print(f"Element terakhir dari a adalah {a[-1]}")

# slicing
# batas atas, batas sebelum akhir (enklusif)
print(f"Element dari 1-6 adalah {a[0:5]}")
print(f"Element dari 4-akhir adalah {a[3:]}")
print(f"Element dari 1-5 adalah {a[:5]}")

# iterasi
for i in a:
    print(f'value = {i}')
