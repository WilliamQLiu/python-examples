#!/usr/bin/python

import pandas

file_name = 'world_bank.csv'

if __name__ == "__main__":
    print "Loading File"
    try:
        mydf = pandas.DataFrame.from_csv(file_name)
    except:
        print "Cannot load Data Frame"
    
    print mydf.head()
