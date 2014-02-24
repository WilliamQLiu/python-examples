#!/usr/local/bin/python
""" Lesson on summarizing and grouping using dataframes """
# Use in bash to write to output file
#$cat nytimes.csv | python counter.py > myoutput.txt
#/usr/bin/env python
#/usr/bin/python

import pandas
import matplotlib
#matplotlib.use('Agg')
import matplotlib.pyplot as plt

#plt.switch_backend('agg')

pandas.set_option('expand_frame_repr', False) # expand text on build
pandas.set_option('display.max_columns', 0) # Display any number of columns
pandas.set_option('display.max_rows', 0) # Display any number of rows

if __name__ == '__main__':
    
    # Get File Online
    #df = pandas.read_csv(\
    #    filepath_or_buffer='http://stat.columbia.edu/~rachel/datasets/nyt1.csv',
    #    sep = ',', header=0)
    
    # Get File from CSV on Dropbox
    df = pandas.DataFrame.from_csv(
        """/Users/williamliu/Dropbox/NYC-DAT-08/Homework_0/william_liu/output/nytimes.csv""",
        index_col = False, header = 0, sep = ',')
    
    #print "Dataframe Head \n", df.head()
    
    #print df.describe() # Get summary description
    #"Age","Gender","Impressions","Clicks","Signed_In"
    
    #df.Gender


    # Sum through grouping by Age and Gender
    #print df.groupby(['Age', 'Gender']).sum()

    pandas.concat(df['Age'], df['Gender'])

    # Plot
    #plt.figure()
    #df.plot(title='NY Times', x='Age', y='Impressions', kind='line')
    #plt.show()

