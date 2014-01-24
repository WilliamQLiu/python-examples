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

