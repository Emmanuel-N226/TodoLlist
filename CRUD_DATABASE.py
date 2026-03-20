import sqlite3

#connect to sqlite3
conn = sqlite3.connect('customers.db')

#create a cursor to edit database
c = conn.cursor()

#create a table
c.execute("""CREATE TABLE customers (
          firstname TEXT,
          lastname TEXT,
          email TEXT
          )""")
print(">> code ran successfully")