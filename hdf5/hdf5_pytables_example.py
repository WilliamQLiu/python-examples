""" HDFStore is a dict-like object that reads and writes pandas using the
    HDF5 format using the PyTables library.  It's like the pickle library, but
    better for pandas.
"""


import numpy as np
import pandas as pd


if __name__ == '__main__':

    ### Setup store
    my_store = pd.HDFStore('my_store.h5')  # File path: store.h5
    print type(my_store)  #<class 'pandas.io.pytables.HDFStore'>

    ### Setup different types of data (Series, DataFrame, Panel)
    np.random.seed(1234)

    # Series
    index = pd.date_range('1/1/2000', periods=8)
    s = pd.Series(np.random.randn(5), index=['a', 'b', 'c', 'd', 'e'])
    print s
    #a    0.471435
    #b   -1.190976
    #c    1.432707
    #d   -0.312652
    #e   -0.720589
    #dtype: float64

    # DataFrame
    df = pd.DataFrame(np.random.randn(8, 3), index=index, columns=['A', 'B', 'C'])
    print df
    #                   A         B         C
    #2000-01-01  0.887163  0.859588 -0.636524
    #2000-01-02  0.015696 -2.242685  1.150036
    #2000-01-03  0.991946  0.953324 -2.021255
    #2000-01-04 -0.334077  0.002118  0.405453
    #2000-01-05  0.289092  1.321158 -1.546906
    #2000-01-06 -0.202646 -0.655969  0.193421
    #2000-01-07  0.553439  1.318152 -0.469305
    #2000-01-08  0.675554 -1.817027 -0.183109

    # Panel
    wp = pd.Panel(np.random.randn(2, 5, 4), items=['Item1', 'Item2'],
                  major_axis=pd.date_range('1/1/2000', periods=5),
                  minor_axis=['A', 'B', 'C', 'D'])
    print wp
    # <class 'pandas.core.panel.Panel'>
    # Dimensions: 2 (items) x 5 (major_axis) x 4 (minor_axis)
    # Items axis: Item1 to Item2
    # Major_axis axis: 2000-01-01 00:00:00 to 2000-01-05 00:00:00
    # Minor_axis axis: A to D

    ### PUT data into different data types (Series, DataFrame, Panel)
    my_store['s'] = s  # my_store.put('s', s) is equivalent method
    my_store['df'] = df
    my_store['wp'] = wp

    ### Data is now stored away so you can retrieve it later
    print my_store
    print type(my_store)
    #File path: my_store.h5
    #/df            frame        (shape->[8,3])
    #/s             series       (shape->[5])
    #/wp            wide         (shape->[2,5,4])
    #<class 'pandas.io.pytables.HDFStore'>
    #Closing remaining open files:my_store.h5...done

    ### GET data from stored objects; get stored objects
    print my_store['df']  #store.get['df'] and store.df is equivalent method
    #                   A         B         C
    #2000-01-01  0.887163  0.859588 -0.636524
    #2000-01-02  0.015696 -2.242685  1.150036
    #2000-01-03  0.991946  0.953324 -2.021255
    #2000-01-04 -0.334077  0.002118  0.405453
    #2000-01-05  0.289092  1.321158 -1.546906
    #2000-01-06 -0.202646 -0.655969  0.193421
    #2000-01-07  0.553439  1.318152 -0.469305
    #2000-01-08  0.675554 -1.817027 -0.183109

    ### Delete object specified by the key
    del my_store['wp']
    print my_store

    my_store.close()  # Close the stored file