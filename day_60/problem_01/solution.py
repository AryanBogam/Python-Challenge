users = {}

while True:
    print("1. Register")
    print("2. Login")
    print("3. Exit")
    
    choice = input("Choose option: ")
    
    if choice == "1":
        username = input("Enter username: ")
        password = input("Enter password: ")
        users[username] = password
        print("Registration successful!")
    
    elif choice == "2":
        username = input("Enter username: ")
        password = input("Enter password: ")
        
        if username in users and users[username] == password:
            print("Login successful!")
        else:
            print("Invalid credentials!")
    
    elif choice == "3":
        break