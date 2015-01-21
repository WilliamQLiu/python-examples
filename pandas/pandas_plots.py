"""
    Pandas' plot () method for Series and DataFrames are a simple wrapper
    around matplotlib's plot() method
    http://pandas.pydata.org/pandas-docs/version/0.15.1/visualization.html
"""

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd


def basic_plotting_series():
    """ plot() on a Series
    http://pandas.pydata.org/pandas-docs/dev/generated/pandas.Series.plot.html 
    """
    mytimeseries = pd.Series(data=np.random.randn(500),
                             index=pd.date_range('1/1/2000', periods=500))
    # print type(mytimeseries)  # <class 'pandas.core.series.Series'
    # print mytimeseries  # e.g. [[2000-01-01, 1.247], [2000-01-02, -0.234]]
    mytimeseries = mytimeseries.cumsum()  # get cumulative sum over flat array
    mytimeseries.plot(kind='line', use_index=True, style='--', color='blue')
    #kind='line', 'bar', 'barh', 'hist', 'pie', 'box', 'kde', 'area', 'density'
    plt.show()  # Displays graph


def basic_plotting_df():
    """ plot() on a DataFrame; it plots all of the columns with labels
    http://pandas.pydata.org/pandas-docs/dev/generated/pandas.DataFrame.plot.html
    """
    mytimeseries = pd.Series(data=np.random.randn(500),
                             index=pd.date_range('1/1/2000', periods=500))
    df = pd.DataFrame(data=np.random.randn(500, 5),  # Create 5 sets of #'s'
                      index=mytimeseries.index,
                      columns=list('ABCDE'))  # 5 elements
    #print type(df)
    #print df.head(2)
    #               A    B    C    D    E
    #2000-01-01    -0.2  .12  .29  .14 1.00
    #2000-01-02    2.0  -1.2  .89  .78  .77

    df = df.cumsum()  # get cumulative sum over flat array
    df.plot(kind='line', use_index=True, style='-')
    plt.show()  # Displays graph


if __name__ == '__main__':
    basic_plotting_series()
    basic_plotting_df()
