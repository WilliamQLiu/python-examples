#!/usr/bin/python
# -*- coding: utf-8 -*-
# pylint: disable=I0011,C0103,W0142

"""Import Modules"""
### Standard Library Modules
import csv # For CSV
import os # For filepaths
import ftplib # Implements the client side of the FTP protocol
#import pdb # Can be invoked as a script: python -m pdb ETLiCarol.py
import codecs

### Third-Party Library Modules
import pandas # For Data frames
import pyodbc # For ODBC
import sqlalchemy
#import numpy # Needed for pandas
#import fnmatch # to check filename pattern
#import string # For String Template
#import datetime, time
import pdb

### Locally-Developed Modules
import settings


###Specify directories

# PC
#originaldirectory = str(r'C:\iCarolFTPFiles\Original')
#cleandirectory = str(r'C:\iCarolFTPFiles\Clean')

# Mac
originaldirectory = str(r'/Users/williamliu/Documents/Lifeline/Original')
cleandirectory = str(r'/Users/williamliu/Documents/Lifeline/Clean')

os.chdir(originaldirectory) #Change Local directory (where files go to)
myfilename = 'iCarolExportClean.csv'

#Get filenames from directories to two lists, 'Original' and 'Clean'
od = [] #Holds list of all filenames that have been downloaded from FTP
cd = [] #Holds list of all filenames that have been cleaned
table = None

#Explicitly list columns from file that we want to keep
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
v27 = u"Follow-up Detail - 1. How helpful was your initial call?"
v28 = u"Follow-up Detail - 2. How likely are you to refer a friend or family member in need of help to this line? "
v29 = u"Follow-up Detail - Barriers to Treatment"
v30 = u"Follow-up Detail - Connected to Treatment or pending appointment"
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
v45 = u"Risk Assessment - Actively Suicidal Ideation within the last 2 days"
v46 = u"Referrals - Type of Referral Provided"
v47 = u"PhoneWorkerName"
v48 = u"NFL Caller Information - NFL Caller is:"
v49 = u"Risk Assessment - Thoughts of suicide in the last 2 months?"
v50 = u"Risk Assessment - Active Suicidal Ideation within the last 2 days"
v51 = u"Client???s MH and SA concerns/treatment - Alcohol and/or drug abuse/Gambling"
v52 = u"Risk Assessment - Passive Suicidal Ideation within the last 2 days"
v53 = u"Risk Assessment - Actively Suicidal"
#v54 = u"Registration - If you completed the Self-Check Quiz please provi"
v54 = u"Registration - If you completed the Self-Check Quiz please provide your Reference Number.<br/>Reference Number:"
v55 = u"Risk Assessment - Actively Homicidal"
# Updated below on: 8/27/2014
v56 = u"CallerName"
v57 = u"CallerLastName"
v58 = u"Client Demographics - D.O.B."
v59 = u"Third Party Information - Name"
v60 = u"Access to Treatment - Ability to access Treatment"
v61 = u"MCT Referral made - Current medical conditions/allergies"
v62 = u"MCT Referral made - Health Insurance Provider"
# Updated below on: 10/3/2014
v63 = u"Follow-up Only - Client contact made"
v64 = u"Follow-up Detail - Follow-Up Step"
v65 = u"Follow-up Detail - Follow-up Outcomes"
v66 = u"Follow-up Detail - Further Follow-up required?"
v67 = u"Follow-up Detail - Post-Lethality on a scale of 1-5 How likely are you to act on this plan?"
v68 = u"Client Demographics - If not English Translation Service Required?"
v69 = u"Risk Assessment - Lethality on a scale of 1-5 How likely are you to act on this plan?"
v70 = u"Follow-up Detail - 1. Was this Follow Up call helpful in keeping you safe? "


mylist = [v0, v1, v2, v3, v4, v5, v6, v7, v8, v9, v10, v11, v12, v13, v14, v15,
        v16, v17, v18, v19, v20, v21, v22, v23, v24, v25, v26, v27, v28, v29,
        v30, v31, v32, v33, v34, v35, v36, v37, v38, v39, v40, v41, v42, v43,
        v44, v45, v46, v47, v48, v49, v50, v51, v52, v53, v54, v55, v56, v57,
        v58, v59, v60, v61, v62, v63, v64, v65, v66, v67, v68, v69, v70]

def create_table():
    """Connect to Server"""
    cnxn = pyodbc.connect(settings.pyodbc_connection)
    #Make a direct connection to a database
    cursor = cnxn.cursor()
    cursor.execute("""CREATE TABLE iCarol(
            CallReportNum nvarchar(255),
            ReportVersion nvarchar(255),
            CallDateAndTimeStart datetime,
            CallDateAndTimeEnd datetime,
            CallLength float,
            CityName nvarchar(255),
            CountyName nvarchar(255),
            StateProvince nvarchar(255),
            PostalCode float,
            PhoneNumberFull float,
            [Call Information - Caller is:] nvarchar(255),
            [Call Information - How caller heard about hotline] nvarchar(255),
            [Call Information - Incoming Line] nvarchar(255),
            [Call Information - Noteworthy call] nvarchar(255),
            [Call Information - Type of Call] nvarchar(255),
            [Client Demographics - Age Group] nvarchar(255),
            [Client Demographics - Gender] nvarchar(255),
            [Client Demographics - Language] nvarchar(255),
            [EMS - EMS Referral Made] nvarchar(255),
            [EMS - Hospital Name] nvarchar(255),
            [Follow-up Detail - 1. How helpful did you find the information provided during your initial call?] nvarchar(255),
            [Follow-up Detail - 2. How likely are you to refer a friend or family member in need of help to this line? ] nvarchar(255),
            [Follow-up Detail - Barriers to Treatment] nvarchar(255),
            [Follow-up Detail - Progress towards treatment] nvarchar(255),
            [Gambling - How Caller heard about Hopeline - Gambling] nvarchar(255),
            [Gambling - Primary Gambling Problem] nvarchar(255),
            [MCT - MCT Name] nvarchar(255),
            [MCT - MCT Referral Made] nvarchar(255),
            [Substance Abuse - How Caller heard about Hopeline - Substance Abuse] nvarchar(255),
            [Substance Abuse - Primary Substance currently abusing] nvarchar(255),
            [Third Party Information - Relationship] nvarchar(255),
            [ReferralsMade] nvarchar(2048),
            [Assessments Needed - Assessments Needed] nvarchar(255),
            [Client Assessment - Attitude] nvarchar(255),
            [Client Assessment - Functional ] nvarchar(255),
            [Client Assessment - Mood] nvarchar(255),
            [Client Assessment - Speech] nvarchar(255),
            [Client Assessment - Thought Content] nvarchar(255),
            [Risk Assessment - Actively Suicidal] nvarchar(255),
            [Referrals - Type of Referral Provided] nvarchar(255),
            [Clients MH and SA concerns/treatment - Highest level of care (MH)] nvarchar(255),
            [Clients MH and SA concerns/treatment - Alcohol and/or drug abuse] nvarchar(255),
            [Clients MH and SA concerns/treatment - Mental Health Concerns - Primary] nvarchar(255),
            [Referrals - Type of Referral Provided] nvarchar(255),
            [PhoneWorkerName] nvarchar(255),
            [NFL Caller Information - NFL Caller is:] nvarchar(255),
            [Risk Assessment - Thoughts of suicide in the last 2 months?] nvarchar(255),
            [Risk Assessment - Suicidal Ideation within the last 2 days] nvarchar(255),
            [Registration - If you completed the Self-Check Quiz please provide your Reference Number.<br/>Reference Number:] nvarchar(255),
            [Risk Assessment - Actively Homicidal] nvarchar(255)
            )""")
    cnxn.commit() #Must commit changes or else does not work
    cnxn.close()
    print "Creating Table; check that table is correct, rerun script for import"

def import_ftp_files():
    """ Loop through matching files and download each one individually;
    if file exists and has content already then the process skips the download,
    otherwise the process downloads files from ftp to local directory"""
    print "Connected!  Searching files"

    #Create an FTP instance and setup local directory using  settings.py
    ftp = ftplib.FTP(settings.HOSTNAME) #Connect to Host
    ftp.login(settings.USERNAME, settings.PASSWORD) #Login
    ftp.cwd(settings.ftpdirectory) #Change FTP's dir (where files come from)
    ftp.set_pasv(False) #Set to Active Mode instead of Passive Mode
            # (or else the program stutters writing files)
    os.chdir(originaldirectory) #Change Local directory (where files go to)

    files = []
    #Get File Name, specifically the date portion, add date to a List
    for filename in ftp.nlst(settings.filematch): #Return a list of file names
        filenamedate = filename[43:51]
        #Get File Name in Format: YYYYMMDD, e.g. 20130531
        files.append(filenamedate)
        mypath = os.path.join(originaldirectory, filename)
        #Get complete file path and file name

        #If file does not exist, then downloads file from FTP to local directory
        if filename in files:
            print "Duplicate date in records" #There already exists a file
        elif os.path.exists(mypath == False): #File does not exist
            fhandle = open(mypath, 'wb')
            print "Getting " + mypath
            ftp.retrbinary('RETR ' + filename, fhandle.write)
            #Retrieve a file in binary transfer mode
            fhandle.close()
        elif os.path.exists(mypath) == True:  #File exists
            filesize = os.stat(filename) #Get stats for filename
            #print filesize.st_size #Test to see file size
            if filesize.st_size == 0:
            # Check if file size is 0, if so replace with updated file on FTP
                print "File size is 0, replacing with updated FTP " + mypath
                fhandle = open(mypath, 'wb')
                ftp.retrbinary('RETR ' + filename, fhandle.write)
                fhandle.close()
            else:
                print "File ", filename, " Exists, Skipping to next Download"
        else:
            print "Unknown Error"


def merge_columns(maindataframe, column1, column2, newname):
    """ Merge multiple columns and rename """

    df1 = pandas.DataFrame(maindataframe[column1])
    df1.rename(columns={column1:newname}, inplace=True)
    #print "Dataframe 1 \n", df1, "\n"

    df2 = pandas.DataFrame(maindataframe[column2])
    df2.rename(columns={column2:newname}, inplace=True)
    #print "Dataframe 2 \n", df2, "\n"

    df3 = df1.combine_first(df2) # Replaces df1's NaNs with df2's values
    #print "Dataframe 3 \n", df3, "\n"

    # Delete old columns on main dataframe
    maindataframe = maindataframe.drop(column1, axis=1) # Remove 1st column
    if column1 != column2:
        maindataframe = maindataframe.drop(column2, axis=1) # Remove 2nd column

    maindataframe = pandas.concat([maindataframe, df3], axis=1)

    return maindataframe

def write_files(filename):
    """Write file from original directory to a clean directory"""
    myinputfilelocation = os.path.join(originaldirectory, filename)
    myoutputfilelocation = os.path.join(cleandirectory, filename)

    myinputfile = codecs.open(filename=myinputfilelocation,
        mode='rb', encoding='ascii', errors='replace')
    myoutputfile = codecs.open(filename=myoutputfilelocation,
        mode='wb', encoding='utf-8', errors='ignore')

    myinputfile.next() #Skip first row
    myinputfile.next() #Skip second row, header on third row

    # Take inputfile, read through all, clean out quotes (since some of the
    # raw data has quotes and misc chars inside), then write to output file
    for line in myinputfile:
        try:
            #newline = unicode(line, decoding='utf-8', errors='ignore')
            #newline = line.encode('utf-8', errors='replace')
            newline = line.encode('ascii', errors='replace')
        except UnicodeDecodeError:
            print "Decode Error"
        #newline = line.encode('utf-8', errors='replace')
            #newline = line.encode('utf-8', errors='ignore')
        #newline = line.decode('utf-8', errors='ignore') # Just added
        myoutputfile.write(newline)
    myinputfile.close()
    myoutputfile.close()

def opencsv_writesql(myinputfile):
    """ Write file to SQL """

    table = iCarol
    with open(os.path.join(cleandirectory, myinputfile)) as f:
        #Assuming first line is header
        cf = csv.DictReader(f, delimiter=',')
        for row in cf:
            if table is None:
                #If table does not exist, create one with Column names from csv
                table = sqlalchemy.Table('iCarol', metadata,
                        sqlalchemy.Column('CallReportNum', sqlalchemy.Integer,
                        primary_key=True),
                        *(sqlalchemy.Column(rowname, sqlalchemy.String())
                        for rowname in row.keys()))
                table.create()
            try:
                table.insert().values(**row).execute() #Insert each row
            except:
                #raise
                #pdb.set_trace()
                print "Error with this row"


def clean_data(mydataframe):
    print "Before cleaning data", mydataframe

    try:
        mydataframe = merge_columns(mydataframe,\
            u'Client???s MH and SA concerns/treatment - Highest level of care (MH)',\
            u'Clients MH and SA concerns/treatment - Highest level of care (MH)',\
            u"Clients MH and SA concerns/treatment - Highest level of care (MH)")

        mydataframe = merge_columns(mydataframe,\
            u'Client???s MH and SA concerns/treatment - Mental Health Concerns - Primary',\
            u'Clients MH and SA concerns/treatment - Mental Health Concerns - Primary',\
            u"Clients MH and SA concerns/treatment - Mental Health Concerns - Primary")

        # Handle: Client???s MH and SA concerns/treatment - Alcohol and/or drug abuse/Gambling
        mydataframe = merge_columns(mydataframe,\
            u'Client???s MH and SA concerns/treatment - Alcohol and/or drug abuse/Gambling',\
            u'Clients MH and SA concerns/treatment - Alcohol and/or drug abuse/Gambling',\
            u"Clients MH and SA concerns/treatment - Alcohol and/or drug abuse/Gambling")

        # Handle: Client???s MH and SA concerns/treatment - Alcohol and/or drug abuse
        mydataframe = merge_columns(mydataframe,\
            u'Client???s MH and SA concerns/treatment - Alcohol and/or drug abuse',\
            u'Clients MH and SA concerns/treatment - Alcohol and/or drug abuse',\
            u"Clients MH and SA concerns/treatment - Alcohol and/or drug abuse")

        # Handle: Clients MH and SA concerns/treatment - Alcohol and/or drug abuse
        mydataframe = merge_columns(mydataframe,\
            u'Clients MH and SA concerns/treatment - Alcohol and/or drug abuse',\
            u'Clients MH and SA concerns/treatment - Alcohol and/or drug abuse/Gambling',\
            u'Clients MH and SA concerns/treatment - Alcohol and/or drug abuse')

        #Registration - If you completed the Self-Check Quiz please provide your Reference Number.<br/>Reference Number:
        #mydataframe = merge_columns(mydataframe,\
        #    u'Registration - If you completed the Self-Check Quiz please provide your Reference Number.<br/>Reference Number:',\
        #    u'Registration - If you completed the Self-Check Quiz please provide your Reference Number.<br/>Reference Number:',\
        #    u"Registration - If you completed the Self-Check Quiz please provi")

        # Handle: Clients MH and SA concerns/treatment - Alcohol and/or drug abuse
        mydataframe = merge_columns(mydataframe,\
            u'Risk Assessment - Actively Suicidal Ideation within the last 2 days',\
            u'Risk Assessment - Active Suicidal Ideation within the last 2 days',\
            u'Risk Assessment - Active Suicidal Ideation within the last 2 days')

    except:
        print "Column missing from merge"

    print "After cleaning data", mydataframe
    return mydataframe



if __name__ == "__main__":

    ###Prepare DB connection for SQLAlchemy
    #Create a specific connection to a MS SQL database engine
    #Set 'echo=True' to see full debugging
    engine=sqlalchemy.create_engine(settings.sqlalchemy_connection, echo=True)
    metadata = sqlalchemy.MetaData(bind=engine)
    try:
        #Assumes that the table exists
        iCarol = sqlalchemy.Table('iCarol', metadata, autoload=True)
    except:
        create_table()
    metadata.create_all(engine) #Create all tables and objects at once
    conn = engine.connect()

    #pdb.set_trace() # Debugging

    write_files(myfilename)
    #Take original data in folder, write to another modified folder

    mynewoutputfile = os.path.join(cleandirectory, myfilename)
    mydataframe = pandas.io.parsers.read_table(mynewoutputfile, sep=',',
            quotechar='"', header=0, index_col=0, error_bad_lines=True,
            warn_bad_lines=True, encoding='utf-8')
    dfclean = pandas.DataFrame(data=mydataframe, columns=mylist)

    dfclean = clean_data(dfclean) #Merge lots of columns together

    #print "Type of dfclean", type(dfclean)

    dfclean = dfclean.drop(u"CallReportNum", axis=1)

    print "Now Cleaned", dfclean

    dfclean.to_csv(mynewoutputfile, index=True,
        index_label='CallReportNum')

    opencsv_writesql(myfilename) #Write data to MS SQL database
