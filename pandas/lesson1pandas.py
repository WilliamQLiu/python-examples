### Import all the libraries needed for the tutorial (global to specific)
# General syntax to import specific functions in a library: 
#   from (library) import (specific library function)
# General syntax to import a library but no functions: 
#   import (library) as (give the library a nickname/alias)
#   E.g. import matplotlib.pyplot

#import os # Used to remove a file
#from os import remove

from pandas import DataFrame, read_csv
#from ggplot import *

### Create Data
# The inital set of baby names and bith rates
names = ['Bob','Jessica','Mary','John','Mel']
births = [968, 155, 77, 578, 973]

"""zip(seq1 [, seq2 [...]]) -> [(seq1[0], seq2[0] ...), (...)]
Return a list of tuples, where each tuple contains the i-th element
from each of the argument sequences.  The returned list is truncated
in length to the length of the shortest argument sequence."""

BabyDataSet = zip(names,births)
#print BabyDataSet # [('Bob', 968), ('Jessica', 155), ('Mary', 77), 
#('John', 578), ('Mel', 973)]

# Setup Dataframe
df = DataFrame(data = BabyDataSet, columns=['Names', 'Births'])
#print df # shows 4 rows by 2 columns ('Names', 'Births')


### Saving and Reading File
df.to_csv('births1880.csv', index=False, header=False) # Write dataframe to csv
# Setup location to look for dataframe
myloc = r'C:\Users\wliu\Documents\GitHub\Python\HelloWorld\pandas\births1880.csv'
# Read the df from location, by default assumes header is first line
#df = read_csv(myloc, header=None) # Need to explicitly state if no header 
# Read the df from myloc while specifying headers
df = read_csv(myloc, names=['Names', 'Births'])
print "Here's the dataframe\n", df

# Think of rows as 'index' of the DataFrame (e.g. 0, 1, 2, 3, 4)
# Index is the 'Primary Key' except that an index can have duplicates
# [Names, Births] are the 'column headers'

# To delete a file
#remove(myloc)


### Analyzing the Data
# Check data type of a specific column (Births)
print "\nData Type of Births column is: ", df.Births.dtype

# Sort the dataframe and select the top row using two methods:
# Method 1 - Sort, Then Print Head(1)
Sorted = df.sort(['Births'], ascending=[0])
print "Highest births by dataframe ", Sorted.head(1)
# Output is dataframe with highest births
# Method 2 - Take Max
print "Maximum births", df['Births'].max()
# Output is just the number 973 (highest births)


### Presenting the Data
#print df['Names'] # Print the entire list of the Names column
#print df['Births'].max() # Print maximum value of Births column
print df['Births']
#print ggplot(aes(x='Names', y='Births'), data=df)
