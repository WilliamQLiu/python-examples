# -*- coding: cp1252 -*-
# Import modules
import csv
import numpy
import pandas # For Data frames
import datetime, time
import pyodbc # For ODBC
import string # For String Template
#import urllib # To interpret text to UTF-8 encoded text (or else "'" gives errors)

# Declare input and output files
myinputfilelocation = 'iCarolExportLarge.csv' # Get File Input Path
myoutputfilelocation = 'iCarolExportLargeOutput.csv' # Get File Output Path
myinputfile = open(myinputfilelocation, 'rb')
myoutputfile = open(myoutputfilelocation, 'wb')

# Skip lines until you reach the header
myinputfile.next() #Skip first row
myinputfile.next() #Skip second row, header on third row

# Take inputfile, read through all, clean out quotes (since some of the raw data has quotes inside), then write to output file
for line in myinputfile:
    try:
        newline = unicode(line, errors='replace')
    except UnicodeDecodeError:
        print("Decode Error")
    newline = newline.encode('latin-1', errors='replace')
    myoutputfile.write(newline)
myinputfile.close()
myoutputfile.close()

"""List columns"""
v0 = u"CallReportNum"
v1 = u"ReportVersion"
v2 = u"CallDateAndTimeStart"
v3 = u"CallDateAndTimeEnd"
v4 = u"CallLength"
v5 = u"CityName"
v6 = u"CountyName"
v7 = u"StateProvince"
v8 = u"PostalCode"
v9 = u"PhoneNumberFull"
v10 = u"Call Information - Caller is:"
v11 = u"Call Information - How caller heard about hotline"
v12 = u"Call Information - Incoming Line"
v13 = u"Call Information - Noteworthy call"
v14 = u"Call Information - Type of Call"
v15 = u"Client Demographics - Age Group"
v16 = u"Client Demographics - Gender"
v17 = u"Client Demographics - Language"
v18 = u"Clients MH and SA concerns/treatment - Alcohol and/or drug abuse"
v19 = u"Clients MH and SA concerns/treatment - Alcohol and/or drug abuse/Gambling"
v20 = u"Client???s MH and SA concerns/treatment - Alcohol and/or drug abuse"
v21 = u"Clients MH and SA concerns/treatment - Mental Health Concerns - Primary"
v22 = u"Client???s MH and SA concerns/treatment - Mental Health Concerns - Primary"
v23 = u"Client???s MH and SA concerns/treatment - Highest level of care (MH)"
v24 = u"Clients MH and SA concerns/treatment - Highest level of care (MH)"
v25 = u"EMS - EMS Referral Made"
v26 = u"EMS - Hospital Name"
v27 = u"Follow-up Detail - 1. How helpful did you find the information provided during your initial call?"
v28 = u"Follow-up Detail - 2. How likely are you to refer a friend or family member in need of help to this line? "
v29 = u"Follow-up Detail - Barriers to Treatment"
v30 = u"Follow-up Detail - Progress towards treatment"
v31 = u"Gambling - How Caller heard about Hopeline - Gambling"
v32 = u"Gambling - Primary Gambling Problem"
v33 = u"MCT - MCT Name"
v34 = u"MCT - MCT Referral Made"
v35 = u"Substance Abuse - How Caller heard about Hopeline - Substance Abuse"
v36 = u"Substance Abuse - Primary Substance currently abusing"
v37 = u"Third Party Information - Relationship"
v38 = u"ReferralsMade"
v39 = u"Assessments Needed - Assessments Needed"
v40 = u"Client Assessment - Attitude"
v41 = u"Client Assessment - Functional "
v42 = u"Client Assessment - Mood"
v43 = u"Client Assessment - Speech"
v44 = u"Client Assessment - Thought Content"
v45 = u"Risk Assessment - Actively Suicidal"
v46 = u"Referrals - Type of Referral Provided"

mylist = [v0, v1, v2, v3, v4, v5, v6, v7, v8, v9, v10, v11, v12, v13, v14, v15, v16, v17, v18, v19, v20, v21, v22, v23, v24, v25, v26, v27, v28, v29, v30, v31, v32, v33, v34, v35, v36, v37, v38, v39, v40, v41, v42, v43, v44, v45, v46]

# Get new output file, then read the csv into a pandas data frame
mynewoutputfile = 'iCarolExportLargeOutput.csv' 
mydataframe = pandas.io.parsers.read_table(mynewoutputfile, sep=',', quotechar='"', header=0, index_col=0, error_bad_lines=True, warn_bad_lines=True, encoding='latin-1') # , encoding='utf-8', encoding='latin-1', warn_bad_lines=False, names=['CallReportNum','ReportVersion', 'CallDateAndTimeStart'], index_col=False, escapechar='\n', names=['CallReportNum','ReportVersion', 'CallDateAndTimeStart'], index_col=False, escapechar='\n'

# Get back clean data frame consisting of only the columns we want
dfclean = pandas.DataFrame(data=mydataframe, columns=mylist)  #print dfclean[mylist[3]]

def mergecolumns(column1, column2):
    """Takes in column names and merges, uses the name of the first column"""
    pieces = [dfclean[column1].dropna(), dfclean[column2].dropna()] # Get two columns, drop any missing values (appears as 'NaN')
    concatenated = pandas.concat(pieces) # Concatenate two columns
    dfaddon = pandas.DataFrame(concatenated) # Put concatenated columns into its own data frame
    dffinal = dfclean.join([dfaddon]) # Join the two data frames
    dffinal = dffinal.drop([column1, column2], axis=1) # Drop the additional columns of messy data
    dffinal = dffinal.rename(columns={0:column1})  # Rename new column '0' to new name
    return dffinal

# Clean up data
dfclean = mergecolumns(mylist[24], mylist[23]) # Removes Client???s MH and SA concerns/treatment - Highest level of care (MH)
dfclean = mergecolumns(mylist[19], mylist[18]) # Removes Clients MH and SA concerns/treatment - Alcohol and/or drug abuse
dfclean = mergecolumns(mylist[19], mylist[20]) # Removes Client???s MH and SA concerns/treatment - Alcohol and/or drug abuse
dfclean = mergecolumns(mylist[21], mylist[22]) # Removes Client???s MH and SA concerns/treatment - Mental Health Concerns - Primary
print dfclean

dfclean = dfclean.drop(u"CallReportNum", axis=1)
dfclean.to_csv('iCarolExportOutputClean.csv')
