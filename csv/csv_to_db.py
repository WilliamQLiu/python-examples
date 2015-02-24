"""
    Load a csv file into a MS SQL Server database, write line by line into
    specific tables.  Multiple tables are written to make normalized tables
"""

import pandas as pd
import numpy as np
try:
    import unicodecsv as csv  # for UTF8Recoder, UnicodeReader, UnicodeWriter
except ImportError:
    import warnings
    warnings.warn("can't import `unicodecsv` lib, encoding errors may occur")
    import csv
import pyodbc
# Optional libraries below for debugging and progress bar
import pdb  # Debugging Purposes
import pyprind as pp  # Used for Progress Bar  TODO
import time  # Used for Progress Bar


# ODBC Database Settings
DB_DRIVER = '{SQL Server}'
DB_SERVER = 'servername'
DB_DATABASE = 'dbname'
DB_UID = 'username'
DB_PWD = 'password'
DB_CONN = ('DRIVER=' + DB_DRIVER + ';'
           + 'SERVER=' + DB_SERVER + ';'
           + 'DATABASE=' + DB_DATABASE + ';'
           + 'UID=' + DB_UID + ';' +'PWD=' + DB_PWD)


class FileWriter(object):
    """ Class to read file while coming up with metadata """
    message_loading = "Loading ... "  # class variable shared by all instances

    def __init__(self, mydf, mydb, mytbl):
        """
            Initialized attributes, these vars are unique to each instance.
            Give dataframe, database connection, table
        """
        self._file = None  # get file
        self._db = mydb  # db connection strings
        self._tbl = mytbl  # table name
        self._df = mydf
        self._header = None  # which columns used (list 'all' or select)
        self._cur_line = 0  # current line in file
        self._errors = 0  # number of errors generated from loading
        self.clean_data()  # clean data
        self.load_data()  # load data from csv, write to database
        self.summary_stats()  # print summary stats

    def clean_data(self):
        """ Clean data with a temp file, add additional data cleaning here """
        print "Cleaning data..."
        TEMP_NAME = "temp.csv"
        temp_df = self._df
        temp_df.drop_duplicates(inplace=True)  # Remove dups for normalizing
        temp_df.to_csv(TEMP_NAME, index=False)
        self._file = TEMP_NAME  # Use the cleaned up temp file

    def load_data(self):
        """
            Get file contents and write data to database

            Query looks like:
            query = 'insert into mydatabase.dbo.SomeTable({0}) values ({1})'

            Query format looks like:
            query = 'insert into mydatabase.dbo.SomeTable(CallReportNum,
                     DateOfCall, CategoryNum, CategoryName, SubCategoryNum,
                     SubCategoryName, AnswerNum, Answer, TextAnswer, GeoCode,
                     GeoAssignment') values (?,?,?,?,?,?,?,?,?,?,?)
        """
        with open(self._file, 'rU') as data:  # ensures file closed properly
            print "Writing file to database"
            reader = csv.reader(data)  # <unicodecsv.UnicodeReader object>
            self._header = next(reader)  # get the column headers

            # Setup query
            query = 'insert into ' + DB_DATABASE + '.dbo.' + self._tbl + '({0}) values ({1})'
            query = query.format(','.join(self._header), ','.join('?' * len(self._header)))

            connection = pyodbc.connect(self._db)
            cursor = connection.cursor()

            try:
                for row in reader:

                    # Debugging purposes
                    print row
                    #print "Line number " , self._cur_line
                    #print row  # row is a list of column params
                    #pdb.set_trace()

                    # Write to database
                    cursor.execute(query, row)  # Run each query line by line
                    self._cur_line += 1
            except:
                print "Error with line: ", self._cur_line
                raise
                self._errors += 1
            cursor.commit()  # save the query
        data.close()  # close data conn in case contxt manager hasn't

    def summary_stats(self):
        print self._file + " was loaded onto " + self._db + " " + self._tbl
        print "Number of lines written: ", self._cur_line
        print "Number of errors: ", self._errors


if __name__ == "__main__":

    # Location of our downloaded file from icarol system
    FILE_PATH = "C:\mylocation\\"
    FILE_NAME = "load_me.csv"
    FILE = FILE_PATH + FILE_NAME

    # Write table - Exact replica of file download, use if non-normalized okay
    df = pd.read_csv(filepath_or_buffer=FILE, sep=',', skiprows=2)
    reader = FileWriter(df, DB_CONN, mytbl='iCarolRelAll')


    # Write main table of basic info, link to Categories and Answers Table
    df = pd.read_csv(filepath_or_buffer=FILE, sep=',', skiprows=2,
                     usecols=['CallReportNum', 'DateOfCall', 'CategoryNum',
                              'SubCategoryNum', 'AnswerNum', 'GeoCode',
                              'GeoAssignment', 'TextAnswer'],
                     dtype={'AnswerNum': np.float64})
    reader = FileWriter(df, DB_CONN, mytbl='iCarolRelMain')

    # Write Categories Table
    df = pd.read_csv(filepath_or_buffer=FILE, sep=',', skiprows=2,
                     usecols=['CategoryNum', 'CategoryName'])
    reader = FileWriter(df, DB_CONN, mytbl='iCarolRelCat')

    # Write SubCategories Table
    df = pd.read_csv(filepath_or_buffer=FILE, sep=',', skiprows=2,
                     usecols=['SubCategoryNum', 'SubCategoryName'])
    reader = FileWriter(df, DB_CONN, mytbl='iCarolRelSubCat')

    # Write Answer Table
    df = pd.read_csv(filepath_or_buffer=FILE, sep=',', skiprows=2,
                     usecols=['AnswerNum', 'Answer'],
                     dtype={'AnswerNum': np.float64})
    reader = FileWriter(df, DB_CONN, mytbl='iCarolRelAns')
