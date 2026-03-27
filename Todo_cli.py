import sqlite3

conn =sqlite3.connect('todoapp.db')
c = conn.cursor()

#Functions

#Create a table
def create_table():
    conn =sqlite3.connect('todoapp.db')
    c = conn.cursor()

    c.execute("""CREATE TABLE IF NOT EXISTS tasks(  
            task TEXT,
            priority TEXT,
            due INT 
            )""")
    print(">> code ran successfully")
    conn.commit()
    conn.close()
#table created on import
create_table()

#Add items
def add_task(task,priority,due):
    conn =sqlite3.connect('todoapp.db')
    c = conn.cursor()

    c.execute("INSERT INTO tasks VALUES(?,?,?)",(task,priority,due))
    print(">> entry entered successfully")

    conn.commit()
    conn.close()

#View tasks
def view_tasks():
    conn =sqlite3.connect('todoapp.db')
    c = conn.cursor()

    c.execute("SELECT rowid, * FROM tasks")
    tasks = c.fetchall()

    for task in tasks:
        print(task)
    conn.close()

#Update task
def edit_task(id, new_task):
    conn =sqlite3.connect('todoapp.db')
    c = conn.cursor()

    c.execute("UPDATE tasks SET task = ? WHERE rowid = ?",(id, new_task))
    print(">> task updated")
    conn.commit()
    conn.close()

#Update due date
def edit_due_date(id, due):
    conn =sqlite3.connect('todoapp.db')
    c = conn.cursor()

    c.execute("UPDATE tasks SET due = ? WHERE rowid = ?",(id,due))
    print(">> task edited")
    conn.commit()
    conn.close()

#Update priority
def edit_priority(id,priority):
    conn =sqlite3.connect('todoapp.db')
    c = conn.cursor()

    c.execute("UPDATE tasks SET priority = ? WHERE rowid = ?",(id,priority))
    print(">> priority edited")
    conn.commit()
    conn.close

def delete_task(id):
    conn =sqlite3.connect('todoapp.db')
    c = conn.cursor()

    c.execute("DELETE FROM tasks WHERE rowid =?",(id,))
    print(">> task deleted")
    conn.commit()
    conn.close()    