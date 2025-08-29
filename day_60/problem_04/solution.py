statuses = []

while True:
    print("1. Post status")
    print("2. View all statuses")
    print("3. Exit")
    
    choice = input("Choose option: ")
    
    if choice == "1":
        status = input("What's on your mind? ")
        statuses.append(status)
        print("Status posted!")
    
    elif choice == "2":
        print("All statuses:")
        for i, status in enumerate(statuses):
            print(str(i + 1) + ".", status)
    
    elif choice == "3":
        break