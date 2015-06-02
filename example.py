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

hist1.plot()
hist2.plot(kind='bar', alpha=0.3)
plt.xlim(-0.1, 10.1)
plt.show()
