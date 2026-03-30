#importing 
from flask import Flask, render_template, request, redirect, url_for
import TodolistCLI

#how we call app in flask
app = Flask(__name__)

#running database once per startup
TodolistCLI.create_table()
#adding routes

#route to home page (index)
@app.route("/")
def index():
    tasks = TodolistCLI.view_tasks()
    return render_template('index.html',tasks=tasks)

#route to add items
@app.route('/add_task',methods=['POST'])
def add_entry():
    task = request.form['task_text']
    priority = request.form['priority_text']
    due = request.form['due_date_text']
    TodolistCLI.add_task(task, priority, due )
    return redirect(url_for('index'))

#route to edit task
@app.route('/edit_task/<int:id>', methods = ['POST', 'GET'])
def edit_task(id,):
    if request.method == 'POST':
        task = request.form['new_task']
        priority = request.form['new_priority']
        due = request.form['new_due_date']
        TodolistCLI.edit_task(id,task, priority, due)
        return redirect(url_for('index'))

    #Show task to edit    
    task = TodolistCLI.get_task_by_id(id)
    #send to update page so they can update 
    return render_template('update_task.html', task=task)

@app.route('/delete_task/<int:id>',methods=['GET'])
def delete_task(id):
    TodolistCLI.delete_task(id)
    return redirect(url_for('index'))

#start
if __name__ == '__main__':
    app.run(debug=True)