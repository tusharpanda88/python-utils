
import os
import sqlite3

db_filename = 'todo.db'
db_is_new = not os.path.exists(db_filename)

if db_is_new:
	print "Creating database"
	conn = sqlite3.connect(db_filename)
	cur = conn.cursor()
	cur.execute('SELECT SQLITE_VERSION()')
	data1 = cur.fetchone() #fetchall will retrieve all available
	cur.execute("CREATE TABLE Cars(Id INT, Name TEXT, Price INT)")
	cur.execute("INSERT INTO Cars VALUES(1,'Audi',52642)")
	cur.execute("INSERT INTO Cars VALUES(2,'Mercedes',57127)")
	cur.execute("INSERT INTO Cars VALUES(3,'Mercedes',34888)")
	cur.execute("INSERT INTO Cars VALUES(4,'omni',10000)")
	cur.execute("INSERT INTO Cars VALUES(5,'hyundai',9000)")
	conn.close()
	print "SQLite version: %s" %data1  
	print "DONE"
else:
	print "database exists"
	conn = sqlite3.connect(db_filename)
	cur = conn.cursor()
	cur.execute("SELECT * FROM Cars")
	row = cur.fetchone()
	print row
	conn.close()

