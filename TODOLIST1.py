tasks = []
def AddTask():
    task = input("Please enter a task:")
    tasks.append(task)
    print(f"Task '{task}' added to the list.")

def ListTasks():
    if not tasks:
        print("There are no tasks currently.")
    else:
        print("Current Tasks:")
        for index, task in enumerate(tasks):
            print(f"Task #{index}.{task}")

def DeleteTask():
    ListTasks()
    try:
        taskToDelete = int(input("Enter the # to delete:"))
        if taskToDelete >=0 and taskToDelete < len(tasks):
            tasks.pop(taskToDelete)
            print(f"Task {taskToDelete} has been removed.")
        else:
            print(f"Task #{taskToDelete} was not found")
    except:
        print("Invalid Input")

print("To Do List:")
while True:
    print("\n")
    print("please select one of the following options")
    print("-------------------------------------------")
    print("1.Add a new task")
    print("2.Delete a task which you want")
    print("3.List tasks ")
    print("4.Quit")


    choice = input("Enter your choice")
    if(choice == "1"):
        AddTask()
    elif(choice == "2"):
        DeleteTask()
    elif (choice == "3"):
        ListTasks()
    elif (choice == "4"):
        break
    else:
        print("Invalid input. Please try again.")

print("Goodbye! ")