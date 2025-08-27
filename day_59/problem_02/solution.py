tasks = []

while True:
    print("1. Add task")
    print("2. Mark completed")
    print("3. View all tasks")
    print("4. View pending tasks")
    print("5. Exit")
    
    choice = input("Choose option: ")
    
    if choice == "1":
        task = input("Enter task: ")
        tasks.append({"task": task, "completed": False})
        print("Task added!")
    
    elif choice == "2":
        task_name = input("Enter task to mark complete: ")
        for task in tasks:
            if task["task"] == task_name:
                task["completed"] = True
                print("Task marked complete!")
                break
    
    elif choice == "3":
        print("All tasks:")
        for task in tasks:
            status = "Done" if task["completed"] else "Pending"
            print("-", task["task"], "(" + status + ")")
    
    elif choice == "4":
        print("Pending tasks:")
        for task in tasks:
            if not task["completed"]:
                print("-", task["task"])
    
    elif choice == "5":
        break