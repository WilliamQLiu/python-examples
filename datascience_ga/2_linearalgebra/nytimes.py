#!/usr/local/bin/python
""" Lesson on summarizing and grouping using dataframes """
# Use in bash to write to output file
#$cat nytimes.csv | python counter.py > myoutput.txt
#/usr/bin/env python
#/usr/bin/python

import pandas
import matplotlib
import numpy
#matplotlib.use('Agg')
#import matplotlib.pyplot as plt
#plt.switch_backend('agg')

pandas.set_option('expand_frame_repr', False) # expand text on build
pandas.set_option('display.max_columns', 0) # Display any number of columns
pandas.set_option('display.max_rows', 0) # Display any number of rows

if __name__ == '__main__':
    
    # Get File Online
    #df = pandas.read_csv(\
    #    filepath_or_buffer=\
    #        'http://stat.columbia.edu/~rachel/datasets/nyt1.csv',
    #    sep = ',', header=0)
    
    # Get File from CSV on Dropbox
    df = pandas.DataFrame.from_csv(
        r"""/Users/williamliu/Dropbox/NYC-DAT-08/Homework_2/william_liu/test.csv""",
        index_col = False, header = 0, sep = ',')
    #
    #"""C:\Users\wliu\Dropbox\NYC-DAT-08\Homework_0\william_liu\output\nytimes.csv"""
 
    #print df.describe() # Get summary description
    #"Age","Gender","Impressions","Clicks","Signed_In"

    print "Dataframe Head \n", df.head()
    #   Age  Gender  Impressions  Clicks  Signed_In
    #0   36       0            3       0          1
    #1   73       1            3       0          1
    #2   30       0            3       0          1
    #3   49       1            3       0          1
    #4   47       1           11       0          1
   
    # Clean up Data
    #df.Gender[df.Gender == 0] = 'Female' #Replace 0's with 'Female'
    #df.Gender[df.Gender == 1] = 'Male' #Replace 1's with 'Male'
    #df.Signed_In[df.Signed_In == 0] = 'Not Signed In' #Replace 0's with No Sign
    #df.Signed_In[df.Signed_In == 1] = 'Signed In' #Replace 0's with No Sign
    #print df.head()
    
    #print df.groupby(['Age', 'Gender', 'Signed_In']).sum()
    #df.plot(title='Test', x='Age', kind='bar')
    #plt.show()

    #### Create column for Click through Rate (CTR)
    #df['Clicks'] = df.Clicks.astype(float)
    #df['Impressions'] = df.Impressions.astype(float)
    #df['ctr'] = df['Clicks'] / df['Impressions']
    
    print df.columns
    #Index([u'Age', u'Gender', u'Impressions', u'Clicks', u'Signed_In', u'ctr'], dtype='object')

    dfg = df[ ['Age', 'Gender', 'Signed_In', 'Clicks', 'Impressions'] ].groupby(['Age']).agg([numpy.sum])
    print dfg
    #dfg['Clicks'] = dfg.Clicks.astype(float)
    #dfg['Impressions'] = dfg.Impressions.astype(float)
    dfg['ctr'] = dfg['Clicks'] / dfg['Impressions']
    print dfg