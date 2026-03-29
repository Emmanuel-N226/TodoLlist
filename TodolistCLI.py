import sqlite3

#connecting database function
def connect_db():
    return sqlite3.connect("todoapp.db")

#Functions

#Create a table
def create_table():
    conn = connect_db()
    c = conn.cursor()

    c.execute("""CREATE TABLE IF NOT EXISTS tasks(
            id INT PRIMARY KEY,    
            task TEXT NOT NULL,
            priority TEXT NOT NULL,
            due INT NOT NULL 
            )""")
    print(">> code ran successfully")
    conn.commit()
    conn.close()
#table created on import


#Add items
def add_task(id, task,priority,due):
    conn = connect_db()
    c = conn.cursor()

    c.execute("INSERT INTO tasks VALUES(?,?,?,?)",(id,task,priority,due))
    print(">> entry entered successfully")

    conn.commit()
    conn.close()

#View tasks
def view_tasks():
    conn = connect_db()
    c = conn.cursor()

    c.execute("SELECT rowid, * FROM tasks")
    tasks = c.fetchall()

    for task in tasks:
        print(task)
    conn.close()

#view by id
def get_task_by_id(id):
    conn = connect_db()
    c = conn.cursor()
    c = conn.execute(
        "SELECT * FROM tasks WHERE id = ?", (id,)
    )
    task = c.fetchone
    conn.close()

#Update task
def edit_task(id, new_task,new_priority,new_due_date):
    conn = connect_db()
    c = conn.cursor()
    c.execute("UPDATE tasks SET task = ?, priority = ? , due = ? WHERE rowid = ?",(id, new_task, new_due_date, new_priority))
    print(">> task updated")
    conn.commit()
    conn.close()

# #Update due date
# def edit_due_date(id, due):
#     conn = connect_db()
#     c = conn.cursor()

#     c.execute("UPDATE tasks SET due = ? WHERE rowid = ?",(id,due))
#     print(">> task edited")
#     conn.commit()
#     conn.close()

# #Update priority
# def edit_priority(id,priority):
#     conn = connect_db()
#     c = conn.cursor()

#     c.execute("UPDATE tasks SET priority = ? WHERE rowid = ?",(id,priority))
#     print(">> priority edited")
#     conn.commit()
#     conn.close

def delete_task(id):
    conn = connect_db()
    c = conn.cursor()

    c.execute("DELETE FROM tasks WHERE rowid =?",(id,))
    print(">> task deleted")
    conn.commit()
    conn.close()    