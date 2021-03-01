import sqlite3

db = sqlite3.connect('sql/test.db')
c = db.cursor()

sql_command = """
CREATE TABLE employee ( 
staff_number INTEGER PRIMARY KEY, 
fname VARCHAR(20), 
lname VARCHAR(30), 
gender CHAR(1), 
joining DATE,
birth_date DATE);"""

c.execute(sql_command)
db.commit()

c.executemany('insert into portfolio values (?,?,?)', stocks)
db.commit()

for row in db.execute('select * from portfolio'):
  print(row)