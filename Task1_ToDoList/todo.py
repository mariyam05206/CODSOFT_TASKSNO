tasks = []
status = []

while True:
    print("\n1. Add Task")
    print("2. View Tasks")
    print("3. Update Task")
    print("4. Delete Task")
    print("5. Complete Task")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        task = input("Enter task: ")
        tasks.append(task)
        status.append("Pending")
        print("Task added!")

    elif choice == 2:
        for i in range(len(tasks)):
            print(i + 1, tasks[i], "-", status[i])

    elif choice == 3:
        n = int(input("Enter task number: "))
        tasks[n - 1] = input("Enter new task: ")
        print("Task updated!")

    elif choice == 4:
        n = int(input("Enter task number: "))
        tasks.pop(n - 1)
        status.pop(n - 1)
        print("Task deleted!")

    elif choice == 5:
        n = int(input("Enter task number: "))
        status[n - 1] = "Completed"
        print("Task completed!")


    else:
        print("Invalid choice!")
