from __future__ import division, absolute_import
import numpy as np

class Statistics():
    """
    Class for calculating running statistics
    that enables more than one value to be filled in at a time

    algorithms are taken from:
    http://en.wikipedia.org/wiki/Algorithms_for_calculating_variance#Parallel_algorithm
    """
    def __init__(self):
        self._n = 0
        self._mean = 0
        self._M2 = 0
        self._M3 = 0
        self._M4 = 0

    def fill(self, B):
        """
        update the Statistics with the new data in B

        notation follows Wikipedia
        """
        B = np.array(B, copy=False, ndmin=1)

        n_A = self._n
        mean_A = self._mean
        M2_A = self._M2
        M3_A = self._M3
        M4_A = self._M4

        n_B = len(B)
        mean_B = B.mean()
        M2_B = np.sum((B - mean_B) ** 2)
        M3_B = np.sum((B - mean_B) ** 3)
        M4_B = np.sum((B - mean_B) ** 4)

        n_X = n_A + n_B
        delta = mean_B - mean_A
        delta_per_n = delta / n_X

        self._n = n_X
        self._mean = (n_A * mean_A + n_B * mean_B) / n_X
        self._M2 = M2_A + M2_B + delta * delta_per_n * n_A * n_B

        self._M3 = M3_A + M3_B \
            + delta * delta_per_n**2 * n_A * n_B * (n_A - n_B) \
            + 3 * delta_per_n * (n_A * M2_B - n_B * M2_A)

        self._M4 = M4_A + M4_B \
            + delta * delta_per_n**3 * n_A * n_B * (n_A**2 - n_A*n_B + n_B**2) \
            + 6 * delta_per_n**2 * (n_A**2 * M2_B + n_B**2 * M2_A) \
            + 4 * delta_per_n * (n_A * M3_B - n_B * M3_A)


    def __len__(self):
        return self._n

    def mean(self):
        return self._mean

    def variance(self):
        return self._M2 / (self._n - 1)

    def std(self):
        return np.sqrt(self.variance())

    def skewness(self):
        return np.sqrt(self._n) * self._M3 / (self._M2 ** 1.5)

    def kurtosis(self):
        return self._n * self._M4 / (self._M2 ** 2) - 3
