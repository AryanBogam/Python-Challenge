notifications = []

while True:
    print("1. Login (view notifications)")
    print("2. Add notification")
    print("3. Exit")
    
    choice = input("Choose option: ")
    
    if choice == "1":
        username = input("Enter username: ")
        
        user_notifications = []
        for notif in notifications:
            if notif["user"] == username:
                user_notifications.append(notif)
        
        if user_notifications:
            print("Your notifications:")
            for notif in user_notifications:
                print("-", notif["message"])
        else:
            print("No notifications!")
    
    elif choice == "2":
        username = input("Enter username: ")
        message = input("Enter notification message: ")
        notifications.append({"user": username, "message": message})
        print("Notification added!")
    
    elif choice == "3":
        break