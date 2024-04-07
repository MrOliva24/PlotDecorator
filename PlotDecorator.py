import matplotlib.pyplot as plt
import numpy as np
from abc import ABC, abstractmethod


class Plot(ABC):
    @abstractmethod
    def plot(self, x, y):
        pass


class PlotDecorator(Plot,ABC):
    def __init__(self, a_plot):
        self._next_plot = a_plot

    @abstractmethod
    def plot(self, x, y):
        self._next_plot.plot(x, y)



class PlotBasic(Plot):
    def plot(self, x, y):
        super().plot(x, y)
        plt.plot(x, y)


class PlotGrid(PlotDecorator):
    def __init__(self, a_plot):
        super(PlotGrid, self).__init__(a_plot)

    def plot(self, x, y):
        super().plot(x, y)
        plt.grid()


class PlotLegend(PlotDecorator):
    def __init__(self, a_plot):
        super(PlotLegend, self).__init__(a_plot)

    def plot(self, x, y):
        super().plot(x, y)
        plt.legend()


class PlotMean(PlotDecorator):
    def __init__(self, a_plot):
        super(PlotMean, self).__init__(a_plot)

    def plot(self, x, y):
        super().plot(x, y)
        plt.plot([x[0], x[-1]], [y.mean(), y.mean()], "b:")


class PlotSize(PlotDecorator):
    def __init__(self, cm_horizontal, cm_vertical, a_plot):
        self.cm_horizontal = cm_horizontal
        self.cm_vertical = cm_vertical
        super(PlotSize, self).__init__(a_plot)

    def plot(self, x, y):
        super().plot(x, y)
        plt.gcf().set_size_inches(self.cm_horizontal / 2.54,
                                  self.cm_vertical / 2.54)


class PlotLabels(PlotDecorator):
    def __init__(self, label_x, label_y, a_plot):
        self.label_x = label_x
        self.label_y = label_y
        super(PlotLabels, self).__init__(a_plot)

    def plot(self, x, y):
        super().plot(x, y)
        plt.xlabel(self.label_x)
        plt.ylabel(self.label_y)


class PlotTitle(PlotDecorator):
    def __init__(self, title, a_plot):
        self.title = title
        super(PlotTitle, self).__init__(a_plot)

    def plot(self, x, y):
        super().plot(x, y)
        plt.title(self.title)


class PlotGlobalExtrema(PlotDecorator):
    def __init__(self, a_plot):
        super(PlotGlobalExtrema, self).__init__(a_plot)

    def plot(self, x, y):
        super().plot(x, y)
        plt.plot()
        plt.plot(x[np.argmin(y)], y.min(), 'bo', label='global minimum')
        plt.plot(x[np.argmax(y)], y.max(), 'ro', label='global maximum')


class PlotLocalExtrema(PlotDecorator):
    def __init__(self, a_plot):
        super(PlotLocalExtrema, self).__init__(a_plot)

    def plot(self, x, y):
        super().plot(x, y)
        idx_maxima = \
        np.where(np.logical_and(y[1:-1] - y[:-2] > 0, y[1:-1] - y[2:] > 0))[
            0] + 1
        plt.plot(x[idx_maxima], y[idx_maxima], 'gx', label='local maxima')
        idx_minima = \
        np.where(np.logical_and(y[1:-1] - y[:-2] < 0, y[1:-1] - y[2:] < 0))[
            0] + 1
        plt.plot(x[idx_minima], y[idx_minima], 'kx', label='local minima')
        plt.text(x[np.argmin(y)] + 5, y.min(), str(y.min()))
        plt.text(x[np.argmax(y)] + 5, y.max(), str(y.max()))

