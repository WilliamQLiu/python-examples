""" Test file for SQL Alchemy Introduction: http://docs.sqlalchemy.org/en/latest/core/tutorial.html"""
from sqlalchemy import *

"""Creating an in-memory-only SQLite database; easy way to test things without needing an actual database defined anywhere.
  echo flag is a shortcut to setting up SQLAlchemy logging, similar to Python's standard 'logging' module"""
engine = create_engine('sqlite:///:memory:', echo=True)
metadata = MetaData() #A Database MetaData is a collection of Table objects and their associated child 'Column' objects
users = Table('users', metadata,
    Column('id', Integer, primary_key=True),
    Column('name', String(50)),
    Column('fullname', String(50)),
)
addresses = Table('addresses', metadata,
    Column('id', Integer, primary_key=True),
    Column('user_id', None, ForeignKey('users.id')),
    Column('email_address', String(50), nullable=False)
)
metadata.create_all(engine) #Create our selection of tables for real inside the SQLite database (passing in the engine, which points to our database)
conn = engine.connect() #Connect to engine



def insert_expressions():
    """Insert Expressions"""
    ins = users.insert()
    str(ins)
    'INSERT INTO users(id, name, fullname) VALUES (:id, :name, :fullname)'

    ins=users.insert().values(name='jack', fullname='Jack Jones')
    str(ins)
    'INSERT INTO users (name, fullname) VALUES (:name, :fullname)'
    ins.compile().params
    {'fullname': 'Jack Jones', 'name': 'jack'} #Seen as 'INSERT INTO users (name, fullname) VALUES (?, ?)'

    result = conn.execute(ins) #Run the last ins statement
    result.inserted_primary_key #Returns [1] since we didn't specify the id column 

    """Executing Multiple Statements"""
    #Use executemany() method to send in a list of dictionaries each containing a distinct set of parameters to be inserted
    ins = users.insert()
    conn.execute(ins, id=2, name='wendy', fullname='Wendy Williams')
    conn.execute(addresses.insert(), [
        {'user_id':1, 'email_address':'jack@yahoo.com'},
        {'user_id':1, 'email_address':'jack@msn.com'},
        {'user_id':2, 'email_address':'www@www.org'},
        {'user_id':2, 'email_address':'wendy@aol.com'},
        ])

def selecting_data():
    """Selecting Data"""
    s = select([users])
    result = conn.execute(s) # Returns a ResultProxy object, which acts like a DBAPI cursor, including methods fetchone() and fetchall()

    """iterate through all the rows in a simple tuple-like result"""
    for row in result:
        print row #Sample Data: (1, u'jack', u'Jack Jones')

    """access through dictionary, using the string names of columns"""
    result = conn.execute(s)
    row = result.fetchone()
    print "Name:", row['name'], "; Fullname:", row['fullname'] #Name: jack ; Fullname: Jack Jones

    """access through the use of Column objects directly as keys"""
    for row in conn.execute(s):
        print "Name:", row[users.c.name], "; Fullname:", row[users.c.fullname] #Name: jack ; Fullname: Jack Jones, Name: wendy ; Fullname: Wendy Williams

    result.close()

def operators():
    """All data worked on is the same type of object, the base class of all of these expressions is 'ColumnElement'"""

    """How to equate two columns to each other"""
    print users.c.id == addresses.c.user_id #Returns: users.id=addresses.user_id

    """Using a literal value (not a SQLAlchemy clause object), we get a bind parameter"""
    print users.c.id==7 #Returns: users.id = id_1

    """The 7 literal is embedded in the resulting ColumnElement; we can use the same trick we did with Insert object to see it"""
    print (users.c.id==7).compile().params #Returns: {u'id_1':7}

    """Most Python operators produce a SQL expression here, like, equals, not equals, etc"""
    print users.c.id !=7 #Returns: users.id != :id_1
    print users.c.name == None #None converts to IS NULL, Returns: users.name IS NULL
    print 'fred' > users.c.name #Returns: users.name < :name_1

    """Adding two integer columns together, we get an additional expression"""
    print users.c.id + addresses.c.id #Returns: users.id + addresses.id

    """Addind two string columns together, we get something different"""
    print users.c.name + users.c.fullname #Returns: users.name || users.fullname

    """If you come across an operator which really isn't available, you can use the ColumnOperators.op() method to generate whatever operator you need"""
    print users.c.name.op('tiddlywinks')('foo') #Returns: users.name tiddlywinks :name_1

if __name__ == "__main__":
    """Running Functions"""
    insert_expressions()  #INSERT Examples
    selecting_data()   #SELECT Examples
    operators()   #OPERATION Examples
