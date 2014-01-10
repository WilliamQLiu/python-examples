### settings.py
### All the FTP, MS SQL Database, and SQLAlchemy connection settings

### ODBC Database Settings for iCarol Export (LifeNet) ###
DB_DRIVER = '{SQL Server}'
DB_SERVER = '<input server name>'
DB_DATABASE = '<input database name>'
DB_UID = '<input user id>'
DB_PWD ='<input password>'

pyodbc_connection = ('DRIVER=' + DB_DRIVER + ';'
        + 'SERVER=' + DB_SERVER + ';'
        + 'DATABASE=' + DB_DATABASE + ';'
        + 'UID=' + DB_UID +  ';' +'PWD=' + DB_PWD)
#print pyodbc_connection


### FTP Settings for iCarol SFTP ###
HOSTNAME = '<input IP Address of hostname>'
USERNAME = '<input username>' # By Default, User:anonymous
PASSWORD = '<input password>' # By Default, Password: anonymous@
ftpdirectory ='/'
filematch = '*.csv'


### SQLAlchemy Engine Settings ###
DB_DRIVER_SQLAlchemy = 'mssql'

sqlalchemy_connection = (DB_DRIVER_SQLAlchemy + '://'
	    + DB_UID + ":" + DB_PWD + "@" + DB_SERVER + "/" + DB_DATABASE 
        )
#print sqlalchemy_connection