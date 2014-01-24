""" There's two dataframes with dates as their index
    One of the dataframes has a timestamp and this prevents from adding
    the dataframes together.  How can you match up time stamps?"""

from pandas import DataFrame, Timestamp, concat

### Setup dataframe 1 (df1)
df1 = DataFrame({'col1':[Timestamp('20130102000030'),
                         Timestamp('2013-01-03 00:00:30'),
                         Timestamp('1/4/2013 000030')],
                 'col2':[1, 10, 18]
    })
print "This is dataframe 1 \n", df1, "\n"
# 2 columns (col1, col2) and 3 rows (row 0, 1, 2)

### Set index of df1
df1 = df1.set_index('col1')
print "Col1 is now the index \n", df1, "\n"
# Replaces column listing numbers (0, 1, 2) with index
# Now df1 is 3 rows (timestamps), 1 column (values: 1, 10, 18)


### Setup dataframe 2 (df2)
d = {'col2':[22, 10, 113]}
i = [Timestamp('20130102'),
     Timestamp('2013-01-03'),
     Timestamp('1/4/2013')]
df2 = DataFrame(data=d, index=i)
df2.index.name = 'col1'
print "This is dataframe 2 \n", df2, "\n"


### Adding Dataframes (by column)
# INCORRECT
# print df1+df2 # We can't just add dataframes together
# This returns 6 rows, 1 col; col1 is merged dates, but col2 is NaNs

# CORRECT
# We need to make index of df2 the same as index of df1 by
# filling in the missing values with previous known values
df2 = df2.reindex(df1.index, method='pad') # Default method='None'
print "Adding dataframes (df1 + df2) \n", df1+df2, "\n"
# Now the values for df1 and df2 are added


### Adding Dataframes (by row)
df1 = DataFrame([1,2,3]) # 3 rows, 1 column
print "New dataframe 1 \n", df1, "\n"
df2 = DataFrame([4,5,6]) # 3 rows, 1 column
print "New dataframe 2 \n", df2, "\n"
print "Concatenated df1, df2 \n", concat([df1, df2]), "\n" # 6 rows, 1 col


### Joining data frames by index
# Setup df1
d = {'col1':[22,10,113]}
i = [Timestamp('1/1/2013'),
     Timestamp('1/2/2013'),
     Timestamp('1/3/2013')]
df1 = DataFrame(data=d, index=i)
print "Another df1 \n", df1, "\n" # 3 rows (of dates), 1 col of integers

# Setup df2
d = {'col2':[5,5]}
i = [Timestamp('1/1/2013'),
     Timestamp('1/3/2013')]
df2 = DataFrame(data=d, index=i)
print "Another df2 \n", df2, "\n" # 2 rows (of dates), 1 col of integers

# Merge df1 and df2
df3 = df1.merge(df2, left_index=True, right_index=True, how='left')
print "Merged database is df3 \n", df3 # 3 rows (of dates), 2 col of integers
# Similar to a database-style join