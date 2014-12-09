#!/usr/bin/python

import pandas
pandas.set_option('expand_frame_repr', False) # expand text on build
pandas.set_option('display.max_columns', 0) # Display any number of columns
#pandas.set_option('display.width', 0)
#pandas.set_option('max_columns',30)

file_name = 'world_bank.csv'

if __name__ == "__main__":
    
    #print "Loading File"
    try:
        mydf = pandas.DataFrame.from_csv(file_name, header=1, index_col=0)
    except:
        print "Cannot load Data Frame"
    
    #print mydf.index # Get list of index
    #print mydf.columns # Get list of columns
    print "Original Dataframe", mydf

    #print mydf.describe()
    #mydf = mydf.dropna(axis=0)
    #print "DF after dropping NaNs", mydf
    
    mydf = mydf.iloc[:29,:22] # Remove rows 30 and lower, remove cols 22 and over
    #mydf.fillna(0, inplace=True)
    print mydf # Cleaned dataframe

    mydf = mydf.astype(float) # Change to float (or else it'll see as string)
    #print mydf.describe()
    #print mydf.index # Show just index names
    #print mydf.columns # Show just column names
    #print mydf.values # Show Values
    #print mydf.T # Transpose
    print "Print which country has highest value for each indicator type"
    print mydf.idxmax() # Returns index of maximum value
    print mydf.max() # Returns <class 'pandas.core.series.Series'>