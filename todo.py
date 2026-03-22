tasks = []
while True:
    print("MENU")
    print("1.add task")
    print("2.view task")
    print("3.delete task")
    print("4.exit")

    choice = input("enter choice: ")

    if choice == "1":
        task = input("enter task: ")
        tasks.append(task)
        print("task added")

    elif choice == "2":
        if not tasks:
            print("no tasks to view")
        else:
            for i, p in enumerate(tasks):
                print(i + 1, p)
            print("viewed task")

    elif choice == "3":
        if not tasks:
            print("no tasks to delete")
        else:
            num = int(input("enter task number to delete: "))
            if num > 0 and num <= len(tasks):
                tasks.pop(num - 1)
                print("task deleted")
            else:
                print("invalid task number")

    elif choice == "4":
        print("exiting")
        break

    else:
        print("invalid choice")  