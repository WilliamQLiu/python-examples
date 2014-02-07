""" Working through examples from Wes McKinney's Python for Data Analysis
    Examples include:
      1.) reshaping data with hierarchical indexing
      
"""

import pandas
import numpy

def stack_basic():
    data = pandas.DataFrame(numpy.arange(6).reshape(2, 3),
        index=pandas.Index(['Ohio', 'Colorado'],
        name='state'),
        columns=pandas.Index(['one', 'two', 'three'], name='number'))
    print "Basic DataFrame \n", data, "\n"

    # Stack method pivots the columns into the rows
    result = data.stack()
    print "Dataframe after calling stack method \n", result, "\n"

    # Unstack method rearranges the data from a hierarchically-indexed
    # Series into a DataFrame
    result = result.unstack()
    print "Dataframe after calling unstack method \n", result, "\n"

def pivot_basic():
    ### Commonly used to store multiple time series by long or stacked format
    longdata = pandas.DataFrame({
        'date':[
            '1959-03-01 00:00:00', '1959-03-02 00:00:00', '1959-03-03 00:00:00',
            '1959-03-31 00:00:00', '1959-06-02 00:00:00', '1959-06-04 00:00:00',
            '1959-09-30 00:00:00', '1959-10-01 00:00:00', '1959-10-15 00:00:00',
            '1959-12-31 00:00:00'],
        'item':['realgdp', 'infl', 'unemp', 'realgdp', 'infl', 'unemp',
            'realgdp', 'infl', 'unemp', 'realgdp'],
        'value':[2710.349, 0.000, 5.800, 2778.801, 2.340, 5.100,
            2775.488, 2.740, 5.300, 2785.204]
        }, index=range(0, 10))

    print "Long DataFrame: \n", longdata, "\n"

    # Pivot DataFrame
    pivoted = longdata.pivot(index='date', columns='item', values='value')
    print "Pivoted Dataframe 'item' values into columns \n", pivoted, "\n"

    # Add another column of random values
    longdata['value2'] = numpy.random.randn(len(longdata))
    print "Dataframe with a new column: values2 \n", longdata, "\n"

    # Pivot DataFrame to make hierarchical columns
    pivoted = longdata.pivot(index='date', columns='item')
    print "Pivoted Dataframe hierarchical columns \n", pivoted, "\n"

    ### Note: Pivot is just a shortcut for set_index method,
    ### then reshaping with unstack method

def remove_dups():
    ### Remove duplicate rows in a DataFrame
    df = pandas.DataFrame({
        'k1': ['one'] * 3 + ['two'] * 4,
        'k2': [1, 1, 2, 3, 3, 4, 4]
        })
    print "DataFrame containing duplicates \n", df, "\n"

    # duplicated() returns a boolean Series saying if row is duplicate
    # Note: By default, this considers all columns in determining duplicate
    print "Returning Series of duplicates \n", df.duplicated(), "\n"

    # drop_duplicates() returns a DataFrame where the duplicated array is True
    # Note: By default, this considers all columns in determining duplicate
    print "Returning DataFrame of duplicates \n", df.drop_duplicates(), "\n"

    # duplicated() and drop_duplicates() can consider specific columns
    # for determining if row is duplicate
    df['v1'] = range(7) # Add a new column
    print "New DataFrame \n", df, "\n"
    dropdf = df.drop_duplicates(['k1']) # Use k1 as the col to check if dup
    print "DataFrame after drop_duplicates on k1 column only \n", dropdf, "\n"
    # Notice that it keeps only the first observed value combination
    # Can specify to take the last_value as well

def replace_values():
    # replace replaces values while something like fillna fills missing data
    mydata = pandas.Series([1., -999., 2., -999., -1000., 3.])
    print "Data in Series \n", mydata, "\n"

    # replace x with y using .replace()
    print "Data after replacing -999 with NaN \n", \
        mydata.replace(-999, numpy.nan), "\n"

    # replace list of x with y using .replace()
    print "Data after replacing -999, -1000 with NaN \n", \
        mydata.replace([-999, -1000], numpy.nan), "\n"

    # replace list of x with list of y using .replace()
    print "Data after replacing -999, -1000 with NaN and 0 \n", \
        mydata.replace([-999, -1000], [numpy.nan, 0]), "\n"    

    # replace dict of x with dict of y using .replace()
    print "Data after replacing -999, -1000 with NaN and 0 (using dict) \n", \
        mydata.replace({-999:numpy.NaN, -1000:0}), "\n"   

if __name__ == '__main__':
    
    #stack_basic() # Stack/Unstack rearranges the data's hierarchical index
    #pivot_basic() # Pivot from 'long' to 'wide' data format
    #remove_dups() # How to remove duplicate rows in a DataFrame
    replace_values() # How to replace values in a Series

