### Testing how to use csv module and open a file

#import csv
#N used to hold head (i.e. first N lines)
#N = 10
##Opens CSV file in Path and prints out the head
#with open("BX-Book-RatingsSmall.csv") as myfile:
#    head=myfile.readlines(N)
#print head

## Testing how to open a csv file and print all the lines
#Opens CSV file in Path and prints out all lines
#for line in open('testFile.csv'):
#    print line,

### Import csv data using third party modules, clean data, and output to a ODBC destination (e.g. SQL Server)
## Import modules
import numpy
import pandas
import datetime
import time
import csv


### Set important settings about the file
myinputfile = 'BX-Book-Ratings.csv'  # Load myinputfile with data
myoutputfile = 'BX-Book-Ratings-Output.csv' # Set File Output Path
numcolumns = 3  # Set Number of Columns in CSV File

## Set File Input Path as read only
## Look through all indexes in myfile, split each line using '\n', remove any data that isn't 3 columns (since data is 3 columns)
#myfile = open (myinputfile, 'r')  #Open file as read only
#for my_row_counter, line in enumerate(myfile):   #for loop to enumerate file (i.e. breaks file into columns) for each row
#   splitline = line.strip().split('\n')    # splitline is a list
#   if len(splitline) != numcolumns-1:
#        first_bad_line = splitline
#        print "First bad row: ", my_row_counter
#        for my_col_counter, col in enumerate(first_bad_line):
#            print my_col_counter, col
#        break
#myfile.close()

## Define function to clean data, input file (reading), output file (writing)
def clean_data(myinputfile, myoutputfile):
    inf = open(myinputfile, 'r')
    outf = open(myoutputfile, 'wb')
    
    for line in inf: # go through each line in the input file
        splitline = line.split(';') # Split the data into columns based on a delimiter, splitline is a list
        if len(splitline)==numcolumns-1: # Check if the length of the list is the number of columns.  Keep in mind lists go from 0, 1, 2, etc.  See below about how strings/lists is treated
            continue
        ## Below describes how a string is treated in Python
        ''' Suppose a string s contained 'Hello'

            H  e  l  l  o
            0  1  2  3  4

            s[0]='H', s[1]='e', s[2]='l', s[3]='l', s[4]='o' # chars starting at index 0
            s[1:4]='ell'  # chars starting at 1 and extending up to, but not including 4
            s[1:]='ello'  # omits either index defaults to the start or end of the string
            s[:]='Hello'  # omitting both always gives a copy of the whole thing
            s[1:100]='ello' # an index that is too big is truncated down to the string length


            H   e  l  l  o
            -5 -4 -3 -2 -1
            
            s[-1]='o'   # last char (1st from the end) as in Hello
            s[-4]='e'   # 4th char from the end
            s[:-3]='He'  # going up to, but not including the last 3 chars
            s[-3:]='llo'    # starting with the 3rd char from the end and extending to the end of the string
        '''

        ## Join the three splitlines using delimiter ';'.  If after X columns there isn't a newline, we add one
        ## Remove "
        ## We then write the line to the output file
        newline = (';').join(splitline[:numcolumns]).replace('"', '')
        if newline[-1: ] != '\n':
            newline += '\n'
        outf.write(newline)
           

    ## Close the input file and the output file
    inf.close()
    outf.close()

## Run the custom defined clean_data function (see above) to clean data
clean_data(myinputfile, myoutputfile)

## Print out file, header is at row 0
mydata = pandas.io.parsers.read_table(myoutputfile, sep = '\n', header=0)

## Print first 50 items to see if it matches
print mydata.head(50)

## Using Pandas dataframe, convert " to ''
#mydata.replace('"',' ')

## Export Pandas dataframe to outputfile
#mydata.to_csv(myoutputfile)

## Print first 50 items to see if it matches
#print mydata.head(50)

