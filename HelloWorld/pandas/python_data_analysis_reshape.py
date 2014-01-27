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
    pass

if __name__ == '__main__':
    
    stack_basic() # Stack/Unstack rearranges the data's hierarchical index
    pivot_basic() # Pivot from 'long' to 'wide' data format