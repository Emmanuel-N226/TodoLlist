import Todo_cli
from datetime import datetime

#CLI for the todolist
#get user task
def get_task():
    getting_task = input("Enter a task:\n")
    if getting_task.isdigit():
        print("Enter words!")
    elif getting_task == "":
        print("Task cant be empty!")
    return


#get priority
def priority():
    get_priority = int(input("Enter the task priority 1.HIGH 2.MEDIUM 3.LOW\n"))
    try:
        if get_priority == 1:
            return "HIGH"
        elif get_priority == 2:
            return "MEDUIM"
        elif get_priority == 3:
            return "LOW"
        else:
            print("Enter valid options!")
    except ValueError:
        print("Enter a valid number!")
        

#get due date
def due_datum():
    while True:
        user_input = input("Enter due date (YYYY/MM/DD): ").strip()
        try:
            due_date = datetime.strptime(user_input, "%Y/%m/%d")
            return due_date.strftime("%Y/%m/%d")  # returns a string
        except ValueError:
            print("❌ Invalid date format. Please use YYYY/MM/DD")



#Add task
def add_task():
    try:
        #get task
        user_task = get_task()
        task_priority= priority()
        due_date = due_datum()
        Todo_cli.add_task(user_task,task_priority,due_date)
    except Exception as e:
        print(f"❌ Error: {e}")


#View tasks
def view_tasks():
    print("Here are your tasks:\n")
    Todo_cli.view_tasks()

#Delete tasks
def remove_task():
    print("Here are your tasks:\n")
    Todo_cli.view_tasks()
    row_id = int(input("Enter a row id you will like to remove:\n"))
    Todo_cli.delete_task(row_id)


#Edit Task
def edit_task():
    try:
        row_id = int(input("Enter the ID you want to update:\n"))
        new_task = input("Enter a new first name:\n")
        Todo_cli.edit_task(row_id, new_task)
    except Exception as e:
        print(f"❌ Error: {e}")

#update last name
def edit_priority() :
    try:
        row_id = int(input("Enter the ID you want to update:\n"))
        new_priority = input("Enter a new first name:\n")
        Todo_cli.edit_priority(row_id, new_priority)
    except Exception as e:
        print(f"❌ Error: {e}")

#update email
def edit_due_date() :
    try:
        row_id = int(input("Enter the ID you want to update:\n"))
        due_date = input("Enter a new email:\n")
        Todo_cli.edit_due_date(row_id, due_date)
    except Exception as e:
        print(f"❌ Error: {e}")


title = "Welcome"
print(title.center(60, "="))

quit_out = True

#exitout function
def exitout():
    global quit_out
    quit_out = False
    print()
    print("Closing Databse backend goodbye!")
    goodbye = ""
    print(goodbye.center(60, "="))
    exit = False

while quit_out:

        heading =""
        print(heading.center(60, "="))
        choice = int(input("Welcome to your ToDoList backend, what would you like to do?\n1.Add the task" \
        "\n2.View tasks\n3.Remove tasks\n4.Edit task\n5.Edit priority\n6.Edit due date\n7.Exit\nInput here: "))
        #ADDING THE LOGIC CONTROLERS
        if choice == 1:
            add_task()
        elif choice == 2:
            view_tasks()
        elif choice == 3:
            remove_task()
        elif choice == 4:
            edit_task()
        elif choice == 5:
            edit_priority()
        elif choice == 6:
            edit_due_date
        elif choice == 7:
            exitout()
        else:
            print("Please enter a valid option!!")