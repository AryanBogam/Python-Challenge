groups = {}

while True:
    print("1. Create group")
    print("2. Add member to group")
    print("3. View groups")
    print("4. Exit")
    
    choice = input("Choose option: ")
    
    if choice == "1":
        group_name = input("Enter group name: ")
        groups[group_name] = []
        print("Group created!")
    
    elif choice == "2":
        group_name = input("Enter group name: ")
        if group_name in groups:
            member_name = input("Enter member name: ")
            groups[group_name].append(member_name)
            print("Member added!")
        else:
            print("Group not found!")
    
    elif choice == "3":
        print("All groups:")
        for group_name, members in groups.items():
            print("Group:", group_name)
            print("Members:", members)
            print()
    
    elif choice == "4":
        break