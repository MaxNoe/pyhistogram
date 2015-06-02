import numpy as np
from histogram import Histogram
import matplotlib.pyplot as plt
from matplotlib.style import use
use('ggplot')

hist1 = Histogram(100, [0, 10])
hist2 = Histogram(100, [0, 10])

for i in range(1000):
    hist1.fill(np.random.normal(5, 1, 10000))
    hist2.fill(np.random.exponential(2, 10000))

print(hist2.n_entries)
print(hist2.n_underflow)
print(hist2.n_overflow)

plt.bar(
    hist1.bin_centers,
    hist1.entries,
    hist1.bin_width,
    align='center',
    lw=0,
    alpha=0.4,
)
plt.bar(
    hist2.bin_centers,
    hist2.entries,
    hist2.bin_width,
    align='center',
    lw=0,
    alpha=0.4,
    color='red',
)
plt.show()
