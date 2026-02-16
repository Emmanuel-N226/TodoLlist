#ToDo lists

#list that will have tasks added 

title = "Welcome"
print(title.center(20, "="))

#list to hold tasks
tasks = []
#list to hold completed tasks
done = []
#Exit condition
exit = True

#ToDo list 
#1.add a task
#2.view tasks
#3.remove a task
#4.View outsanding
#5.view completed
#6.exit

#Functions for each section
def add_task():
    task = input("Enter a task: ")
    #check if its an integer beimg entered
    if task.isdigit():
        print("Please enter words!!")
        add_task()
    tasks.append(task)
    pass

def view_task():
    if len(tasks) == 0:
        print("No task here!!")
    else:
        print(f"Here are your tasks\n{tasks}")
    pass

def remove_tasks():
    if len(tasks) == 0:
        print("No tasks to remove")
    else:
        task_remove =input(f"Enter a task your done with from the list\n{tasks}: ")
        #remove uses value
        #delete uses index 
        #added task come here 
        done.append(task_remove)
        tasks.remove(task_remove)
        print(f"Your task {task_remove} has been completed and added to your done catalogue!!")
    pass

def view_outstanding():
    view_task()
    pass

def view_completed():
    print(f"here are you completed tasks:\n{done}")
    pass

def exitout():
    global exit
    print("Closing ToDo list goodbye !!")
    exit = False
    pass

#Daddy code holding all functions
while exit:
    choice = int(input("Hey welcome to your ToDo list what would you like to do?\n1.Add Task\n2.View Tasks\n3.Remove tasks\n4.View outsanding tasks\n5.View completed tasks\n6.Exit\nInput here: "))
    if choice == 1:
        add_task()
    elif choice == 2:
        view_task()
    elif choice == 3:
        remove_tasks()
    elif choice == 4:
        view_outstanding()
    elif choice == 5:
        view_completed()
    elif choice == 6:
        exitout()
    else:
        print("Please enter a valid option!!")


    

