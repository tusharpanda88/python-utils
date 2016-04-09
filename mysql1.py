#insert data

import MySQLdb as mdb

con = mdb.connect('localhost', 'testuser', 'test623', 'testdb');

with con:
    
    cur = con.cursor()
    cur.execute("DROP TABLE IF EXISTS Writers")
    cur.execute("CREATE TABLE Writers(Id INT PRIMARY KEY AUTO_INCREMENT, \
                 Name VARCHAR(25))")
    cur.execute("INSERT INTO Writers(Name) VALUES('abc')")
    cur.execute("INSERT INTO Writers(Name) VALUES('def')")
    cur.execute("INSERT INTO Writers(Name) VALUES('feh')")
    cur.execute("INSERT INTO Writers(Name) VALUES('fet')")
    cur.execute("INSERT INTO Writers(Name) VALUES('geh')")
