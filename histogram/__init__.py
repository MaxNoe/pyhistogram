from __future__ import division, absolute_import
import numpy as np
import matplotlib.pyplot as plt
from .runningstats import Statistics

class Histogram():
    """
    A 1D Histogram that can be filled and stores some statistics
    """
    def __init__(self, bins, limits=None, include_all=False):
        if np.isscalar(bins):
            if limits is None:
                raise ValueError(
                    'If you supply the number of bins '
                    'you need to supply limits'
                )
            self.n_bins = bins
            self.bin_edges = np.linspace(limits[0], limits[1], bins+1)
            self.limits = tuple(limits)
        else:
            self.n_bins = len(bins) - 1
            self.bin_edges = bins
            self.limits = (min(bins), max(bins))

        self.entries = np.zeros(self.n_bins)
        self.n_entries = 0
        self.n_underflow = 0
        self.n_overflow = 0

        self.bin_width = np.diff(self.bin_edges)
        if np.all(self.bin_width == self.bin_width[0]):
            self.bin_width = self.bin_width[0]


        self.bin_centers = self.bin_edges[:-1] + 0.5 * self.bin_width

        self.stats = Statistics()
        self.include_all = include_all

    def fill(self, data):
        data = np.array(data, ndmin=1, copy=False)

        if self.include_all:
            self.stats.fill(data)
        else:
            a, b = self.limits
            in_limits = np.logical_and(data >= a, data <= b)
            self.stats.fill(data[in_limits])

        entries, _ = np.histogram(data, self.bin_edges)
        self.entries += entries
        self.n_entries += entries.sum()

        self.n_underflow += np.sum(data < self.limits[0])
        self.n_overflow += np.sum(data > self.limits[1])

    def plot(self, kind='step', ax=None, **kwargs):

        if ax is None:
            ax = plt.gca()

        if kind == 'step':
            px = np.repeat(self.bin_edges, 2)
            py = np.hstack([[0], np.repeat(self.entries, 2), [0]])

            ax.plot(px, py, '-', **kwargs)

        if kind == 'bar':
            ax.bar(
                self.bin_centers,
                self.entries,
                self.bin_width,
                align='center',
                **kwargs
            )

        plt.draw_if_interactive()

    def __len__(self):
        return self.entries

    def mean(self):
        return self.stats.mean()

    def std(self):
        return self.stats.std()

    def variance(self):
        return self.stats.variance()

    def kurtosis(self):
        return self.stats.kurtosis()

    def skewness(self):
        return self.stats.skewness()
