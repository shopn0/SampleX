print("Let's Do Something!")
todo = []

def task_add():
    x = input("Enter your task: ")
    todo.append(x)
    print("Taks added!")
    return

def rem_task():
    if not todo:
        print("No task found in the list.")
        return
    index = int(input("Enter the serial number of task you want to remove: "))
    if index<0 or index >= len(todo):
        print("Invalid task.")
    else:
        del todo[index]
        print("Task removed.")

    