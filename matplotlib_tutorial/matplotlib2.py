import numpy as np
import matplotlib.pyplot as plt

# generator sinyal sinusoidal

# membuat data --> vt= Vm . (sin(2wt + theta)) rumus sinusoidal
# camel case


def sinusGenerator(amplitudo, frekuensi, timeAkhir, theta):
    t = np.arange(0, timeAkhir, 0.1)
    y = amplitudo * np.sin(2*frekuensi*t + np.deg2rad(theta))
    return t, y


title = "\nGelombang Sinusoidal\n"
# rumus = r'$ \mathcal{Y} = A.sin(2 \omega t) $'
# membuat plot
plt.title(title + r'$ \mathcal{Y} = A.sin(2 \omega t)$'+"\n")
# plt.xlabel("sudut (sin)")
# plt.ylabel("amplitudo (A)")
plt.text(0.1, 2, "amplitudo (A)")
plt.text(4, 0.1, "sudut (sin)")

# setting axis
# plt.axis([xmin, xmax, ymin, ymax])
plt.axis([-1, 4, -2, 2])

# menggeser axis
ax = plt.gca()
ax.spines['left'].set_position(('data', 0))
ax.spines['bottom'].set_position(('data', 0))
ax.spines['right'].set_color('none')
ax.spines['top'].set_color('none')

t1, y1 = sinusGenerator(1, 1, 4, 0)
plt.plot(t1, y1, label='sinus 1', color="yellow", linewidth=3)
plt.text(1, 1, 'sin(0)')  # menambahkan text

t2, y2 = sinusGenerator(1, 1, 4, 30)
plt.plot(t2, y2, label='sinus 2', color="plum",
         linestyle="dashed", linewidth=2)

t3, y3 = sinusGenerator(1, 1, 4, 60)
plt.plot(t3, y3, color="purple", linestyle="dotted",
         label="sinus 3", linewidth=1)

# menampilkan plot
plt.legend(loc='lower right', shadow=True)  # box informasi
plt.show()
