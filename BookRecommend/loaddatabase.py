### Import csv data using third party modules, clean data, and output to a ODBC destination (e.g. SQL Server)

## Import modules
import numpy
import pandas
import datetime
import time
import csv

### Set important settings about the file
myinputfile = 'BX-Book-Ratings-Output.csv'  # Load myinputfile with data
myoutputfile = 'BX-Book-Ratings-Output-Database.csv' # Set File Output Path

## Creates dataframe mydata, header is at row 1
mydata = pandas.io.parsers.read_table(myinputfile, sep = '\n', quotechar='"', header=1, )

## Print first 50 items to see if it matches
print mydata.head(50)

## Export Pandas dataframe to outputfile
#mydata.to_csv(myoutputfile)

# ********************************************************************************************************* #

### Connect to a database (for this instance, a Microsoft SQL Server 2008 R2), write data
### Documenation from: https://code.google.com/p/pyodbc/wiki/GettingStarted
import pyodbc

## Make a direct connection to a database and create a cursor
#cnxn = pyodbc.connect('DRIVER={SQL Server};SERVER=WILL-PC\SQLEXPRESS;DATABASE=BookDatabase;UID=Will-PC\Will;PWD=')
cnxn = pyodbc.connect('DRIVER={SQL Server};SERVER=WILL-PC\SQLEXPRESS;DATABASE=BookDatabase;Trusted_Connection=yes')
cursor = cnxn.cursor()

## Check if a table exists
if cursor.tables(table='BX-Book-Ratings-Output').fetchone():
    print 'Yes, a table exists.  Populating table with data'
    cursor.execute(""" BULK INSERT
                       [BX-Book-Ratings-Output] FROM 'C:\Python27\BX-Book-Ratings-Output.csv'
                       WITH( FIELDTERMINATOR = ';', ROWTERMINATOR = '\n')
                       """)
    cursor.commit()
#    cursor.execute(""" SELECT *
#                       FROM [BookDatabase].[dbo].[BX-Book-Ratings-Output]
#                       """)
#    cursor.commit()
#    for rowcounter in cursor:
#        print rowcounter.User-ID, rowcounter.ISBN, rowcounter.Book-Rating
#    cursor.description

else:
    print 'No, a table does not exist, but we will create one!'
    cursor.execute(""" CREATE TABLE [BX-Book-Ratings-Output](
                       [User-ID] varchar(50), [ISBN] varchar(50), [Book-Rating] varchar(50)
                       )""")
    cnxn.commit() # Must commit changes or else does not work
#    cursor.execute(""" SELECT *
#                       FROM [BookDatabase].[dbo].[BX-Book-Ratings-Output]
#                       """)
#    ## Go through the cursor and print out all files
#    for myrowcounter in cursor:
#        print myrowcounter.User-ID, myrowcounter.ISBN, myrowcounter.Book-Rating

