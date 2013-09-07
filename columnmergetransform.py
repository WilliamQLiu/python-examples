# -*- coding: cp1252 -*-
# Import modules
import csv
import numpy
import pandas # For Data frames
import datetime, time
import csv
import pyodbc # For ODBC
import string # For String Template
#import urllib # To interpret text to UTF-8 encoded text (or else "'" gives errors)

# Declare input and output files
#myinputfilelocation = 'iCarolExportSubset.csv' # Get File Input Path # ExportSubset.csv was for testing smaller chunks of data
myinputfilelocation = 'iCarolExportLarge.csv' # Get File Input Path
myoutputfilelocation = 'iCarolExportLargeOutput.csv' # Get File Output Path
myinputfile = open(myinputfilelocation, 'rb')
#myinputfile = codecs.open(myinputfilelocation, 'r', encoding='utf-8')
myoutputfile = open(myoutputfilelocation, 'wb')

### Data Cleaning - Remove extra " characters since iCarol has extras

# Skip lines until you reach the header
myinputfile.next() #Skip first row
myinputfile.next() #Skip second row, header on third row

# Take inputfile, read through all, clean out quotes (since some of the raw data has quotes inside), then write to output file
for line in myinputfile:
    #print type(line) # Type is string 
    try:
        newline = unicode(line, errors='replace')
    except UnicodeDecodeError:
        print("Decode Error")
    newline = newline.encode('latin-1', errors='replace')
    #newline = line.encode('latin-1', errors='ignore')
    myoutputfile.write(newline)
    #line.decode('utf-8', errors='ignore') # To get rid of weird encoding for characters like '
    #line.decode('latin-1', errors='ignore') # To get rid of weird encoding for characters like '
    #line.decode('iso-8859-1')
    #line = line.replace('’', "").strip()
    #myoutputfile.write(line)
    #myoutputfile.write('\n')
    #print line
myinputfile.close()
myoutputfile.close()

v1 = u"CallReportNum"
v2 = u"ReportVersion"
v3 = u"CallDateAndTimeStart"
v4 = u"CallDateAndTimeEnd"
v5 = u"CallLength"
v6 = u"CityName"
v7 = u"CountyName"
v8 = u"StateProvince"
v9 = u"PostalCode"
v10 = u"PhoneNumberFull"
v11 = u"Call Information - Caller is:"
v12 = u"Call Information - How caller heard about hotline"
v13 = u"Call Information - Incoming Line"
v14 = u"Call Information - Noteworthy call"
v15 = u"Call Information - Type of Call"
v16 = u"Client Demographics - Age Group"
v17 = u"Client Demographics - Gender"
v18 = u"Client Demographics - Language"
v19 = u"Clients MH and SA concerns/treatment - Alcohol and/or drug abuse"
v20 = u"Clients MH and SA concerns/treatment - Alcohol and/or drug abuse/Gambling"
v21 = u"Client???s MH and SA concerns/treatment - Alcohol and/or drug abuse"
v22 = u"Clients MH and SA concerns/treatment - Mental Health Concerns - Primary"
v23 = u"Client???s MH and SA concerns/treatment - Mental Health Concerns - Primary"
v24 = u"Client???s MH and SA concerns/treatment - Highest level of care (MH)"
v25 = u"Clients MH and SA concerns/treatment - Highest level of care (MH)"
v26 = u"EMS - EMS Referral Made"
v27 = u"EMS - Hospital Name"
v28 = u"Follow-up Detail - 1. How helpful did you find the information provided during your initial call?"
v29 = u"Follow-up Detail - 2. How likely are you to refer a friend or family member in need of help to this line? "
v30 = u"Follow-up Detail - Barriers to Treatment"
v31 = u"Follow-up Detail - Progress towards treatment"
v32 = u"Gambling - How Caller heard about Hopeline - Gambling"
v33 = u"Gambling - Primary Gambling Problem"
v34 = u"MCT - MCT Name"
v35 = u"MCT - MCT Referral Made"
v36 = u"Substance Abuse - How Caller heard about Hopeline - Substance Abuse"
v37 = u"Substance Abuse - Primary Substance currently abusing"
v38 = u"Third Party Information - Relationship"
v39 = u"ReferralsMade"

myfullschema = [v1, v2, v3, v4, v5, v6, v7, v8, v9, v10, v11, v12, v13, v14, v15, v16, v17, v18, v19, v20, v21, v22, v23, v24, v25, v26, v27, v28, v29, v30, v31, v32, v33, v34, v35, v36, v37, v38, v39]

### Read Stripped Data into Data Frame
mynewoutputfile = 'iCarolExportLargeOutput.csv' # Get new output file, then read the csv into a pandas data frame, #mynewoutputfile = codecs.open('iCarolExportSmallOutput.csv', 'r', encoding='utf-8')

mydataframe = pandas.io.parsers.read_table(mynewoutputfile, sep=',', quotechar='"', header=0, index_col=0, error_bad_lines=True, warn_bad_lines=True, encoding='latin-1') # , encoding='utf-8', encoding='latin-1', warn_bad_lines=False, names=['CallReportNum','ReportVersion', 'CallDateAndTimeStart'], index_col=False, escapechar='\n', names=['CallReportNum','ReportVersion', 'CallDateAndTimeStart'], index_col=False, escapechar='\n'
#mydataframe['ReferralsMade']
#mydataframe.to_csv('iCarolTest.csv')
#print mydataframe.columns

## For Testing
#print mydataframe.columns #Print out all column names
#print mydataframe[v25] # Print out specific column

#mydataframe2 = pandas.DataFrame(data = mydataframe, columns=[v1, v2, v3, v4, v5, v6, v7, v8, v9, v10, v11, v12, v13, v14, v15, v16, v17, v18, v19, v20, v21, v22, v23, v24, v25, v26, v27, v28, v29, v30, v31, v32, v33, v34, v35, v36, v37, v38])
#print mydataframe2
#dfclean = [v1, v2, v3, v4, v5, v6, v7, v8, v9, v10, v11, v12, v13, v14, v15, v16, v17, v18, v26, v27, v28, v29, v30, v31, v32, v33, v34, v35, v38]

dfclean = pandas.DataFrame(data=mydataframe, columns = [v1, v2, v3, v4, v5, v6, v7, v8, v9, v10, v11, v12, v13, v14, v15, v16, v17, v18, v26, v27, v28, v29, v30, v31, v32, v33, v34, v35, v38, v39])
#pieces = [mydataframe[u"Client???s MH and SA concerns/treatment - Highest level of care (MH)"].dropna(), mydataframe[u"Clients MH and SA concerns/treatment - Highest level of care (MH)"].dropna()]
pieces = [mydataframe[v24].dropna(), mydataframe[v25].dropna()]
concatenated = pandas.concat(pieces) # Concatenate two columns
dfaddon = pandas.DataFrame(concatenated) # Put concatenated columns into its own data frame
dffinal = dfclean.join([dfaddon]) # Join the two data frames
dffinal.columns = [v1, v2, v3, v4, v5, v6, v7, v8, v9, v10, v11, v12, v13, v14, v15, v16, v17, v18, v26, v27, v28, v29, v30, v31, v32, v33, v34, v35, v38, v39, 'Clients MH and SA concerns/treatment - Highest level of care (MH)'] # Rename column names (otherwise concatenated column names are '0')
#print dffinal

## ["Clients MH and SA concerns/treatment - Alcohol and/or drug abuse"] and ["Clients MH and SA concerns/treatment - Alcohol and/or drug abuse/Gambling"]
dfclean = dffinal
pieces = [mydataframe[v19].dropna(), mydataframe[v20].dropna()]
concatenated = pandas.concat(pieces) # Concatenate two columns
dfaddon = pandas.DataFrame(concatenated) # Put concatenated columns into its own data frame
dffinal = dfclean.join([dfaddon]) # Join the two data frames
dffinal.columns = [v1, v2, v3, v4, v5, v6, v7, v8, v9, v10, v11, v12, v13, v14, v15, v16, v17, v18, v26, v27, v28, v29, v30, v31, v32, v33, v34, v35, v38, v39, 'Clients MH and SA concerns/treatment - Highest level of care (MH)', "Clients MH and SA concerns/treatment - Alcohol and/or drug abuse"] # Rename column names (otherwise concatenated column names are '0')
#print dffinal

## ["Clients MH and SA concerns/treatment - Mental Health Concerns - Primary"] and ["Client’s MH and SA concerns/treatment - Mental Health Concerns - Primary"]
dfclean = dffinal
pieces = [mydataframe[v22].dropna(), mydataframe[v23].dropna()]
concatenated = pandas.concat(pieces) # Concatenate two columns
dfaddon = pandas.DataFrame(concatenated) # Put concatenated columns into its own data frame
dffinal = dfclean.join([dfaddon]) # Join the two data frames
#dffinal = dffinal.rename(columns={"$0":"Clients MH and SA concerns/treatment - Mental Health Concerns - Primary"}, inplace=True)
dffinal.columns = [v1, v2, v3, v4, v5, v6, v7, v8, v9, v10, v11, v12, v13, v14, v15, v16, v17, v18, v26, v27, v28, v29, v30, v31, v32, v33, v34, v35, v38, v39, 'Clients MH and SA concerns/treatment - Highest level of care (MH)', "Clients MH and SA concerns/treatment - Alcohol and/or drug abuse", "Clients MH and SA concerns/treatment - Mental Health Concerns - Primary"] # Rename column names (otherwise concatenated column names are '0')
print dffinal

dffinal.to_csv('iCarolExportOutputClean.csv')
#print dffinal

### Use below to write data to the database

## Use cursor to execute a SQL statement using cursor.execute function
##cursor.execute("SELECT TOP 50 [Microboard],[DateTime],[Date],[Month],[Day],[Time],[TextNumber],[Data] FROM [DataWarehouse].[dbo].[DDHTexts]")
#''' Note: A lot of SQL statements don't fit on one line easily so you can use triple quoted strings around the selection
#    E.g. cursor.execute(""" SELECT TOP 50
#                        [Microboard],[DateTime],[Date],
#                        [Month],[Day],[Time],[TextNumber],[Data]
#                        FROM [DataWarehouse].[dbo].[DDHTexts]""")
#'''

## Below describes what fetching options are available
#''' If a SQL statement returns rows (e.g. SELECT statement), you can retrieve them using the following Cursor fetch functions
#  fetchone - returns first row, otherwise returns 'None'
#  fetchall - returns all rows in a list, otherwise returns an empty list
#  fetchmany - returns a list of remaining rows
#  Note: Row objects in pyodbc are similar to tuples, but they also allow access to columns by name
#  print 'name:', row[1]
#  print 'name:', row.user_name
#'''
### Connect to ODBC

#cnxn = pyodbc.connect('DRIVER={SQL Server};SERVER=LL-SQL-PI01;DATABASE=DataWarehouse;UID=sa;PWD=enterpassword') #Make a direct connection to a database
#cursor = cnxn.cursor()

#myquery1 = [v1, v2, v3, v4, v5, v6, v7, v8, v9, v10, v11, v12, v13, v14, v15, v16, v17, v18, v26, v27, v28, v29, v30, v31, v32, v33, v34, v35, v38, 'Clients MH and SA concerns/treatment - Highest level of care (MH)', "Clients MH and SA concerns/treatment - Alcohol and/or drug abuse", "Clients MH and SA concerns/treatment - Mental Health Concerns - Primary"]
#cursor.execute("INSERT INTO WillTest(ID, FirstName, LastName) VALUES(?, ?, ?)", '100', 'William','Liu')

## Check if a table exists
#if cursor.tables(table='WillTest').fetchone():
#    print 'Yes, a table exists.  Inserting SQL'
#    count = 0
#    for x in dffinal.iterrows(): # Go through all the rows
        #a = int(pandas.Series(data=dffinal['CallReportNum']).index[0]) # Select row by index label and column   #NEED TO MODIFY HERE FOR index[x]
#        q1 = int(pandas.Series(data=dffinal['CallReportNum']).index[count]) # Select row by index label and column   #NEED TO MODIFY HERE
#        count+=1
#        q2 = str(dffinal.loc[q1,'ReportVersion']) #ReportVersion, #q2 = str(dffinal.loc[q1,'ReportVersion'])
#        #q3 = datetime.strptime(str(dffinal.loc[q1,v3]), "%Y, %m, %d, %H, %M, %S") #CallDateAndTimeStart, #q3 = str(dffinal.loc[q1,'CallDateAndTimeStart']) # DATE TIME NOT WORKING
#        #q4 = datetime.strptime(str(dffinal.loc[q1,v4]), "%Y, %m, %d, %H, %M, %S") #CallDateAndTimeEnd, #q4 = str(dffinal.loc[q1,'CallDateAndTimeEnd']) # DATE TIME NOT WORKING
#        q5 = int(dffinal.loc[q1,'CallLength']) #CallLength, #q5 = str(dffinal.loc[q1,'CallLength'])
#        q6 = str(dffinal.loc[q1,'CityName']) #CityName, #q6 = str(dffinal.loc[q1,'CityName'])
#        cursor.execute(""" INSERT INTO WillTest(CallReportNum, ReportVersion, CallLength, CityName, CountyName) VALUES(?,?,?,?,?)""", q1, q2, q5, q6, q7)
#else:
#    print 'No, a table does not exist, but we will create one!  Run program again to populate values.'
#    cursor.execute(""" CREATE TABLE WillTest(
#                       CallReportNum varchar(50), ReportVersion varchar(50), CallLength int, CityName varchar(50), CountyName varchar(50)
#                       )""")
#    cnxn.commit() # Must commit changes or else does not work
#                       FROM [DataWarehouse].[dbo].[WillTest]
#                       """)
#    ## Go through the cursor and print out all files
#    #for rowcounter in cursor:
#    #    print rowcounter.CallReportNum, rowcounter.CityName, rowcounter.CountyName
#
#mysqlstatement = "INSERT INTO iCarolAllData(%s, %s, %s) VALUES(?, ?, ?)" %tuple(myquerytest)
#mysqlstatement = "INSERT INTO iCarolAllData(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s) VALUES(?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)" %tuple(myquery1)
#print mysqlstatement

# Do SQL Insert
     #cursor.execute(mysqlstatement, '123456', 'LifeNet', '2013-09-01 00:00:00.000', '2013-09-01 00:00:00.000', '77')
     #cursor.execute(mysqlstatement)
#cnxn.commit() # Must commit changes or else does not work

