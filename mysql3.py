# retrieve data (one-by-one)

import MySQLdb as mdb

con = mdb.connect('localhost', 'testuser', 'test623', 'testdb');

with con:

    cur = con.cursor()
    cur.execute("SELECT * FROM Writers")

    for i in range(cur.rowcount):
        
        row = cur.fetchone()
        print row[0], row[1]
#close database
	con.close()
