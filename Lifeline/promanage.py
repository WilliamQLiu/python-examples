# Program to calculate projected completion date for projects (with source being an Excel file)
import os # For filepaths
import pandas # For dataframes
import datetime # Needed for date calculations
from pandas.tseries.offsets import * # For Bday (Business Days) utility

#Specify directories
originaldirectory = str('C:\Users\wliu\Desktop\Spiceworks\Original')
os.chdir(originaldirectory) #Change Local directory (where files go to)
FILENAME = 'Export2014-1-9.csv'

"""
# Use only if data is messy, not needed unless you need to clean unknown chars
cleandirectory = str('C:\Users\wliu\Desktop\Spiceworks\Modified') 
def write_files(myfilename):
    ''' This function is not needed/used unless data is corrupt with unknown 
    inputs, then call this to replace unknown characters'''
    myinputfilelocation = os.path.join(originaldirectory, myfilename)
    #print myinputfilelocation #C:\Users\wliu\Desktop\Spiceworks\Original\Export2013-11-18.csv
    
    myoutputfilelocation = os.path.join(cleandirectory, myfilename)
    #print myinputfilelocation #C:\Users\wliu\Desktop\Spiceworks\Modified\Export2013-11-18.csv
    
    myinputfile = open(myinputfilelocation, 'rb')
    myoutputfile = open(myoutputfilelocation, 'wb')

    # Take inputfile, read through all lines, clean out quotes
    # (since some of the raw data has quotes inside), then write to output file
    for line in myinputfile:
        try:
            newline = unicode(line, errors='replace')
        except UnicodeDecodeError:
            print("Decode Error")
        newline = newline.encode('utf-8', errors='replace')
        myoutputfile.write(newline)
    myinputfile.close()
    myoutputfile.close()
"""

def modify_files(mydataframe):
    # Exclude specific columns from the data source
    mydataframe = mydataframe[mydataframe['Status']=='open']
    mydataframe = mydataframe[mydataframe['Category']!='Facilities']
    mydataframe = mydataframe[mydataframe['Division']!='Help Desk']
    mydataframe.fillna(0, inplace=True) # Fill NaN's with 0's
    mydataframe = mydataframe.sort(columns='IT Ranking', ascending=False) # Sort Desc
    #print mydataframe.values # print actual values instead of summary
    return mydataframe

def estimate_today():
    # <Take next highest ranked item and add 'Hours Remaining' to a new column 'Estimated Date'>
    #today = (time.strftime("%m/%d/%Y"))
    now = datetime.datetime.now()
    return now

def write_dataframe_to_csv(mydataframe, name):
    newname = name + '.csv' # Modify name to new csv name
    mydataframe.to_csv(newname) # Write dataframe to csv

def calc_hours(mydataframe):
    # Takes 'Hours Remaining' column, then creates an aggregate of hours into a new column

    #myhoursremaining = mydataframe['Hours Remaining'].sum() # Get total hours remaining
    #myitem = mydataframe.ix[[1563],'Hours Remaining'] # Prints Index (1563) and Hours Remaining (4)
    #mylist.append(myitem) # Take 'Hours Remaining' and add to list
    #print mylist #

    # Create two lists to hold current 'Hours Remaining' and Sum of 'Hours Remaining' (as it goes along column)
    mycurrenthours=[]
    myagghours=[]
    mytotalhours = 0

    for a in mydataframe['Hours Remaining']: # Go through all 'Hours Remaining' list one at a time
        mycurrenthours.append(a) # mycurrenthours gets the current 'Hours Remaining' (e.g. 4, 2, 28, 2, 8, etc.)
        mytotalhours = sum(mycurrenthours) # add the current hours to an temporary total hours (i.e. doing a rolling sum)
        myagghours.append(mytotalhours) # add the rolling sum to a new list
    return myagghours

def estimate_days_projects(mylist):
    
    mylist = map(int, mylist) # Convert all list items into int (from a numpy float)
    myprojecteddates = [] # Will hold all projected dates
    workinghoursperday = 3 # Number of hours per working day

    now = datetime.datetime.now() # Get today's datetime
    #print now

    for a in mylist:
        #print a # this holds the aggregate hours remaining (e.g. 4, 6, 36, etc.)
        #print (a/workinghoursperday) # this holds the number of days remaining ()
        finishdate = (a/workinghoursperday) 
        finishdate = now + BDay(finishdate) # Returns the next business date that this item will be done
        finishdate = finishdate.strftime('%m/%d/%Y') # Format to mm/dd/yyyy
        myprojecteddates.append(finishdate) # Appends the next business date into list
    return myprojecteddates # returns a list of projected dates (e.g. '11/19/2013', '11/19/2013', '11/25/2013', '11/26/2013')

def concate_list(mydayslist, mydataframe):
    
    mydataframe['Projected Completion Date'] = mydayslist #Add mydayslist to a new column called 'Projected Date'
    return mydataframe

def create_projected_dates(mydataframe):
    
    myhourslist = calc_hours(mydataframe) # Returns a list of aggregate hours sorted by IT Ranking (e.g. 4, 6, 34, 44, 46, 51, 76, 146)
    mydayslist = estimate_days_projects(myhourslist) # Returns a list of projected dates per project (e.g. '11/19'2013', '11/25/2013')
    mydataframe = concate_list(mydayslist, mydataframe) # Returns dataframe with new column 'Projected Date' concatenated
    return mydataframe

if __name__ == "__main__":

    # Specify file locations
    mynewoutputfile = os.path.join(originaldirectory, FILENAME)
    dataframe = pandas.io.parsers.read_table(mynewoutputfile, sep=',',
        quotechar='"', header=0, index_col=0, error_bad_lines=True,
        warn_bad_lines=True, encoding='utf-8')
    #print mydataframe
    
    cleandataframe = modify_files(dataframe) # Clean file (e.g. No HelpDesk tickets, No Facilities tickets, Open Tickets Only)

    # Slice up data by 'Division'
    programdf = cleandataframe[cleandataframe['Division']=='Web Development/Programming']
    reportdf = cleandataframe[cleandataframe['Division']=='Reporting/Routing']
    sysadmindf = cleandataframe[cleandataframe['Division']=='System Admin']

    # Run a few functions to create projected dates
    programdf = create_projected_dates(programdf)
    reportdf = create_projected_dates(reportdf)
    sysadmindf = create_projected_dates(sysadmindf)

    # Write dataframes to csv files
    write_dataframe_to_csv(programdf, 'Programming')
    write_dataframe_to_csv(reportdf, 'Reporting')
    write_dataframe_to_csv(sysadmindf, 'System Admin')