#ToDo lists

#list that will have tasks added 

title = "Welcome"
print(title.center(60, "="))

#list to hold tasks
tasks = {}
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
#priorities function

        
def add_task():
    adding_task = True
    while adding_task:
        print()
        task = input("Enter a task: ")
        #adding due date
        due_date = input("Enter task due date: ")
        #adding priority
        priority = input("Enter priority\nHigh, Meduim , Low: ").capitalize()
        
        tasks[task] = {"due" : due_date,
                    "priority" : priority}  #combining the key and value pairs
        

        #Check if its an integer being entered
        if task.isdigit() or priority.isdigit():
            print("Please enter words!!")
            return
        #New improvement
        elif task == "" or due_date == "" or priority == "":
            print("Space cannot be empty!!")
            return
        elif priority != "High" and priority != "Meduim" and priority != "Low":
            print("Enter a valid priorities option!")
            return
        
        finished = input("Are you done entering tasks? Y/N: ").capitalize()
        if finished == "Y":
            adding_task = False
            break
        elif finished == "N":
            print("Task succesfully added!")
            continue
        elif finished == "":
            print("Space can not be empty!")
            return
        else:
            print("Enter a valid option!")
            return
    
    print("Task succesfully added!")
    
    

def view_task():
    global tasks
    if len(tasks) == 0:
        print()
        print("No task here!")
    else:
        #new feature enumerate 
        print()
        print("Here are your tasks!")
        for task, info in tasks.items():
            #cleaner format on task viewing
            print()
            print(f"Task: {task}")
            print(f"Due: {info['due']}")
            print(f"Priority: {info['priority']}")
            print()
        
        print(f"You have {len(tasks)} tasks remaining.")

    

def remove_tasks():
    global tasks
    if len(tasks) == 0:
        print()
        print("No tasks to remove.")
    else:
        removing_tasks = True
        while removing_tasks:
            print("Here are tasks you can remove:")
            for i , (task , info) in enumerate(tasks.items(), start=1):
                print()
                print(f"{i}.Task: {task}")
                print(f"Due: {info['due']}")
                print(f"Priority: {info['priority']}")
                print()

            task_remove =int(input(f"Enter number of the task your done with from the list: ")) 
            removed = list(tasks.keys())[task_remove-1]
            done.append(removed)
            #new improvement
            del tasks[removed]
            reremove= input("Do you want to remove more tasks? Y/N: ").capitalize()
            if reremove == "Y":
                print(f"Your task {removed} has been completed and added to your done catalogue!")
                continue
            elif reremove == "N":
                break
            else:
                print("enter a vald option")
                continue
        print(f"Your task {removed} has been completed and added to your done catalogue!")
        print(f"You have {len(tasks)} tasks remaining.")
    

def view_outstanding():
    view_task()
    

def view_completed():
    print()
    print(f"here are you completed tasks:\n{done}")
    print(f"You have {len(tasks)} tasks remaining.")
    

def exitout():
    global exit
    print()
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

 