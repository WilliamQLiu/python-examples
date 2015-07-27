""" Working through examples from Wes McKinney's Python for Data Analysis
    Examples include:
      1.) pandas.merge - connects rows in DataFrames based on keys and/or index
      2.) pandas.concat stacks together objects along an axis
          using lists and dicts, outputting Series and DataFrames
      3.) pandas.combine_first - splice toegether overlapping data to fill in
          missing values in one object with values from another
"""

import pandas
import numpy

def merge_on_key():
    ### Setup DataFrame examples for Merge on Key
    print "\nMerge on Key \n"
    df1 = pandas.DataFrame({
            'key':['b', 'b', 'a', 'c', 'a', 'a', 'b'],
            'data1':range(7)})

    df2 = pandas.DataFrame({
            'key':['a', 'b', 'd'],
            'data2':range(3)})

    print "Dataframe 1 \n", df1, "\n"
    print "Dataframe 2 \n", df2, "\n"

    ### Merge on Keys
    # Merging many-to-one situation with the same key name
    print "Merging df1 and df2 \n", \
            pandas.merge(df1, df2, on='key', how='inner'), "\n"
    # Merging many-to-one situation with different key names
    #print "Merging df1 and df2 \n",
    #    pandas.merge(df1, df2, left_on='leftkey', right_on='rightkey'), "\n"
    # Merges can also be: how='inner' (default), 'outer', left', 'right'

def merge_on_index():
    ### Setup DataFrame examples for Merge on Index
    print "\nMerge on Index \n"
    df1 = pandas.DataFrame({
            'key':['a', 'b', 'a', 'a', 'b', 'c'],
            'value':range(6)})

    df2 = pandas.DataFrame({
            'group_val':[3.5, 7]
        }, index=['a', 'b'])

    print "Dataframe 1 \n", df1, "\n"
    print "Dataframe 2 \n", df2, "\n"

    ### Merge on Index (and Key) with outer join
    print "Merging df1 and df2 with outer join \n", \
            pandas.merge(df1, df2, left_on='key', \
            right_index=True, how='outer'), "\n"


def concat_on_axis_series():
    print "\nConcatenating on Axis \n"
    series1 = pandas.Series([0, 1], index=['a', 'b'])
    series2 = pandas.Series([2, 3, 4], index=['c', 'd', 'e'])
    series3 = pandas.Series([5, 6], index=['f', 'g'])

    print "Series1 is \n", series1, "\n"
    print "Series2 is \n", series2, "\n"
    print "Series3 is \n", series3, "\n"

    # Calling concat for a list of Series links together the values and
    # indexes (default is axis=0)
    print "Concat series 1-3 into a Series (axis=0) \n", \
            pandas.concat([series1, series2, series3]), "\n"

    # Calling concat along axis=1 (instead of default, axis=0) produces
    # a DataFrame (instead of Series)
    # axis=0 was the index/rows, whereas axis=1 is the columns
    print "Concat series 1-3 into a DataFrame (axis=1) \n", \
            pandas.concat([series1, series2, series3], axis=1), "\n"

    # Calling concat along axis=1 showing an intersect
    series4 = pandas.concat([series1 * 5, series3])
    print "Series 4 \n", series4, "\n"
    print "Concat series 1, 4 with outer join into a DataFrame (axis=1) \n", \
            pandas.concat([series1, series4], axis=1), "\n"
    print "Concat series 1, 4 with inner join into a DataFrame (axis=1) \n", \
            pandas.concat([series1, series4], axis=1, join='inner'), "\n"

    # Specify join_axes (i.e. concat using these axis)
    print "Concat series 1, 4 with join_axes into a DataFrame (axis=1) \n", \
            pandas.concat([series1, series4], axis=1, \
            join_axes=[['a', 'c', 'b', 'e']])

    # Create hierarchical index on concatenation axis using 'keys' argument
    result = pandas.concat([series1, series1, series3], \
        keys=['one', 'two', 'three'])
    print "Hierarchical index using keys argument (axis=0) \n", result, "\n"
    result = pandas.concat([series1, series1, series3], axis=1, \
        keys=['one', 'two', 'three'])
    print "Hierarchical index using keys argument (axis=1) \n", result, "\n"


def concat_on_axis_dataframe():
    # Setup DataFrames for examples
    df1 = pandas.DataFrame(numpy.arange(6).reshape(3, 2), \
        index=['a', 'b', 'c'],
        columns=['one', 'two'])

    df2 = pandas.DataFrame(5 + numpy.arange(4).reshape(2, 2), \
        index=['a', 'c'],
        columns=['three', 'four'])

    print "Dataframe 1 \n", df1, "\n"
    print "Dataframe 2 \n", df2, "\n"

    ### Using Lists of objects
    # Concat example with axis=0 and specified keys arguments
    result = pandas.concat([df1, df2], axis=0, keys=['level1', 'level2'])
    print "Hierarchical index with dataframe (of lists) using keys argument", \
            "(axis=0) \n", result, "\n"
    # Concat example with axis=1 and specified keys arguments
    result = pandas.concat([df1, df2], axis=1, keys=['level1', 'level2'])
    print "Hierarchical index with dataframe (of lists) using keys argument", \
            "(axis=1) \n", result, "\n"

    ### Using Dict of objects (instead of Lists), uses dict's keys for keys arg
    result = pandas.concat({'level1':df1, 'level2':df2}, axis=1)
    print "Hierarchical index with dataframe (of dicts) using keys argument", \
            "(axis=1) \n", result, "\n"

    ### Name hierarchical indexes with names arguments
    result = pandas.concat({'level1':df1, 'level2':df2}, axis=1,
        names=['upper', 'lower'])
    print "Can name the hierarchical indexes using names argument", \
            "(axis=1) \n", result, "\n"

    ### Can also ignore_index=True if the row/index is not meaningful


def numpy_where_data_with_overlap():
    # How to handle two datasets where indexes overlap in full or part
    # Method 1: NumPy's Where Function
    a = pandas.Series([numpy.nan, 2.5, numpy.nan, 3.5, 4.5, numpy.nan],
        index=['f', 'e', 'd', 'c', 'b', 'a'])
    b = pandas.Series(numpy.arange(len(a), dtype=numpy.float64),
        index=['f', 'e', 'd', 'c', 'b', 'a'])
    b[-1] = numpy.nan

    print "Series A \n", a, "\n"
    print "Series B \n", b, "\n"
    print "NumPy Where Function \n", numpy.where(pandas.isnull(a), b, a), "\n"


def combine_first_data_with_overlap():
    # How to handle two datasets where indexes overlap in full or part
    # Method 2: Pandas' combine_first method
    df1 = pandas.DataFrame({
        'a': [1., numpy.nan, 5., numpy.nan],
        'b': [numpy.nan, 2., numpy.nan, 6.],
        'c': range(2, 18,4)})
    df2 = pandas.DataFrame({
        'a': [5., 4., numpy.nan, 3., 7.],
        'b': [numpy.nan, 3., 4., 6., 8.]})

    print "DF1 is \n", df1, "\n"
    print "DF2 is \n", df2, "\n"
    # Combine_First patches in the missing data in the calling object with data
    # from the object you pass
    print "Combine_First Method with DF1 on left, DF2 on right \n", \
        df1.combine_first(df2), "\n"
    print "Combine_First Method with DF2 on left, DF1 on right \n", \
        df2.combine_first(df1), "\n"

if __name__ == '__main__':

    ### Merge Examples
    #merge_on_key()
    merge_on_index()

    ### Concat Examples
    #concat_on_axis_series()
    #concat_on_axis_dataframe()

    ### How to handle two datasets where indexes overlap in full or part
    ### Can solve with NumPy's Where Method or Panda's Combine_First Method
    #numpy_where_data_with_overlap()
    #combine_first_data_with_overlap()