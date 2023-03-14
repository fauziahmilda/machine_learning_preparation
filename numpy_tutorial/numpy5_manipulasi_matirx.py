import numpy as np

# matrix
a = np.array(([1, 2, 3],
              [4, 5, 6]))

print(f"matrix a dengan ukuran {a.shape}")
print(a)

# transpose
print("Transpose matrix a:")
print(a.transpose())
print(np.transpose(a))
print(a.T)

# flatten: menjadi vector baris
print("Flatten matrix a:")
flatten = a.ravel()
print(a.ravel())
print(np.ravel(a))
print(flatten[1])

# reshape matrix
print("Reshape matrix a:")
print(a.reshape(3, 2))
print(a.reshape(1, 6))

# resize matrix
print("Resize matrix a:")
a.resize(3, 2)
print(a)  # akan merubah isi a nya
