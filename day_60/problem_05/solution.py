messages = []

while True:
    print("1. Send message")
    print("2. View chat history")
    print("3. Exit")
    
    choice = input("Choose option: ")
    
    if choice == "1":
        sender = input("Your name: ")
        message = input("Your message: ")
        messages.append({"sender": sender, "message": message})
        print("Message sent!")
    
    elif choice == "2":
        print("Chat History:")
        for msg in messages:
            print(msg["sender"] + ":", msg["message"])
    
    elif choice == "3":
        break