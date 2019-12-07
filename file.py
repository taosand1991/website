import sqlite3
import os.path


db = 'data.db'
con = sqlite3.connect(db)
c = con.cursor()
c.execute('''CREATE A TABLE my table(a TEXT, b TEXT, c TEXT)''')
c.execute('''INSERT INTO  my_table VALUES (?,?,?)''', ("test1", "text2","test3"))
con.close()
os.remove(db)