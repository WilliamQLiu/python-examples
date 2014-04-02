import sql
import pandas as pd

q = 'select * from nytimes limit 10'
df = sql.read_db(q, database_url)
print df.head()

#with sql.get_db(database_url) as conn, closing(conn.cursor()) as curs:
#	print "hi"

#df.head().to_db('nytimes_copy', database_url)
