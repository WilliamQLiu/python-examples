""" Plotting with Pandas' rplot """

from pandas import read_csv
import pandas.tools.rplot as rplot
import matplotlib.pyplot as plt
import pylab

TIPS_DATA = read_csv('tips.csv')
# total_bill, tip, sex, smoker, day, time, size
# 16.99, 1.01, Female, No, Sun, Dinner, 2

def trellis_plot_histogram():
    """ Trellis Plot arranges data in a rectangular grid by values of certain attributes using a histogram """

    plot =rplot.RPlot(TIPS_DATA, x='total_bill', y='tip')
    plot.add(rplot.TrellisGrid(['sex', 'smoker']))
    plot.add(rplot.GeomHistogram())
    plot.render(plt.gcf())

def trellis_plot_density():
    """ Trellis Plot arranges data in a rectangular grid by values of certain attributes using a density plot """

    plot =rplot.RPlot(TIPS_DATA, x='total_bill', y='tip')
    plot.add(rplot.TrellisGrid(['sex', 'smoker']))
    plot.add(rplot.GeomDensity())
    plot.render(plt.gcf())

def trellis_plot_scatter_and_polyfit():
    """ Trellis Plot arranges data in a rectangular grid by values of certain attributes using two plots: a scatter plot and a polyfit"""

    plot =rplot.RPlot(TIPS_DATA, x='total_bill', y='tip')
    plot.add(rplot.TrellisGrid(['sex', 'smoker']))
    plot.add(rplot.GeomScatter())
    plot.add(rplot.GeomPolyFit(degree=2))
    plot.render(plt.gcf())

def trellis_plot_scatter_and_density2d():
    """ Trellis Plot arranges data in a rectangular grid by values of certain attributes using a scatter plot with a 2D kernel density superimposed"""

    plot =rplot.RPlot(TIPS_DATA, x='total_bill', y='tip')
    plot.add(rplot.TrellisGrid(['sex', 'smoker']))
    plot.add(rplot.GeomScatter())
    plot.add(rplot.GeomDensity2D())
    plot.render(plt.gcf())

if __name__ == '__main__':
    plt.figure()

    #trellis_plot_histogram()
    #trellis_plot_density()
    trellis_plot_scatter_and_polyfit()
    #trellis_plot_scatter_and_density2d()

    pylab.show() # Display the graph
