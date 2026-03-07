#ToDo lists

#list that will have tasks added 

title = "Welcome"
print(title.center(60, "="))

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
    #check if its an integer being entered
    if task.isdigit():
        print("Please enter words!!")
        return
    #new improvement
    elif task == "":
        print("Space cannot be empty!!")
        return
    print("Task succesfully! added")
    tasks.append(task)
    

def view_task():
    global tasks
    if len(tasks) == 0:
        print("No task here!")
    else:
        #new feature enumerate 
        print("Here are your tasks!")
        for i , task in enumerate(tasks, start=1):
            print(f"{i}. {tasks}")
            print(f"You have {len(tasks)} tasks remaining.")

    

def remove_tasks():
    global tasks
    if len(tasks) == 0:
        print("No tasks to remove.")
    else:
        for i , task in enumerate(tasks, start=1):
            print(f"{i}. {tasks}")

        task_remove =int(input(f"Enter number of the task your done with from the list: ")) 
        done.append(task_remove)
        #new improvement
        tasks.pop(task_remove-1)
        print(f"Your task {task_remove} has been completed and added to your done catalogue!")
        print(f"You have {len(tasks)} tasks remaining.")
    

def view_outstanding():
    view_task()
    

def view_completed():
    print(f"here are you completed tasks:\n{done}")
    print(f"You have {len(tasks)} tasks remaining.")
    

def exitout():
    global exit
    print("Closing ToDo list goodbye!")
    goodbye = ""
    print(goodbye.center(60, "="))
    exit = False
    

#Code holding all functions
while exit:
    try:
        heading =""
        print(heading.center(60, "="))
        choice = int(input("Welcome to your ToDo list, what would you like to do?\n1.Add Task\n2.View Tasks\n3.Remove tasks\n4.View outsanding tasks\n5.View completed tasks\n6.Exit\nInput here: "))
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
    #new improvement
    except ValueError:
        print("Please enter a valid option!!")



    

1