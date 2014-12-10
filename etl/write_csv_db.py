""" Open CSV file locally, then write to Database """
import csv # For CSV
import os # For filepaths
import pyodbc # for database connections


def write_file(myfilename):
    connection = pyodbc.connect('DRIVER={SQL Server};SERVER=myserver;DATABASE=mydatabase;UID=myusername;PWD=mypassword')
    cursor = connection.cursor()

    with open (myfilename, 'r') as csvfile:
        reader = csv.reader(csvfile)  # Read CSV file
        next(reader, None)  # skip the headers
        next(reader, None)  # skip the headers
        columns = next(reader)
        query = 'insert into dbo.iCarolChatsRouted({0}) values ({1})'
        query = query.format(','.join(columns), ','.join('?' * len(columns)))

        try:
            for data in reader:
                cursor.execute(query, data)
        except:
            raise

            print "Error with this line"
            print query
            print data
        cursor.commit()

if __name__ == "__main__":

    mydirectory = str(r"C:\Users\wliu\Desktop")
    os.chdir(mydirectory)  # Change to directory
    myfilename = 'chatsrouted.csv' # Filename

    write_file(myfilename)
