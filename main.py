from PlotDecorator import *

x1 = np.linspace(-10*np.pi, 10*np.pi, 1000)
y1= np.sin(x1)/x1
x2 =np.linspace(0, 2*np.pi, 500)
y2 = np.sin(x2)**2
x3 = np.linspace(-np.pi, np.pi, 200)
y3 = np.cos(x3)*np.sin(x3)


p_basic = PlotBasic()

p_grid = PlotGrid(
            PlotTitle('basic + grid + title',
                PlotBasic()))

p_extrema = PlotTitle('basic + global + local extrema + title',
                PlotGlobalExtrema(
                    PlotLocalExtrema(
                        PlotBasic())))

p_full = PlotSize(18, 18,
            PlotTitle('full',
                PlotLabels('x','sin(x)/x',
                    PlotLegend(
                        PlotGrid(
                            PlotMean(
                                PlotGlobalExtrema(
                                    PlotLocalExtrema(
                                        PlotBasic()))))))))


p_extrema.plot(x1, y1)
plt.show()
p_full.plot(x2, y2)
plt.show()
p_extrema.plot(x3, y3)
plt.show()