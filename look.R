# Open up library for ODBC connections
library(RODBC)

# Connect to ODBC using: odbcConnect(DSN, uid="", pwd="")
dbhandle <- odbcDriverConnect("driver={SQL Server};server=WILL-PC\\SQLEXPRESS;database=BookDatabase;Trusted_Connection='yes'")

# Select all data from table DDHTexts (assuming [BookDatabase].[dbo].[BX-Book-Ratings-Output])
mydata <- sqlQuery(dbhandle, 'SELECT * FROM [BX-Book-Ratings-Output]')

# See the first 6 rows of data using head()
head(mydata)

