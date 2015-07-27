import urllib
import pyodbc
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import pandas as pd

# SQLAlchemy SETUP
params = urllib.quote_plus('DRIVER={SQL Server};SERVER=myserver;DATABASE=mydb;UID=sa;PWD=mypassword')
engine = create_engine("mssql+pyodbc:///?odbc_connect=%s" % params)
Base = declarative_base()
Session = sessionmaker(bind=engine)

class LookupTable(Base):
    """
        LookupTable is the Python object that represents the Lookup Table used in the database.
    """
    __tablename__ = 'iCarolLookup'

    cscid = Column(String(50), primary_key=True)
    value = Column(String(512))


if __name__ == '__main__':

    # SETUP
    Base.metadata.create_all(engine)
    print type(Base)
    #session = Session()

    # Let's see what is in the current Table, we want a 'snapshot' of this Table
    #current_table = session.query(LookupTable).all()
    #for row in current_table:
    #    print row.cscid, row.value  # Peak at the dataset

    # We want to convert this query into a Pandas DataFrame for checking later
    #query = session.query(LookupTable)
    #data_records = [rec.__dict__ for rec in query.all()]
    #current_df = pd.DataFrame.from_records(data_records)
    #print raw_df.columns  # Index([u'_sa_instance_state', u'cscid', u'value'], dtype='object')
    #print current_df

    pdsql = pd.io.sql.SQLDatabase(engine)
    current_df = pd.read_sql("SELECT * FROM iCarolLookup", con=engine)
    print current_df


    # Get csv file from iCarol to import into our Database Table
    #new_df = pd.DataFrame.from_csv('')

    test_dict = {
                '2': 'Testing2',
                '3': 'Testing3'
    }

    test_df = pd.DataFrame({'cscid': ['2', '3', '4'],
                           'value': ['Hello', 'World', 'Liu']})

    print test_df

    # Compare the two dataframes, see what fields have changed

    # Write new df to SQL
    test_df.to_sql(name="iCarolLookup", if_exists='append', index=False, con=engine)

    # How to write data to the Database Table
    #test_kvpair = LookupTable(cscid='1', value='Testing')
    #session.add(test_kvpair)

    #try:
    #    session.commit()
    #    print "Session Committed"
    #except:
    #    print "Error with committing session"
    #    raise



