tasks = []

def add_task(task):
    tasks.append(task)

def delete_task(task):
    if task in tasks:
        tasks.remove(task)
    else:
        print("Task not found!")

def view_tasks():
    print("Tasks:")
    for task in tasks:
        print(task)

# Usage example:
add_task("Buy groceries")
add_task("Finish homework")
view_tasks()
delete_task("Buy groceries")
view_tasks()

