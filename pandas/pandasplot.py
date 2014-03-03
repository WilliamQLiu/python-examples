""" Plotting with Pandas' rplot """

from pandas import read_csv
import pandas.tools.rplot as rplot
import matplotlib.pyplot as plt

TIPS_DATA = read_csv('tips.csv')


if __name__ == '__main__':
    plt.figure()
    plot =rplot.RPlot(TIPS_DATA, x='total_bill', y='tip')
    plot.add(rplot.TrellisGrid(['sex', 'smoker']))
    plot.add(rplot.GeomHistogram())
    plot.render(plt.gcf())
    