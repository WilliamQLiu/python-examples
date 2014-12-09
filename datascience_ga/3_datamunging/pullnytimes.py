#!/usr/local/bin/python

import pandas

print "Getting first file"
mydf = pandas.read_csv(filepath_or_buffer=\
    'http://stat.columbia.edu/~rachel/datasets/nyt1.csv', sep=',', header=0)

def get_files_online(num):

    #mypath = "http://stat.columbia.edu/~rachel/datasets/nyt1.csv"
    mypath = "http://stat.columbia.edu/~rachel/datasets/nyt" + str(num) + ".csv"
    print "Getting ", mypath

    # Get File Online
    df = pandas.read_csv(filepath_or_buffer=mypath, sep = ',')

    return df


    #mydf = pandas.DataFrame.merge(df, mydf, how='left')

if __name__ == "__main__":

    # Get files 2 through 30
    for x in range(29):
        currentdf = get_files_online(x+2)
        mydf = mydf.append(currentdf)

    print "Writing final file"
    mydf.to_csv("nytimes.csv")

    #df = pandas.DataFrame.from_csv(
    #r"""/Users/williamliu/Dropbox/NYC-DAT-08/Homework_0/william_liu/output/nytimes.csv""",
    #index_col = False, header = 0, sep = ',')
