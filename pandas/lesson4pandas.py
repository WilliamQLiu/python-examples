# Import libraries
from pandas import DataFrame


### Setup Data

# Our small data set
d = [0,1,2,3,4,5,6,7,8,9]

# Create dataframe
df = DataFrame(d)
#print df # 10 rows, 1 column

# Change column name
df.columns = ['Rev']
#print df # 10 rows, 1 column (now named 'Rev')

# Add a column
df['NewCol'] = 5
#print df # 10 rows, 2 columns (new col is called 'NewCol' with all 5's)

# Modify values in columsn
df['NewCol'] = df['NewCol'] + 1
#print df # 10 rows, 2 columns, NewCol values inc by 1

# Deleting columns
del df['NewCol']
#print df # 10 rows, 1 column

# Create two new columns, 'test' and 'col' for 10 rows, 3 columns
df['test'] = 3
df['col'] = df['Rev']
#print df
#print list(df.columns.values) # Prints list of column names #['Rev', 'test', 'col']

# Modifying Index names
myindex = ['a','b','c','d','e','f','g','h','i','j']
df.index = myindex # index size must match or error
#print df # Now dataframe is a-j for rows, with cols 'Rev', 'test', 'col'


### Selecting data (loc)
# Using loc, strictly label based
#print df.loc['a'] # prints just row 'a' values

# Using loc[inclusive:inclusive]
#print df.loc['a':'d'] # prints row 'a', 'b', 'c', 'd' values


### Selecting data (iloc)
# Using iloc, strictly integer position based
# df.iloc[inclusive:exclusive]
#print df.iloc[0:3] # prints row 'a', 'b', 'c'; rows 0, 1, 2


### Selecting data (column names)
#print df['Rev'] # Get column of 'Rev' only along with the index
#print df[['Rev', 'test']] # Get columns 'Rev', 'test' along with the index

#df['ColumnName'][inclusive:exclusive]
#print df['Rev'][0:3] # Get column 'Rev' with rows 0, 1, 2
#print df['col'][5:] # Get column 'col' with rows 5+
#print df[['col','test']][:3] # Get columns 'col', 'test' with rows 0, 1, 2

### Selecting data (Head and Tail)
#print df.head() # Select top N records (default = 5)
#print df.tail() # Select top N records (default = 5)
